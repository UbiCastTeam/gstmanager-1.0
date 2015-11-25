#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gstmanager1.detector import ParserBasedDetector


class AlsaDetector(ParserBasedDetector):
    def __init__(self):
        ParserBasedDetector.__init__(self, "/proc/asound/cards", "Alsa sound card")

    def parse(self):
        nb_devices = len(self.data) / 2
        self.devices_list = range(int(nb_devices))

if __name__ == "__main__":
    a = AlsaDetector()
    l = a.detect_devices()
    print(l)
