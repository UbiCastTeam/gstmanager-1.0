#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger('sbinmanager')


class SBinManager(object):
    def __init__(self):
        self.pipeline_desc = ""
        self.check_for_compat = True

    def add_sbin(self, element):
        if self.check_for_compat and "source" in element.type:
            if element.sbin.find("tee name=%s_tee" % element.tags[0]) != -1:
                logger.info("Adding %s source %s to pipeline" % (element.type, element.description))
                self._add_sbin(element.sbin)
            else:
                oks = 0
                for tag in element.tags:
                    if "name=%s_tee" % tag in self.pipeline_desc:
                        oks += 1

                if not len(element.tags) == oks:
                    logger.error("Compatible %s source branch not found to fit %s" % (element.type, element.description))
                else:
                    logger.info("Adding branch %s %s to pipeline" % (element.type, element.description))
                    self._add_sbin(element.sbin)
        else:
            self._add_sbin(element.sbin)

    def add_many(self, *args):
        for element in args:
            if element is not None:
                self.add_sbin(element)

    def _add_sbin(self, sbin):
        self.pipeline_desc += "%s " % sbin

    def get_pipeline(self):
        logger.info("Pipeline is:\n%s" % self.pipeline_desc)
