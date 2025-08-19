import ipaddress
import requests
import urllib3

from datetime import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def retrive_ips(url):
    headers = {
        'User-agent': "Moziliz/5.0"
    }
    try:
        req = requests.get(url=url, headers=headers, verify=False)
        return req.text
    except Exceptions as err:
        print(f"Request Error: {err}")
        exit(-1)

def calculate_ips(cidr):
    network = ipaddress.IPv4Network(cidr, strict=False)
    available_ips = list(network.hosts())
    if available_ips:
        return f"{available_ips[0]}-{available_ips[-1]}"
    else:
        return "No usable IPs available"

def write_dat(filename, data):
    with open(filename, 'a') as fn:
        fn.write(data+'\n')

if __name__ == '__main__':
    current_time = datetime.now()
    filename = 'ISP_China{}.dat'.format(current_time.strftime("%Y-%m-%d"))
    url = 'https://www.ipdeny.com/ipblocks/data/countries/cn.zone'
    write_dat(filename, '#desc:中国\n#desc_en:China')
    for ip_cidr in retrive_ips(url).split('\n')[:-1]:
        ip_range = calculate_ips(ip_cidr)
        write_dat(filename, ip_range)