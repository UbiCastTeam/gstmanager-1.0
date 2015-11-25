#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gstmanager1.sbins.source import AudioSource


class AlsaSource(AudioSource):
    def __init__(self, device_id="0", latency_time="10000"):
        self.description = "Alsa source"
        self.type = "audio"
        sbin = "alsasrc device=hw:%s latency-time=%s" % (device_id, latency_time)
        AudioSource.__init__(self, sbin)
