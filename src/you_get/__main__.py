#!/usr/bin/env python

import os

__script_name__ = 'you-get'

__help__ = """Usage: {} [OPTION]... [URL]...
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

    from .common import script_main
    from .extractor import any_download, any_download_playlist
    script_main('you-get', any_download, any_download_playlist)

if __name__ == "__main__":
    main()
