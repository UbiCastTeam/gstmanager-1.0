#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import easyevent
import time

from gi.repository import GObject
from gstmanager1.gstmanager1 import PipelineManager


class Actioner(easyevent.User):
    def __init__(self):
        easyevent.User.__init__(self)
        self.register_event("caps")

    def evt_caps(self, event):
        print("Caps received, %s" % event.content)

if __name__ == '__main__':

    a = Actioner()

    pipeline_desc = "audiotestsrc ! faac ! rtpmp4gpay name=pay ! udpsink host=127.0.0.1 port=1234 name=sink"
    print("pipeline : %s" % (pipeline_desc))
    pipelinel = PipelineManager(pipeline_desc)

    def get_time(time_epoch):
        if time_epoch == 0:
            time_epoch = "never"
        else:
            time_epoch = time.ctime(time_epoch/1000000000)
        return time_epoch

    def get_udp_stats():
        sink = pipelinel.pipeline.get_by_name("sink")
        # Fixme return a structure but data ar not available
        struct_stat = sink.emit("get-stats", "127.0.0.1", 1234)
        # Should be struct_stat.get_value("bytes_sent")
        return True

    GObject.timeout_add(1000, get_udp_stats)
    GObject.threads_init()
    GObject.idle_add(pipelinel.activate_caps_reporting_on_element, "pay")
    GObject.idle_add(pipelinel.run)
    main_loop = GObject.MainLoop()
    GObject.timeout_add(5000, main_loop.quit)
    main_loop.run()
