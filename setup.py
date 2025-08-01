#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (c) 2010-2014 Jennifer Ennis, William Tisäter.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/lgpl.txt>.
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from pygeoip import __version__

setup(name='pygeoip',
      version=__version__,
      description='GeoScanner 0.1.9',
      author='Jennifer Ennis',
      author_email='zaylea@gmail.com',
      maintainer='CipherTheDev',
      maintainer_email='ciphersec4@gmail.com',
      url='https://github.com/appliedsec/GeoIP',
      classifiers=['Programming Language :: Python',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.2',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.6',
                   'Programming Language :: Python :: 3.7',
                   'Programming Language :: Python :: 3.8',
                   'Programming Language :: Python :: 3.9',
                   'Programming Language :: Python :: 3.10',
                   'Programming Language :: Python :: 3.11',
                   'Programming Language :: Python :: 3.12',
                   'Programming Language :: Python :: 3.13'],
      packages=['pygeoip'],
      license='LGPLv3+',
      keywords='geoip')
