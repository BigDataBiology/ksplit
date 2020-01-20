# -*- coding: utf-8 -*-
# Copyright (C) 2020, Luis Pedro Coelho
# vim: set ts=4 sts=4 sw=4 expandtab smartindent:
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.

import setuptools
import os

exec(compile(open('ksplit/ksplit_version.py').read(),
             'ksplit/ksplit_version.py', 'exec'))

long_description = open('README.md', encoding='utf-8').read()
packages = setuptools.find_packages()

classifiers = [
'Intended Audience :: Science/Research',
'Programming Language :: Python',
'Programming Language :: Python :: 3',
'Programming Language :: Python :: 3.6',
'Programming Language :: Python :: 3.7',
'Operating System :: OS Independent',
'License :: OSI Approved :: MIT License',
]

setuptools.setup(name = 'ksplit',
      version = __version__,
      description = 'K-SPLIT',
      long_description = long_description,
      long_description_content_type = 'text/markdown',
      author = 'Luis Pedro Coelho',
      author_email = 'luispedro@big-data-biology.org',
      license = 'MIT',
      platforms = ['Any'],
      classifiers = classifiers,
      packages = packages,
      entry_points={
          'console_scripts': [
              'ksplit = ksplit.main:main',
          ],
      },
      )

