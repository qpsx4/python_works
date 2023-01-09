from multiprocessing import Pool
import socket
from netaddr import IPRange
import itertools


def scan_host(hostname_port):
    hostname = str(hostname_port[0])
    port = hostname_port[1]
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    try:
        s.connect((hostname, port))
        print(f"{hostname} Port: {port}, is open")
    except socket.error:
        pass
    finally:
        s.close()


if __name__ == "__main__":

    port_list = (43, 80, 109, 110, 115, 118, 119, 143, 194, 220, 443, 540,
                 585, 591, 1112, 1433, 1443, 3128, 3197, 3306, 3899, 4224,
                 4444, 5000, 5432, 6379, 8000, 8080, 10000)

    ip_start, ip_end = input("Введите IP-IP: ").split("-")
    iprange = IPRange(ip_start, ip_end)

    ip_and_ports = list(itertools.product(iprange, port_list))
    p = Pool(4)
    p.map(scan_host, ip_and_ports)
