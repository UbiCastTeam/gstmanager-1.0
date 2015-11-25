#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gstmanager1.sbins.analyse import AudioAnalyser


class LevelAnalyser(AudioAnalyser):
    def __init__(self):
        self.description = "Audio level analysis component"
        self.type = "audio"
        sbin = "level"
        self.msg_evt_name = "level"
        self.msg_evt_fields = ["peak", "decay"]
        AudioAnalyser.__init__(self, sbin)
