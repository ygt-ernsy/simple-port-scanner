import concurrent.futures
import re
import socket
from typing import List

def scan_given_port(ip: str, port: int) -> bool:
    ip_used: str

    if ip == 'localhost':
        ip_used = '127.0.0.1'
    else:
        ip_used = ip

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        try:
            s.connect((ip_used, port))
            return True
        except socket.timeout:
            print('Connection timed out.')
            return False
        except  ConnectionRefusedError:
            print('Connection refused.')
            return False
        except OSError as e:
            print(f"Error: {e}")
            return False


def scan_sequential_ip(ip: str) -> List[str]:
    open_ports: List[str] = []
    for i in range(65536):
        if scan_given_port(ip, i):
            open_ports.append(f'{ip}:{i}')
    return open_ports

def scan_concurent_ip(ip: str) -> List[str]:
    open_ports: List[str] = []
    futures: dict[concurrent.futures.Future, str] = {}

    with concurrent.futures.ThreadPoolExecutor(max_workers=500) as executor:
        for i in range(65536):
            port_address = f"{ip}:{i}" 
            futures[executor.submit(scan_given_port, ip, i)] = port_address

        for future in concurrent.futures.as_completed(futures):
            try:
                if future.result():
                    open_ports.append(str(futures.get(future)))
            except Exception as e:
                print(e)

    return open_ports

def get_service_banner(ip: str, port: int) -> str:
    ip_used: str

    if ip == 'localhost':
        ip_used = '127.0.0.1'
    else:
        ip_used = ip

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        response_msg = ''
        try:
            s.connect((ip_used, port))
            response = s.recv(1024)

            try:
                response_msg = response.decode('utf-8').strip()
            except UnicodeDecodeError:
                response_msg = response.decode('latin-1').strip()

        except ConnectionRefusedError:
            print("Connection refused")
            pass
        except socket.timeout:
            print("Timed out")
            pass

        return response_msg



print(get_service_banner('1.1.1.1', 53))
