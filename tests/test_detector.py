#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import sys

from gstmanager1.detectors.alsa import AlsaDetector
from gstmanager1.detectors.firewire import FirewireDetector
from gstmanager1.detectors.v4l import V4LDetector
from gstmanager1.sbins.sources.alsa import AlsaSource
from gstmanager1.sbins.sources.v4l import V4LSource

if __name__ == '__main__':

    logging.basicConfig(
        level=getattr(logging, "DEBUG"),
        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        stream=sys.stderr
    )

    sbins = []

    a = AlsaDetector()
    a.detect_devices()

    for device in a.devices_list:
        alsa_sbin = AlsaSource(device_id=device)
        sbins.append(alsa_sbin)

    d_v4l = V4LDetector()
    d_v4l.detect_devices()

    for device in d_v4l.devices_list:
        v4l_sbin = V4LSource(device_id=device)
        sbins.append(v4l_sbin)
    d_fire = FirewireDetector()
    d_fire.detect_devices()

    for sbin in sbins:
        print("Got %s %s, gstreamer source bin is: %s" % (sbin.type, sbin.description, sbin.sbin))
