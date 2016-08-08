#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from gi.repository import GObject
from gstmanager1.gstmanager1 import PipelineManager


def set_input(pipelinel, value):
    print("Switching to pad %s" % value)
    selector = pipelinel.pipeline.get_by_name("select")
    newpad = selector.get_static_pad("sink_%s" % value)
    selector.set_property("active-pad", newpad)
    pipelinel.pause()
    pipelinel.play()

if __name__ == '__main__':

    pipeline_desc = "videotestsrc is-live=true ! timeoverlay ! queue ! input-selector name=select sync-mode=1 ! tee name=tee ! queue ! theoraenc ! oggmux name=mux ! filesink location=/tmp/test.ogg tee. ! queue ! xvimagesink videotestsrc pattern=2 is-live=true ! timeoverlay ! queue ! select. audiotestsrc is-live=true ! vorbisenc ! mux."

    pipelinel = PipelineManager(pipeline_desc)
    print(pipeline_desc)
    pipelinel.run()

    selector = pipelinel.pipeline.get_by_name("select")
    print("Active pad: %s" % selector.get_property("active-pad"))

    # Let's schedule some property changing
    GObject.timeout_add(2000, set_input, pipelinel, 1)
    GObject.timeout_add(4000, set_input, pipelinel, 0)
    GObject.timeout_add(7000, set_input, pipelinel, 1)
    GObject.timeout_add(10000, pipelinel.send_eos)

    main_loop = GObject.MainLoop()
    GObject.timeout_add(15000, main_loop.quit)
    main_loop.run()
