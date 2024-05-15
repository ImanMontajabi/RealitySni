import os
import csv
import signal
import asyncio

import aiodns
from dotenv import load_dotenv
import tqdm.asyncio


load_dotenv()
token = os.getenv('ip_token')

# TODO: write docstring for functions
_DO_NOT_CANCEL_TASKS: set[asyncio.Task] = set()


def protect(task: asyncio.Task) -> None:
    _DO_NOT_CANCEL_TASKS.add(task)


def shutdown(sig: signal.Signals) -> None:
    print(f'Received exit signal {sig.name}')

    all_tasks = asyncio.all_tasks()
    task_to_cancel = all_tasks - _DO_NOT_CANCEL_TASKS

    for task in task_to_cancel:
        task.cancel()

    print(f'Cancelled {len(task_to_cancel)} out of {len(all_tasks)}')


def setup_signal_handler() -> None:
    """
    This function gets running loop and add specific signals to the loop.

    :param: None

    :return: None
    """
    loop = asyncio.get_running_loop()

    '''
    SIGHUP: Hangup Signal - connection lost
    SIGTERM: Termination Signal - completely done and termination
    SIGINT: Interrupt Signal - interrupt running process by pressing ctrl+c
    first "sig" is variable of for-loop (received signal) and second "sig" is 
    the argument passed to shutdown'''
    for sig in (signal.SIGHUP, signal.SIGTERM, signal.SIGINT):
        loop.add_signal_handler(sig, shutdown, sig)


async def dns_resolve(semaphore, resolver, host_name) -> dict:
    ipv4: list[str] = list()
    ipv6: list[str] = list()
    ip_v4_v6: dict[str, list[str]] = dict()
    output: dict[str, dict[str, list[str]]] = dict()

    async with semaphore:
        try:
            resp = await asyncio.wait_for(
                resolver.query(host_name, 'A'), timeout=3)
            for ip in resp:
                if ip:
                    ipv4.append(ip.host)
            ip_v4_v6['ipv4'] = ipv4

            resp = await asyncio.wait_for(
                resolver.query(host_name, 'AAAA'), timeout=3)
            for ip in resp:
                if ip:
                    ipv6.append(ip.host)
            ip_v4_v6['ipv6'] = ipv6
            output[host_name] = ip_v4_v6
            # print(output)
            return output
        except asyncio.CancelledError:
            print(f'Cancelled!!!!')
        except aiodns.error.DNSError:
            pass
        except asyncio.TimeoutError:
            pass


async def main() -> None:
    setup_signal_handler()

    '''Protect main task from being cancelled, otherwise it will cancel
    all other tasks'''
    protect(asyncio.current_task())

    resolver = aiodns.DNSResolver()
    semaphore = asyncio.Semaphore(1000)

    full_length = int(input('How many urls: '))
    host_names: list[str] = []

    base_path = os.path.dirname(__file__)
    csv_path = os.path.join(base_path, 'file2.csv')

    with open(csv_path) as csv_file:
        hosts = csv.reader(csv_file)
        for host in hosts:
            host_names.append(host[0])
            if len(host_names) >= full_length:
                break

    tasks = []
    results = []
    for host_name in host_names:
        tasks.append(dns_resolve(semaphore, resolver, host_name))

    '''wait for all tasks to finish and show progress bar'''
    for f in tqdm.asyncio.tqdm.as_completed(tasks):
        result = await f
        if result:
            results.append(result)
    # print(results)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, asyncio.CancelledError):
        print('App was interrupt')
    else:
        print('App was finished gracefully')
