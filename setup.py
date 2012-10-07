#! /usr/bin/env python

# Public Domain (-) 2010-2011 The Tavutil Authors.
# See the Tavutil UNLICENSE file for details.

import sys

from distutils.command.build_ext import build_ext
from setuptools import Extension, setup

# ------------------------------------------------------------------------------
# Extensions
# ------------------------------------------------------------------------------

extensions = [
    Extension(
        "tavutil.lzf",
        ["tavutil/lzf.c", "tavutil/lzf/lzf_c.c", "tavutil/lzf/lzf_d.c"],
        include_dirs=["tavutil/lzf"],
        )
    ]

# TODO(tav): Disable the sandbox for now as it doesn't seem to work on OS X
# Lion.
#
# if sys.platform == 'darwin':
#     extensions.append(
#         Extension("tavutil.darwinsandbox", ["tavutil/darwinsandbox.c"])
#         )

# ------------------------------------------------------------------------------
# Run Setup
# ------------------------------------------------------------------------------

setup(
    name="tavutil",
    author="tav",
    author_email="tav@espians.com",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: Public Domain",
        "Operating System :: OS Independent",
        "Programming Language :: C",
        "Programming Language :: Cython",
        "Programming Language :: Python"
        ],
    cmdclass=dict(build_ext=build_ext),
    description="A collection of utility modules",
    ext_modules=extensions,
    install_requires=[
        "BeautifulSoup>=3.2.0",
        "ipaddr>=2.1.7",
        "tornado>=1.2.1"
        ],
    keywords=["async", "crypto", "sandbox", "utility", "redis", "zeroconf"],
    license="Public Domain",
    long_description=open('README.rst').read(),
    packages=["tavutil"],
    url="https://github.com/tav/tavutil",
    version="1.0.2",
    zip_safe=True
    )
