#!/usr/bin/env python

import sys

if sys.version_info[0] == 3:
    from .__main__ import *
    #from .version import *
    #from .common import *
    #from .cli_wrapper import *
    #from .extractor_ import *
    #from .site import *
    from .extractor import Extractor
    from .extractor import VideoExtractor # required by site
