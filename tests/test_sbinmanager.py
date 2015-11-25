#!/usr/bin/env python
# -*- coding: utf-8 -*-

# SBins are for "String Bins": manipulating Bins directly with Python can be tricky, notably because of the API differences (and lack of documentation porting) with the C API. Using string-based bin-like manipulation offers some flexibility over raw bin programming

import logging
import sys
from gi.repository import GObject

from gstmanager1.gstmanager1 import PipelineManager
from gstmanager1.sbins.encoders.ogg import OggEncoder
from gstmanager1.sbins.sinks.alsa import AlsaSink
from gstmanager1.sbins.sinks.ximagesink import XImageSink
from gstmanager1.sbins.sources.audiotest import AudioTestSource
from gstmanager1.sbins.sources.videotest import VideoTestSource
from gstmanager1.sbinmanager import SBinManager

logging.basicConfig(
    level=getattr(logging, "DEBUG"),
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    stream=sys.stderr
)

v = VideoTestSource()

s = XImageSink()

s2 = AudioTestSource()

s3 = AlsaSink()

e = OggEncoder("/tmp/test.ogg")

man = SBinManager()

man.add_many(v, s, s2, s3, e)

if __name__ == '__main__':

    pipelinel = PipelineManager(man.pipeline_desc)
    pipelinel.run()
    GObject.timeout_add(2000, pipelinel.send_eos)
    GObject.timeout_add(3500, man.get_pipeline)
    main_loop = GObject.MainLoop()
    main_loop.run()
