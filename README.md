GSTMANAGER-1.0
===============

Based on the gstreamer-1.0 python bindings, gstmanager is a python module containing a basic gstreamer programming context to ease application development, with an emphasis on string-based manipulations; it currently offers the following features:

  * PipelineManager: pipeline manipulation
    * launch from pipeline description string
    * states wrapping
    * position/seeking wrapping
    * EOS emission forcing
    * caps parsing
    * error parsing
    * element message proxy (to very easy to use event system) 
  * BinManager: bin manipulation
    * bin repository
    * states wrapping
  * Detector: devices detection (currently, Alsa, V4L and Firewire devices)
  * SBins (for String Bins): simple, string-based bin-alike definition and use

You can use gstmanager to create such workflows:
DETECT_SOURCES -> CHOOSE_SOURCES -> CHOOSE_PROCESSING -> BUILD_PIPELINE -> LAUNCH_PIPELINE -> CONTROL_PIPELINE

Complementary features:
  * logging support
  * easy to use event system

DEPS
====
    * python3
    * gstreamer and python bindings

COMPATIBILITY
=============
    * PipelineManager has been tested on Ubuntu 14.04 gstreamer environments
    * BinManager does not work on Ubuntu 14.04 gstreamer environment 
