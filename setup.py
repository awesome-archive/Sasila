#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
        name='sasila',
        version='0.0.1',
        description=(
            'a simple spider system'
        ),
        long_description=open('README.rst').read(),
        author='DaVinciDW',
        author_email='darkwings_love@163.com',
        maintainer='DaVinciDW',
        maintainer_email='darkwings_love@163.com',
        license='MIT License',
        packages=['sasila'],
        platforms=["all"],
        url='https://github.com/DarkSand/Sasila',
        install_requires=[
            'Flask>=0.11.1',
            'redis>=2.10.5',
            'requests>=2.13.0',
            'six>=1.10.0',
            'SQLAlchemy>=1.1.4',
            'kafka_python>=1.3.1',
            'grequests>=0.3.0',
            'dill>=0.2.5',
            'selenium>=2.53.6',
            'lxml>=3.7.2',
            'beautifulsoup4>=4.6.0',
            'kafka>=1.3.3',
        ],
        classifiers=[
            'Development Status :: 2 - Pre-Alpha',
            "Environment :: Web Environment",
            "Intended Audience :: Developers",
            "Operating System :: OS Independent",
            "Topic :: Text Processing :: Indexing",
            "Topic :: Utilities",
            "Topic :: Internet",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2.6",
            "Programming Language :: Python :: 2.7",
        ],
)