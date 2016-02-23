#!/usr/bin/python3
# -*- coding: utf-8 -*-

import easyevent


class DefaultEncodingProfile(easyevent.User):
    def __init__(self):
        easyevent.User.__init__(self)
        # In kbits/s
        self.video_bitrate = 2000
        # In bits/s
        self.audio_bitrate = 128000
        # In kbits/s
        self.video_width = 320
        self.video_height = 240
        self.video_framerate = 25
        self.register_event("sos")

    def evt_sos(self, event):
        pass

    def get_string(self):
        return self.__dict__

    def get_total_bitrate(self):
        total_bitrate = self.video_bitrate + self.audio_bitrate/1000
        return total_bitrate
