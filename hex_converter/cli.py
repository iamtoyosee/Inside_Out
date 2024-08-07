# hex_converter/cli.py

import argparse
from .converters import (
    hex_to_ascii, ascii_to_hex,
    hex_to_decimal, decimal_to_hex,
    hex_to_binary, binary_to_hex
)
from .utils import validate_hex_input, validate_binary_input

def print_menu():
    print("Select a conversion operation:")
    print("1. Hex to ASCII")
    print("2. ASCII to Hex")
    print("3. Hex to Decimal")
    print("4. Decimal to Hex")
    print("5. Hex to Binary")
    print("6. Binary to Hex")
    print("0. Exit")

def main():
    parser = argparse.ArgumentParser(
        description='Convert between hex, ASCII, decimal, and binary formats.'
    )
    parser.add_argument(
        '-c', '--choice',
        type=int,
        help='Choose the conversion operation',
        required=True
    )
    parser.add_argument(
        '-i', '--input',
        help='Input value for conversion',
        required=True
    )
    
    args = parser.parse_args()

    if args.choice == 1:
        result = hex_to_ascii(validate_hex_input(args.input))
    elif args.choice == 2:
        result = ascii_to_hex(args.input)
    elif args.choice == 3:
        result = hex_to_decimal(validate_hex_input(args.input))
    elif args.choice == 4:
        result = decimal_to_hex(args.input)
    elif args.choice == 5:
        result = hex_to_binary(validate_hex_input(args.input))
    elif args.choice == 6:
        result = binary_to_hex(validate_binary_input(args.input))
    elif args.choice == 0:
        print("Exiting...")
        return
    else:
        print("Invalid choice. Please select a valid option.")
        print_menu()
        return

    print(result)

if __name__ == "__main__":
    print_menu()
    main()
