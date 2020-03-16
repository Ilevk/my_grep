import argparse
from src.my_grep import *


def main():
    parser = argparse.ArgumentParser(description='My grep arguments')

    parser.add_argument('-o', '--option', type=str, required=False, help="Grep options")
    parser.add_argument('-p', '--pattern', type=str, required=True, help="String Pattern")
    parser.add_argument('-f', '--file', type=str, required=True, help="File Path to find Pattern")

    args = parser.parse_args()

    print(f'option: {args.option}, pattern: {args.pattern}, file: {args.file}')
    logging.info(f'args: {args.option, args.pattern, args.file}')

    mg = My_grep(args.option, args.pattern, args.file)
    mg.load_find()
    mg.print_pattern()

if __name__ == '__main__':
    main()
