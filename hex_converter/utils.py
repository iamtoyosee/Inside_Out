# hex_converter/utils.py

import re

def is_hex(s):
    """Check if a string is a valid hexadecimal number."""
    return re.fullmatch(r'[0-9a-fA-F]+', s) is not None

def is_binary(s):
    """Check if a string is a valid binary number."""
    return re.fullmatch(r'[01]+', s) is not None

def validate_hex_input(hex_str):
    """Validate and return a cleaned hexadecimal string."""
    if is_hex(hex_str):
        return hex_str
    else:
        return "Invalid hex input"

def validate_binary_input(binary_str):
    """Validate and return a cleaned binary string."""
    if is_binary(binary_str):
        return binary_str
    else:
        return "Invalid binary input"
