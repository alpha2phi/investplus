import os
from setuptools import setup, find_packages


def read(fname):
    """
    Read the file content.

    :param fname str: File name.
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="investplus",
    version="0.0.1",
    author="alpha2phi",
    author_email="alpha2phi@gmail.com",
    description=("A library to scrape stock data."),
    license="BSD",
    keywords="stock scraping",
    url="https://github.com/alpha2phi/investplus",
    packages=find_packages(),
    long_description=read("README"),
    install_requires=requirements(filename="requirements.txt"),
    include_package_data=True,
    python_requires=">=3",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
