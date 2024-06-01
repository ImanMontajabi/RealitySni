<p align="center">
    <img src="https://github.com/ImanMontajabi/TLS-Checker/assets/52942515/bb20a89e-94cc-4b6a-86a7-29622c42dad6" alt="TLS-Checker" width="200"
</p>



<h1 align="center">TLS-Checker V2 🚀️</h1>


<p align="center">این اسکنر با گرفتن لیستی از دامین‌ها، اطلاعات مورد استفاده برای کاربردهایی نظیر تحلیل‌های آماری، نظارت و مدیریت و اسکن شبکه را در اختیار قرار میدهد و به عنوان یک ابزار سریع میتواند مورد استفاده قرار بگیرد. سابقا برای ساختن پروکسی نیز کارآمد بود.</p>

---------------------------

## محیط برنامه

<p align="center">
    <img src="https://github.com/ImanMontajabi/TLS-Checker/assets/52942515/e138379a-b695-4784-a337-b13ca8260210" alt="menu-1" width="600"/>
</p>

## نمونه خروجی برنامه

| domain_name | ipv4 | ipv6 | asn | asn_organ | iso_code | country | cipher | tls_version | issuer_organ | ping |
|-------------|------|------|-----|-----------|----------|---------|--------|-------------|--------------|------|
| oup.com | 75.2.119.185 | NULL | 16509 | AMAZON-02 | US | United States | ECDHE-RSA-AES128-GCM-SHA256 | TLSv1.2 | Amazon | 40 |
| google.ca | 216.239.38.120 | 2001:4860:4802:32::78 | 15169 | GOOGLE | US| United States | TLS_AES_256_GCM_SHA384 | TLSv1.3 | Google Trust Services LLC | 43 |
| nvidia.com | 34.194.97.138 | NULL | 14618 | AMAZON-AES | US | United States | ECDHE-RSA-AES128-GCM-SHA256 | TLSv1.2 | Amazon | NULL |

> [!tip]
> پیش نمایش کاملتری از خروجی رو میتونید از [اینجا](https://github.com/ImanMontajabi/TLS-Checker/blob/main/TLS-Checker/csv/results.csv#L77) مشاهده کنید.

 ## نصب و راه اندازی


### پیش‌نیازها

> [!IMPORTANT]
> برای استفاده از حداکثر ۱۰۰۰ عدد دامین نیازی به استفاده از pypy نیست و مفسر پایتون عملکرد قابل قبولی ارائه میکند ولی برای استفاده‌ی بیش از این مقدار توصیه‌ی اکید به استفاده از کامپایلر pypy می‌گردد.

- python `3.10` [Link](https://www.python.org/downloads)
- pypy `3.10` [Link](https://www.pypy.org/download.html)

> [!IMPORTANT]
>  توجه کنید که pypy نیازی به نصب کردن ندارد و پس از دانلود صرفا مانند اجرای یک اسکریپت پایتونی مانند دستور زیر از آن استفاده می‌شود. برای اجرای برنامه به آدرس محل فایل اجرایی pypy و محل فایل main.py این برنامه که از قسمت Release دانلود کردید نیاز دارید یا این که وارد پوشه‌ی حاوی main.py بشوید و با تایپ مسیر pypy در ابتدای main.py آن را اجرا کنید

 ### اجرای برنامه
 
 - در ابتدا مطمئن شوید که پیشنیازهای برنامه را نصب کرده‌اید برای استفاده از pypy و احتمالا ایجاد virtualenv از این راهنمای داکیومنت رسمی pypy کمک بگیرید.[لینک](https://doc.pypy.org/en/latest/install.html#installing-more-modules)
 - پیشنیازهای برنامه را نصب کنید و سپس برنامه را اجرا کنید :blueberries:
 - 
۱. نصب پیش‌نیاز
```
~/.../pypy-folder/bin/pypy3 -m pip install -r ~/.../TLS-Checker-folder/requirements.txt
```
یا بعد از رفتن به مسیر فایل requirements.txt
```
~/.../pypy-folder/bin/pypy3 -m pip install -r ./requirements.txt
```

۲. اجرا
 
 ```
~/.../pypy-folder/bin/pypy3 ~/.../TLS-Checker-folder/main.py
```
یا بعد از رفتن به مسیر فایل main.py
```
~/.../pypy-folder/bin/pypy3 ./main.py
```
