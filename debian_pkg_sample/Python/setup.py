#!/usr/bin/python3

from setuptools import setup

packages = ["hello"]
requires = []

setup(
    name = "hello",
    version = "1.0.0",
    description = "Ubuntu Community Packaging Workshop",
    author = "kssim",
    author_email = "ksub0912@gmail.com",
    url = "https://github.com/kssim/2018-korea-ubuntu-packaging-workshop",
    packages = packages,
    package_dir = {"hello": "hello"},
    include_package_data = True,
    install_requires = requires,
    zip_safe = False,
)
