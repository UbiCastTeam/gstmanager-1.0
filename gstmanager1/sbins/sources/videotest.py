#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gstmanager1.sbins.source import VideoSource


class VideoTestSource(VideoSource):
    # Video Test Source class
    def __init__(self, device_id="0"):
        self.description = "Video Test Source"
        self.type = "video"
        sbin = "videotestsrc pattern=%s" % device_id
        VideoSource.__init__(self, sbin)
