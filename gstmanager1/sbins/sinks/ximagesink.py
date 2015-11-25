#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gstmanager1.sbins.sink import VideoSink


class XImageSink(VideoSink):
    # X Image Sink class
    def __init__(self):
        self.description = "X Image Sink"
        self.type = "video"
        sbin = "ximagesink max-lateness=-1"
        VideoSink.__init__(self, sbin)
