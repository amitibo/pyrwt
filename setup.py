# -*- coding: utf-8 -*-
"""
cyipot: Python wrapper for the Ipopt optimization package, written in Cython.

Copyright (C) 2012 Amit Aides
Author: Amit Aides <amitibo@tx.technion.ac.il>
URL: <http://http://code.google.com/p/cyipopt/>
License: EPL 1.0
"""
from setuptools import setup
from setuptools.extension import Extension
from distutils.sysconfig import get_python_lib
from Cython.Distutils import build_ext
import numpy as np
import os.path
import sys


PACKAGE_NAME = 'rwt'
VERSION = '0.1'
DESCRIPTION = 'A Cython wrapper to the IPOPT optimization package'
AUTHOR = 'Amit Aides'
EMAIL = 'amitibo@tx.technion.ac.il'
URL = "http://code.google.com/p/cyipopt/"

IPOPT_ICLUDE_DIRS=[]
IPOPT_ICLUDE_DIRS += [np.get_include()]

def main():
    setup(
        name=PACKAGE_NAME,
        version=VERSION,
        description=DESCRIPTION,
        author=AUTHOR,
        author_email=EMAIL,
        url=URL,
        packages=[PACKAGE_NAME],
        cmdclass = {'build_ext': build_ext},
        ext_modules = [
            Extension(
                PACKAGE_NAME + '.' + 'cyrwt',
                ['src/cyrwt.pyx'],
                include_dirs=IPOPT_ICLUDE_DIRS
            )
        ],
    )


if __name__ == '__main__':
    main()