#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='CW-Neural-Network-Recognition',
    version='1.0',
    description='Course work and various uses of neural networks',
    url='https://github.com/Andinoriel/CW-Neural-Network-Recognition.git',
    author='andinoriel',
    author_email='36269798+Andinoriel@users.noreply.github.com',
    license='GPL-3.0',
    packages=['CW-Neural-Network-Recognition'],
    nstall_requires=['requests', 'PyQt5', 'numpy', 'tensorflow', 'dlib', 'PIL', 'scikit-image'] # external packages as dependencies
    # install manually:
    #       tensorflow.object_detection
    #       tensorflow.object_detection.utils
    #       ...
)