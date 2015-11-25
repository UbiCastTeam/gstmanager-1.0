#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gstmanager1.profile import DefaultEncodingProfile


class DefaultDVProfile(DefaultEncodingProfile):
    def __init__(self):
        DefaultEncodingProfile.__init__(self)
        self.extension = "dv"
        self.video_width = 720
        self.video_height = 576
        self.video_bitrate = vb = 25146  # kbits/s
        self.audio_bitrate = ab = 1536000  # bits/s
        self.misc_bitrate = mb = 8700  # kbits/s
        self.total_bitrate = tb = (vb + mb) + ab/1000  # kbits/s
        self.total_bitrate_kB = tb*1024  #

    def get_total_bitrate(self):
        return self.total_bitrate
