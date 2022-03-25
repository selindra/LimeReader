#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 11:29:11 2022

@author: selindra
"""

from setuptools import setup, find_packages
from pathlib import Path
from limereader.version import __version__

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='limereader',
    packages=find_packages(),
    version=__version__,
    description='Class to read data from LimeSDR',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='selindra',
    url='https://github.com/selindra/LimeReader',  # use the URL to the github repo
    license='GPLv3',
    keywords=['physics', 'atomic', 'mass', 'ion',
              'accelerators'],  # arbitrary keywords
    classifiers = [
        'Environment :: X11 Applications :: Qt',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Topic :: Scientific/Engineering :: Physics',
        'Intended Audience :: Science/Research',
    ],
    python_requires=">=3.6"

)