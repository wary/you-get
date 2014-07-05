#!/usr/bin/env python

import sys

if sys.version_info[0] == 3:
    from .__main__ import *
    from .extractor import Extractor # required by console
    from .extractor import VideoExtractor # required by site/
    #from .version import *
    #from .common import *
    #from .cli_wrapper import *
    #from .extractor_ import *
    #from .site import *
