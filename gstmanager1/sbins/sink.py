#!/usr/bin/python3
# -*- coding: utf-8 -*-


class VideoSink(object):
    def __init__(self, sbin_content):
        self.tags = ["v_src"]
        self.sbin = "%s_tee. ! queue ! videoconvert ! %s" % (self.tags[0], sbin_content)


class AudioSink(object):
    def __init__(self, sbin_content):
        self.tags = ["a_src"]
        self.sbin = "%s_tee. ! queue ! audioconvert ! %s" % (self.tags[0], sbin_content)


class FakeSink():
    def __init__(self):
        self.description = "fake Sink"
        self.type = "fake"
        self.tags = ["v_src"]
        self.sbin = "%s_tee. ! queue ! fakesink" % (self.tags[0])
