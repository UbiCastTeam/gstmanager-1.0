#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gstmanager1.profiles.ogg import OggDefaultRecordingProfile
from gstmanager1.sbins.encoder import VideoEncoder, AudioEncoder
from gstmanager1.sbins.muxer import Muxer
from gstmanager1.sbins.encoder import FileEncoder


class Mpeg4Encoder(VideoEncoder):
    def __init__(self, profile):
        self.description = "Mpeg4 encoder"
        self.type = "video"
        sbin = "queue ! ffenc_mpeg4 bitrate=%s ! queue" % profile.video_bitrate
        VideoEncoder.__init__(self, sbin, profile=profile)


class VorbisEncoder(AudioEncoder):
    def __init__(self, profile):
        self.description = "Vorbis encoder"
        self.type = "audio"
        sbin = "vorbisenc bitrate=%s" % profile.audio_bitrate
        AudioEncoder.__init__(self, sbin)


class IdentityEncoder(AudioEncoder):
    def __init__(self, profile):
        self.description = "Identity encoder"
        self.type = "audio"
        sbin = "identity silent=true"
        AudioEncoder.__init__(self, sbin)


class MkvMuxer(Muxer):
    def __init__(self):
        self.description = "Mkv Muxer"
        self.type = "audio/video"
        sbin = "matroskamux min-index-interval=1000000000"
        Muxer.__init__(self, sbin)


class MkvMpeg4Encoder(FileEncoder):
    def __init__(self, filename="/tmp/test.mkv", profile=OggDefaultRecordingProfile()):
        FileEncoder.__init__(self, filename)
        self.venc = Mpeg4Encoder(profile)
        self.aenc = IdentityEncoder(profile)
        # self.aenc = VorbisEncoder(profile)
        self.muxer = MkvMuxer()
        self.add_many(self.venc, self.aenc, self.muxer)
        self.tags = ["a_src", "v_src"]
        self.type = "audio-video"
        self.description = "Mkv/mpeg4 to File Encoder"
        self.sbin = "%s muxer_tee. ! filesink location=%s" % (self.pipeline_desc, filename)
