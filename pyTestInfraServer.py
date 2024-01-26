from prometheus_client import start_http_server, Counter, Enum, Gauge, generate_latest

import dns
import dns.resolver 

def test_google_dns():
    result = dns.resolver.query('google.com', 'A')

    for ipval in result:
        print('IP', ipval.to_text())

result = dns.resolver.query('google.com', 'MX')
for ipval in result:
    print('IP', ipval.to_text())
