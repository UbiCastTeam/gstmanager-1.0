#!/usr/bin/python3
# -*- coding: utf-8 -*-


class AudioAnalyser(object):
    def __init__(self, sbin_content):
        self.tags = ["a_src"]
        self.sbin = " %s_tee. ! queue ! audioconvert ! %s ! fakesink silent=True" % (self.tags[0], sbin_content)


class VideoAnalyser(object):
    def __init__(self, sbin_content):
        self.tags = ["v_src"]
        self.sbin = " %s_tee. ! queue ! videoconvert ! %s ! fakesink silent=True" % (self.tags[0], sbin_content)
