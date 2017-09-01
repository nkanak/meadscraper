#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'lxml==3.8.0',
    'beautifulsoup4==4.6.0',
    'requests==2.18.3',
    # TODO: put package requirements here
]

setup_requirements = [
    # TODO(nkanak): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    # TODO: put package test requirements here
    'tox==2.3.1',
]

setup(
    name='meadscraper',
    version='0.1.0',
    description="Mead UPatras website scraper",
    long_description=readme + '\n\n' + history,
    author="nkanak",
    author_email='nikos.kanakaris89@gmail.com',
    url='https://github.com/nkanak/meadscraper',
    packages=find_packages(include=['meadscraper']),
    entry_points={
        'console_scripts': [
            'meadscraper=meadscraper.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="GNU General Public License v3",
    zip_safe=False,
    keywords='meadscraper',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
