#!/usr/bin/python3
# -*- coding: utf-8 -*-

from distutils.core import setup

VERSION = "1.0"

setup(
    name="gstmanager1",
    version=VERSION,
    description="gstmanager is a helper for building gstreamer applications",
    author="Florent Thiery",
    author_email="florent.thiery@ubicast.eu",
    url="https://github.com/UbiCastTeam/gstmanager",
    license="GNU/LGPLv3",
    packages=[
        'gstmanager1',
        'gstmanager1/detectors',
        'gstmanager1/sbins',
        'gstmanager1/sbins/encoders',
        'gstmanager1/sbins/analysis',
        'gstmanager1/sbins/sinks',
        'gstmanager1/sbins/sources',
        'gstmanager1/profiles'
    ],
    install_requires=[
        'gi',
        'libgstreamer1.0',
    ]
)
