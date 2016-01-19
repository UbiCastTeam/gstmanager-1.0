#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import easyevent
import logging
import sys

from gi.repository import GObject
from gstmanager1.gstmanager1 import PipelineManager
logger = logging.getLogger('message_test')


class Actioner(easyevent.User):
    def __init__(self, pipelinel):
        easyevent.User.__init__(self)
        self.pipelinel = pipelinel
        self.signal_identity = None
        self.identity = None
        self.register_event("eos")

    def connect_identity(self):
        self.identity = self.pipelinel.pipeline.get_by_name("identity")
        self.signal_identity = self.identity.connect("handoff", self.identity_callback)

    def evt_eos(self, event):
        logger.info("EOS Received")
        self.identity.disconnect(self.signal_identity)
        self.pipelinel.stop()
        sys.exit()

    def identity_callback(self, element, buf):
        print(buf.pts)

if __name__ == '__main__':

    logging.basicConfig(
        level=getattr(logging, "DEBUG"),
        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        stream=sys.stderr
    )

    pipeline_desc = "videotestsrc num-buffers=100 ! videobalance ! identity silent=false signal-handoffs=true name=identity ! xvimagesink"

    pipelinel = PipelineManager(pipeline_desc)
    actioner = Actioner(pipelinel)
    pipelinel.run()
    actioner.connect_identity()

    main_loop = GObject.MainLoop()
    main_loop.run()
