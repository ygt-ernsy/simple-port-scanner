import argparse
from scanner import scan_concurent_ip, scan_given_port, scan_sequential_ip

parser = argparse.ArgumentParser(
    prog='Port scanner',
    description='Scans for open ports on a target IP.',
    epilog='Example: python scanner.py -sT localhost --concurrent'
)

parser.add_argument('-sT', nargs='+', help='Target IP and optional Port (e.g., "127.0.0.1" or "127.0.0.1 80")', required=True)
parser.add_argument('--concurent', action='store_true', help='Use multi-threading for faster scanning')

args = parser.parse_args()

target_ip = args.sT[0]

if len(args.sT) == 2:
    target_port: int = int(args.sT[1])
    print(f"Scanning single port {target_port} on {target_ip}...")
    if scan_given_port(target_ip, target_port):
        print('open')
    else:
        print('closed')

elif len(args.sT) == 1:
    if args.concurent:
        found = scan_concurent_ip(target_ip)
    else:
        found = scan_sequential_ip(target_ip)
    print(f"\nScan complete. Open ports: ")
    for port in found:
        print(port)
else:
    print("Error: Too many arguments for -sT. Please provide IP, or IP and Port.")
