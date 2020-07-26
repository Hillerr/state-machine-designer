import setuptools
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="state_machine", 
    packages=find_packages(),
    version="0.0.0",
    author = 'Hillerr',                   # Type in your name
    author_email = 'rafaelhiller23@gmail.com',
    description="State machine designer and implementation package",
    python_requires='>=3.6',
    url = 'https://github.com/Hillerr/state-machine-designer'
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    download_url = 'https://github.com/Hillerr/state-machine-designer/archive/v0.0.0.tar.gz'
    install_requires=requirements,
)