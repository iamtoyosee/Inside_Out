from setuptools import setup, find_packages

setup(
    name='inside_out',
    version='0.1.0',
    author='BlackTechieGirl',
    author_email='blacktechiegirl@gmail.com',
    description='Advanced Encoder and Decoder Tool,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/iamtoyosee/Inside_Out',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},  # Source directory
    install_requires=[
       
    ],
    extras_require={
        
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
