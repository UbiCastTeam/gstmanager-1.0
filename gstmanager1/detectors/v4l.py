#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gstmanager1.detector import FileBasedDetector


class V4LDetector(FileBasedDetector):
    def __init__(self):
        FileBasedDetector.__init__(self, "/dev/video", "V4L")
