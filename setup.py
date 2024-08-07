from setuptools import setup, find_packages

setup(
    name='hex_converter',
    version='0.1',
    author='BlackTechieGirl',
    author_email='blacktechiegirl@gmail.com',
    url='https://github.com/iamtoyosee/Inside_Out',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'hex-converter=hex_converter.cli:main',
        ],
    },
    description='A command-line tool for converting between hex, ASCII, decimal, and binary.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
