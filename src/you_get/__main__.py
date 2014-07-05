#!/usr/bin/env python

import getopt
import os
import platform
import sys
from you_get.util import log
from you_get.util import git

__script_name__ = 'you-get'

__options__ = [
    'help',
    'version',
    'gui',
    'force',
    'playlists',
]
__short_options__ = 'hVgfl'

__help__ = """Usage: {} [OPTION]... [URL]...
TODO
""".format(__script_name__)

from .version import __version__

def main(**kwargs):
    """Main entry point."""

    # Get (branch, commit) if running from a git repo.
    try:
        __commit__ = git.get_head(kwargs['repo_path'])
    except:
        __commit__ = None

    # Unrecognized option.
    try:
        opts, args = getopt.getopt(sys.argv[1:], __short_options__, __options__)
    except getopt.GetoptError as e:
        log.wtf("""
    [FATAL] {}.
    Try 'you-get --help' for more options.""".format(e))

    # Parse options.
    conf = {}
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            # Display help.
            print(__help__)

        elif opt in ('-V', '--version'):
            # Display version.
            print("version:  {}".format(__version__))
            if __commit__ is not None:
                print("""branch:   {}\ncommit:   {}""".format(*__commit__))
            else:
                print("""branch:   {}\ncommit:   {}""".format("(UNKNOWN)", "(UNKNOWN)"))

            print("platform: {}".format(platform.platform()))
            print("python:   {}".format(sys.version))

        elif opt in ('-g', '--gui'):
            # Run using GUI.
            conf['gui'] = True

        elif opt in ('-f', '--force'):
            # Force download.
            conf['force'] = True

        elif opt in ('-l', '--playlist', '--playlists'):
            # Download playlist whenever possible.
            conf['playlist'] = True

    #if not args:
    #    from .gui import gui_main
    #    gui_main(**conf)

    #from .common import script_main
    #from .extractor import any_download, any_download_playlist
    #script_main('you-get', any_download, any_download_playlist)

if __name__ == "__main__":
    main()
