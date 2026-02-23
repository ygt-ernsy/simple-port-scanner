import argparse
from typing import Tuple
from scanner import *

parser = argparse.ArgumentParser(
    prog='Port scanner',
    description='Scans for open ports on a target IP.',
    epilog='Example: python scanner.py -sT localhost --concurrent'
)

parser.add_argument('-sT', nargs='+', help='Target IP and optional Port (e.g., "127.0.0.1" or "127.0.0.1 80")')
parser.add_argument('--concurent', action='store_true', help='Use multi-threading for faster scanning. Note: Only supports -sT for now')
parser.add_argument('-gS', help='Gets the service of the given local port. Note do not give ip adrress this flag is only for local ports.') # The should be thought on further
parser.add_argument('-b', nargs='+', help='Attempts to get the service banner of a given port.')

args = parser.parse_args()

if args.sT:
    # target_ip = args.sT[0]
    # target_port = args.sT[1]

    if len(args.sT) == 2:
        print(f"Scanning single port {int(args.sT[1])} on {args.sT[0]}...")
        if scan_given_port(args.sT[0], int(args.sT[1])):
            print('open')
        else:
            print('closed')

    elif len(args.sT) == 1:
        if args.concurent:
            found = scan_concurent_ip(args.sT[0])
        else:
            found = scan_sequential_ip(args.sT[0])
        print(f"\nScan complete. Open ports: ")
        for port in found:
            print(port)
    else:
        print("Error: Too many arguments for -sT. Please provide IP, or IP and Port.")

elif args.gS:
    service: str = get_service_of_port(int(args.gS))

    if service != '':
        print(f"The service of the port {int(args.gS)} is {service}.")
    else:
        print(f"The service of the port {int(args.gS)} is unknown.")

elif args.b:
    print(get_service_banner(args.b[0], int(args.b[1])))
