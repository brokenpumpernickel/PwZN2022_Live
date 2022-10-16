# import sys
# print(sys.argv)

import argparse
from ast import arg

parser = argparse.ArgumentParser()
parser.add_argument('file_name')
parser.add_argument('-a', '--additional', default = 'default_file.py')
parser.add_argument('-f', '--format', action = 'store_true')
parser.add_argument('-o', '--others', nargs = '*')

args = parser.parse_args()
#print(f'fsd {args.file_name} dsfsdf dsada {3 + 8}')
print(f'{args.file_name = }')
print(f'{args.additional = }')
print(f'{args.format = }')
print(f'{args.others = }')