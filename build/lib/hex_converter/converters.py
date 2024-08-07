# hex_converter/converters.py

def hex_to_ascii(hex_str):
    """Convert hexadecimal string to ASCII."""
    try:
        bytes_object = bytes.fromhex(hex_str)
        return bytes_object.decode('ascii')
    except ValueError:
        return "Invalid hex string"
    except UnicodeDecodeError:
        return "Hex string does not represent valid ASCII"

def ascii_to_hex(ascii_str):
    """Convert ASCII string to hexadecimal."""
    return ascii_str.encode('ascii').hex()

def hex_to_decimal(hex_str):
    """Convert hexadecimal string to decimal."""
    try:
        return int(hex_str, 16)
    except ValueError:
        return "Invalid hex string"

def decimal_to_hex(decimal):
    """Convert decimal to hexadecimal string."""
    try:
        return hex(int(decimal))[2:]
    except ValueError:
        return "Invalid decimal value"

def hex_to_binary(hex_str):
    """Convert hexadecimal string to binary."""
    try:
        return bin(int(hex_str, 16))[2:]
    except ValueError:
        return "Invalid hex string"

def binary_to_hex(binary_str):
    """Convert binary string to hexadecimal."""
    try:
        return hex(int(binary_str, 2))[2:]
    except ValueError:
        return "Invalid binary string"
