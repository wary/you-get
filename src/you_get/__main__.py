#!/usr/bin/env python

def main():
    from .common import script_main
    from .extractor import any_download, any_download_playlist
    script_main('you-get', any_download, any_download_playlist)

if __name__ == "__main__":
    main()
