#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gi.repository import GObject
from gstmanager1.event import User
from gstmanager1.gstmanager1 import PipelineManager


class Test(User):
    def __init__(self):
        User.__init__(self)
        self.register_event("drop_value_change")

    def evt_drop_value_change(self, event):
        data = event.content["value"]
        src = event.content["source"]
        property = event.content["property"]
        print("%s reports %s prop change to value %s" % (src, property, data))


caps_in = "video/x-raw, format=(string)YUY2, width=(int)320, height=(int)240, framerate=(fraction)30/1"
caps_out = "video/x-raw, format=(string)YUY2, width=(int)320, height=(int)240, framerate=(fraction)25/1"
pip = "videotestsrc ! %s ! videorate ! %s ! fakesink" % (caps_in, caps_out)

p = PipelineManager(pip)

p.play()
p.activate_polling_of_property_on_element(element_name="videorate0", property="drop", interval_ms=500)
print("Will poll element videorate for drop values for 10 seconds on 500ms interval")

t = Test()

main_loop = GObject.MainLoop()
GObject.timeout_add_seconds(10, p.deactivate_pollings)
GObject.timeout_add_seconds(12, p.stop)
GObject.timeout_add_seconds(12, main_loop.quit)
main_loop.run()
