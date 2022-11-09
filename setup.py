#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

setup(
    name='milvus-backup',
    version='0.0.1',
    author='Last',
    author_email='huan0016@gmail.com',
    url='https://github.com/InvisibleFuture/milvus-backup',
    description=u'Last',
    packages=['src'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'milvus-backup=jujube_pill:jujube',
            'milvus-update=jujube_pill:pill'
        ]
    }
)

