#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gstmanager1.sbins.encoder import AudioEncoder
from gstmanager1.sbins.encoder import DefaultEncodingProfile
from gstmanager1.sbins.encoder import VideoEncoder


class H264Encoder(VideoEncoder):
    def __init__(self, bytestream="False", profile=DefaultEncodingProfile()):
        self.description = "h264 encoder"
        self.type = "video"
        if hasattr(profile, 'keyframe_freq'):
            keyframe_freq = profile.keyframe_freq
        else:
            keyframe_freq = 0
        sbin = "videobalance name=vlivemute ! x264enc bitrate=%s threads=%s byte-stream=%s key-int-max=%s" % (profile.video_bitrate, profile.encoding_threads, bytestream, keyframe_freq)
        VideoEncoder.__init__(self, sbin, profile)


class AACEncoder(AudioEncoder):
    def __init__(self, profile=DefaultEncodingProfile()):
        self.description = "AAC encoder"
        self.type = "audio"
        sbin = "volume name=alivemute ! faac bitrate=%s profile=2" % profile.audio_bitrate
        AudioEncoder.__init__(self, sbin)
