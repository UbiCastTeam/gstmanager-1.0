#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gstmanager1.sbins.source import AudioSource


class AudioTestSource(AudioSource):
    def __init__(self, num_buffers=-1):
        self.description = "Audio test Source class, generates 440Hz tone"
        self.type = "audio"
        sbin = "audiotestsrc num-buffers=%s" % (num_buffers)
        AudioSource.__init__(self, sbin)
