#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gstmanager1.sbins.source import AudioSource


class AudioTestSource(AudioSource):
    def __init__(self):
        self.description = "Audio test Source class, generates 440Hz tone"
        self.type = "audio"
        sbin = "audiotestsrc"
        AudioSource.__init__(self, sbin)
