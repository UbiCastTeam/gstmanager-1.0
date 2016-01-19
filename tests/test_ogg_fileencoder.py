#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# SBins are for "String Bins": manipulating Bins directly with Python can be tricky, notably because of the API differences (and lack of documentation porting) with the C API. Using string-based bin-like manipulation offers some flexibility over raw bin programming

import easyevent
import logging
import sys
logger = logging.getLogger("ogg-encoder")

from gi.repository import GObject

from gstmanager1.gstmanager1 import PipelineManager
from gstmanager1.profiles.ogg import OggDefaultRecordingProfile
from gstmanager1.sbinmanager import SBinManager
from gstmanager1.sbins.sources.audiotest import AudioTestSource
from gstmanager1.sbins.encoders.ogg import OggEncoder
from gstmanager1.sbins.sources.videotest import VideoTestSource
from gstmanager1.sbins.sinks.xvimagesink import XVImageSink


class OggRecordingProfile(OggDefaultRecordingProfile):
    def __init__(self):
        OggDefaultRecordingProfile.__init__(self)
        self.video_width = 640
        self.video_height = 480


class Actioner(easyevent.User):
    def __init__(self):
        easyevent.User.__init__(self)
        self.register_event("eos")
        self.register_event("caps")
        self.register_event("encoding_progress")
        self.register_event("encoding_error")

    def evt_eos(self, event):
        logger.info("EOS Received")
        sys.exit(0)

    def evt_encoding_progress(self, event):
        size = event.content.size
        dur = event.content.hduration
        print("Filesize is %s, at duration %s" % (size, dur))

    def evt_encoding_error(self, event):
        print("Error, encoding stalled")
        sys.exit(1)

logging.basicConfig(
    level=getattr(logging, "DEBUG"),
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    stream=sys.stderr
)


class OggEncodingTestApp(SBinManager, PipelineManager):
    def __init__(self, vsource, asource, previewsink):
        SBinManager.__init__(self)
        profile = OggRecordingProfile()
        self.encoder = encoder = OggEncoder(filename="/tmp/test", profile=profile)
        self.add_many(vsource, asource, previewsink, encoder)
        print(self.pipeline_desc)
        PipelineManager.__init__(self, self.pipeline_desc)

if __name__ == '__main__':

    v = VideoTestSource()
    a = AudioTestSource()
    sink = XVImageSink()

    encoder = OggEncodingTestApp(v, a, sink)

    listener = Actioner()

    GObject.timeout_add(100, encoder.run)
    main_loop = GObject.MainLoop()
    main_loop.run()
