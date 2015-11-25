#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gstmanager1.sbins.source import VideoSource, AudioSource


class DVVideoSource(VideoSource):
    """
    DV Video Source

    Constructor arguments:
    - device_id: DV port to use
    - filename: dump filename, if needed

    Since DV is a bit special, you can dump the raw dv stream
    by passing a non-Null *filename* argument
    """
    def __init__(self, device_id="0", filename=None):
        self.description = "Video DV (Firewire) source"
        self.type = "video_source"
        if filename is not None:
            dumper_str = "tee name=dump_tee ! queue ! filesink location=%s dump_tee. !" % filename
        else:
            dumper_str = ""
        v_caps = "video/x-raw, width=(int)720, height=(int)576, framerate=(fraction)25/1, format=(string)I420, pixel-aspect-ratio=(fraction)1/1"
        sbin = "dv1394src port=%s ! queue ! %s dvdemux name=dv_src ! queue ! dvdec ! ffmpegcolorspace ! ffdeinterlace ! videoscale ! %s" % (device_id, dumper_str, v_caps)
        VideoSource.__init__(self, sbin)


class DVAudioSource(AudioSource):
    def __init__(self):
        self.description = "Audio DV (Firewire) source"
        self.type = "audio"
        a_caps = "audio/x-raw-int"
        sbin = "dv_src. ! %s" % a_caps
        AudioSource.__init__(self, sbin)
