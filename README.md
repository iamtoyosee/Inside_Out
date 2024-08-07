# Hex Converter

A command-line tool for converting between hex, ASCII, decimal, and binary formats. The `hex-converter` utility provides a simple way to perform these conversions directly from the command line.

## Features

- Convert hexadecimal to ASCII and vice versa
- Convert hexadecimal to decimal and vice versa
- Convert hexadecimal to binary and vice versa

## Installation

### Local Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/hex-converter.git

2. Navigate to the Project Directory

    ```bash
    cd hex-converter

3. Build the package:

    ```bash
    python setup.py sdist bdist_wheel

4. Install the package locally:

    ```bash
    pip install dist/hex_converter-0.1.0-py3-none-any.whl --force-reinstall


## Usage

The `hex-converter` command-line tool allows you to perform various conversions between hexadecimal, ASCII, decimal, and binary formats. Use the following options to specify the type of conversion and provide the input value.

### Convert Hexadecimal to ASCII

```bash
hex-converter -c 1 -i <hexadecimal>

