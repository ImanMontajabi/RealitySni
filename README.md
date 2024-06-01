<p align="center">
    <img src="https://github.com/ImanMontajabi/TLS-Checker/assets/52942515/bb20a89e-94cc-4b6a-86a7-29622c42dad6" alt="TLS-Checker" width="200"
</p>



<h1 align="center">TLS-Checker</h1>
 
<p align="center">This Python script is designed to gather information about a list of domains</p>

[About](https://github.com/ImanMontajabi/TLS-Checker/edit/main/README.md#about) | [Output]() | [Screenshot]() | [Download & Install]() | [How to use]()

## About

The script collects various details about each domain, including:

- IPv4
- IPv6
- Autonomous System Number (ASN)
- ASN organization
- ISO code of the country
- Country name
- Cipher
- SSL/TLS version
- Issuer organization
- Ping response time from the domain's server

## Output

The results are saved in a SQLite database named output.db and a CSV file named results.csv. I've also provided an example below:

| domain_name | ipv4 | ipv6 | asn | asn_organ | iso_code | country | cipher | tls_version | issuer_organ | ping |
|-------------|------|------|-----|-----------|----------|---------|--------|-------------|--------------|------| 
| nvidia.com | 34.194.97.138 | NULL | 14618 | AMAZON-AES | US | United States | ECDHE-RSA-AES128-GCM-SHA256 | TLSv1.2 | Amazon | NULL |
