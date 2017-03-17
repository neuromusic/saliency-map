#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = "SaliencyMap",
    author="Mayo Yamasaki",
    license = "MIT License",
    version = "0.1",
    packages = find_packages(),
    test_suite = 'all_tests.suite'
)