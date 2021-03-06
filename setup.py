#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This software is licensed as described in the README.rst and LICENSE
# files, which you should have received as part of this distribution.

import os
import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# noinspection PyPep8Naming
from rpi_doorman_gammu import __version__ as VERSION

read = lambda fname: open(os.path.join(os.path.dirname(__file__), fname)).read()

DEPS = ['RPi.GPIO', 'rpi-doorman']

CLASSIFIERS = [
    'Environment :: Console',
    'Intended Audience :: System Administrators',
    'Intended Audience :: Developers',
    'Operating System :: Unix',
    'Operating System :: POSIX :: Linux',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
    'Development Status :: 3 - Alpha',
    'Topic :: Utilities'
]

packages = [
    'rpi_doorman_gammu',
]

setup(
    name='rpi-doorman-gammu',
    version=VERSION,
    description='Door state monitor, with ability to make a phone call',
    long_description=read('README.rst'),
    author='Richard Kellner',
    author_email='richard.kellner [at] gmail.com',
    url='https://github.com/ricco386/rpi-doorman-gammu/',
    license='MIT',
    packages=packages,
    scripts=['bin/rpi-doorman-gammu'],
    install_requires=DEPS,
    platforms='any',
    classifiers=CLASSIFIERS,
    include_package_data=True
)
