import argparse
from scanner import scan_given_port

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
