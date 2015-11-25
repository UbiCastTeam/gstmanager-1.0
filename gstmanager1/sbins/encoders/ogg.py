#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gstmanager1.profiles.ogg import OggDefaultRecordingProfile
from gstmanager1.sbins.encoder import VideoEncoder, AudioEncoder
from gstmanager1.sbins.muxer import Muxer
from gstmanager1.sbins.encoder import FileEncoder


class TheoraEncoder(VideoEncoder):
    def __init__(self, profile):
        self.description = "Theora encoder"
        self.type = "video"
        sbin = "theoraenc bitrate=%s keyframe-auto=False keyframe-force=%s keyframe-freq=%s" % (profile.video_bitrate, profile.keyframe_freq, profile.keyframe_freq)
        VideoEncoder.__init__(self, sbin, profile=profile)


class VorbisEncoder(AudioEncoder):
    def __init__(self, profile):
        self.description = "Vorbis encoder"
        self.type = "audio"
        sbin = "vorbisenc bitrate=%s" % profile.audio_bitrate
        AudioEncoder.__init__(self, sbin)


class OggMuxer(Muxer):
    def __init__(self):
        self.description = "Ogg Muxer"
        self.type = "audio/video"
        sbin = "oggmux"
        Muxer.__init__(self, sbin)


class OggEncoder(FileEncoder):
    def __init__(self, filename="/tmp/test.ogg", profile=OggDefaultRecordingProfile()):
        FileEncoder.__init__(self, filename)

        self.venc = TheoraEncoder(profile)
        self.aenc = VorbisEncoder(profile)
        self.muxer = OggMuxer()
        self.add_many(self.venc, self.aenc, self.muxer)
        self.tags = ["a_src", "v_src"]
        self.type = "audio-video"
        self.description = "Ogg to File Encoder"
        self.sbin = "%s muxer_tee. ! filesink location=%s" % (self.pipeline_desc, filename)


class MkvTheoraEncoder(FileEncoder):
    def __init__(self, filename="/tmp/test.mkv", profile=OggDefaultRecordingProfile()):
        FileEncoder.__init__(self, filename)

        self.venc = TheoraEncoder(profile)
        self.aenc = VorbisEncoder(profile)
        from mjpeg import MkvMuxer
        self.muxer = MkvMuxer()
        self.add_many(self.venc, self.aenc, self.muxer)
        self.tags = ["a_src", "v_src"]
        self.type = "audio-video"
        self.description = "Mkv/Theora/Vorbis to File Encoder"
        self.sbin = "%s muxer_tee. ! filesink location=%s" % (self.pipeline_desc, filename)
