#!/usr/bin/env python

import getopt
import os
import platform
import sys
from you_get.util import log

__script_name__ = 'you-get'

__options__ = [
    'help',
    'version',
]
__short_options__ = 'hV'

__help__ = """Usage: {} [OPTION]... [URL]...
TODO
""".format(__script_name__)

from .version import __version__

def get_head(repo_path):
    ref = open(os.path.join(repo_path, '.git', 'HEAD'), 'r').read().strip()[5:].split('/')
    return ref[-1], open(os.path.join(repo_path, '.git', *ref), 'r').read().strip()[:7]

def main(**kwargs):
    try:
        __commit__ = get_head(kwargs['repo_path'])
    except:
        __commit__ = None

    try:
        opts, args = getopt.getopt(sys.argv[1:], __short_options__, __options__)
    except getopt.GetoptError as e:
        log.wtf("""
    [FATAL] {}.
    Try 'you-get --help' for more options.""".format(e))

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print(__help__)

        elif opt in ('-V', '--version'):
            print("version:  {}".format(__version__))
            if __commit__ is not None:
                print("""branch:   {}\ncommit:   {}""".format(*__commit__))
            else:
                print("""branch:   {}\ncommit:   {}""".format("(UNKNOWN)", "(UNKNOWN)"))

            print("platform: {}".format(platform.platform()))
            print("python:   {}".format(sys.version))

    #from .gui import gui_main
    #gui_main()

    #from .common import script_main
    #from .extractor import any_download, any_download_playlist
    #script_main('you-get', any_download, any_download_playlist)

if __name__ == "__main__":
    main()
