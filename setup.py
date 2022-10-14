#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pip

try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

## workaround derived from: https://github.com/pypa/pip/issues/7645#issuecomment-578210649
parsed_requirements = parse_requirements(
    'requirements/prod.txt',
    session='workaround'
)

parsed_test_requirements = parse_requirements(
    'requirements/test.txt',
    session='workaround'
)


requirements = [str(ir.req) for ir in parsed_requirements]
test_requirements = [str(tr.req) for tr in parsed_test_requirements]


setup(
    name='sampler_survey',
    version='0.1.0',
    description="Survey of different sampling methods",
    long_description=readme + '\n\n' + history,
    author="August George",
    author_email='georgeau@ohsu.edu',
    url='https://github.com/augeorge/sampler_survey',
    packages=[
        'sampler_survey',
    ],
    package_dir={'sampler_survey':
                 'sampler_survey'},
    include_package_data=True,
    install_requires=requirements,
    license="ISCL",
    zip_safe=False,
    keywords='sampler_survey',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
