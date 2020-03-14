import argparse
import logging
from src.my_grep import *


def main():
    parser = argparse.ArgumentParser(description='My grep arguments')

    parser.add_argument('-o', '--option', type=str, required=False, help="Grep options")
    parser.add_argument('-p', '--pattern', type=str, required=True, help="String Pattern")
    parser.add_argument('-f', '--file', type=str, required=False, help="File Path to find Pattern")

    args = parser.parse_args()

    print(f'args: {args}')
    logging.info(f'args: {args}')


if __name__ == '__main__':
    main()
