#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gstmanager1.sbins.analyse import VideoAnalyser


class BrightnessVideoAnalyse(VideoAnalyser):
    def __init__(self):
        self.description = "Brightness analysis component"
        self.type = "video"
        sbin = "videoanalyse message=true name=videoanalyse"
        self.msg_evt_name = "GstVideoAnalyse"
        self.msg_evt_fields = ["brightness", "brightness-variance"]
        VideoAnalyser.__init__(self, sbin)
