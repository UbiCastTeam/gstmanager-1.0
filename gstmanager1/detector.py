#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger('detector')


class ParserBasedDetector(object):
    def __init__(self, file_path, type_desc):
        file_path = file_path
        file = open(file_path)
        self.data = file.readlines()
        self.type = type_desc
        file.close()
        self.devices_list = []

    def detect_devices(self):
        self.parse()
        for device in self.devices_list:
            logger.debug("Found %s device with id %s" % (self.type, device))
        return self.devices_list

    def parse(self):
        # Surclass this
        for line in self.data:
            self.devices_list.append(line)


class FileBasedDetector(object):
    def __init__(self, file_pattern, type_desc):
        self.file_pattern = file_pattern
        self.type = type_desc
        self.devices_list = []
        # TODO: use glob

    def detect_devices(self):
        i = 0
        while True:
            file = "%s%s" % (self.file_pattern, i)
            import os
            if os.path.exists(file):
                logger.debug("Found %s device at %s" % (self.type, file))
                self.devices_list.append(file)
                i += 1
            else:
                logger.info("Found %s %s device(s)" % (len(self.devices_list), self.type))
                return self.devices_list
