#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gstmanager1.sbins.source import VideoSource


class ElphelSource(VideoSource):
    def __init__(self, device_id="ip"):
        self.description = "Elphel 353 optimized source"
        self.type = "video"
        # TODO: grab real current resolution using web calls
        output_caps = "video/x-raw, width=(int)1920, height=(int)1088, framerate=(fraction)25/1, format=(string)I420"
        sbin = 'rtspsrc location=rtsp://%s:554 protocols=0x00000001 latency=10 ! rtpjpegdepay ! jpegdec ! videorate name=videorate ! %s' % (device_id, output_caps)
        VideoSource.__init__(self, sbin)
