#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gstmanager1.sbins.sink import VideoSink


class XVImageSink(VideoSink):
    # XV Image Sink class
    def __init__(self, sync="True"):
        self.description = "XV Image Sink"
        self.type = "video"
        sbin = "xvimagesink max-lateness=-1 sync=%s" % sync
        VideoSink.__init__(self, sbin)
