import socket
import argparse

def scan_given_port(ip: str, port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        try:
            s.connect((ip, port))
            return True
        except Exception:
            return False

parser = argparse.ArgumentParser(
    prog='Port scanner',
    description='',
    epilog=''
)

parser.add_argument('-sT', nargs=2, help='')

args = parser.parse_args()

if args.sT:
    if scan_given_port(args.sT[0], int(args.sT[1])):
        print('open')
    else:
        print('closed')
