#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys

from gstmanager1.event import User
from gstmanager1.gstmanager1 import PipelineManager
from gi.repository import GObject
logger = logging.getLogger('Gstmanager1')


class EOS_actioner(User):
    # This class will subscribe to proxied eos messages
    def __init__(self, pipelinel):
        User.__init__(self)
        self.pipelinel = pipelinel
        self.register_event("eos")

    def evt_eos(self, event):
        # This is the callback used for every evt_MSGNAME received
        logger.info("EOS Recieved")
        self.pipelinel.stop()
        sys.exit()


def set_brightness(pipelinel, value):
    # set_property_on_element example
    pipelinel.set_property_on_element(element_name="balance", property_name="brightness", value=value)

if __name__ == '__main__':

    logging.basicConfig(
        level=getattr(logging, "DEBUG"),
        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        stream=sys.stderr
    )

    pipeline_desc = "videotestsrc num-buffers=100 ! videobalance name=balance ! xvimagesink"
    pipelinel = PipelineManager(pipeline_desc)
    eso_actioner = EOS_actioner(pipelinel)
    pipelinel.run()

    # Let's schedule some property changing
    GObject.timeout_add(2000, set_brightness, pipelinel, 0.2)

    main_loop = GObject.MainLoop()
    main_loop.run()
