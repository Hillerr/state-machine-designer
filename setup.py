import setuptools
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open('README.md', "r") as fh:
    long_description = fh.read()

setup(
    name="state-machine-designer", 
    packages=find_packages(),
    version="0.0.0",
    author = 'Hillerr',                   # Type in your name
    author_email = 'rafaelhiller23@gmail.com',
    description="State machine designer and implementation package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3.6',
    url = 'https://github.com/Hillerr/state-machine-designer',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    download_url = 'https://github.com/Hillerr/state-machine-designer/archive/v0.0.0.tar.gz',
    install_requires=requirements,
)