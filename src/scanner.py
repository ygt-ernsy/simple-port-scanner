import socket

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
        except ConnectionRefusedError:
            return False
        except socket.timeout:
            return False
        except OSError as e:
            print(f"Error: {e}")
            return False

