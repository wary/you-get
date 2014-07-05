#!/usr/bin/env python

from you_get import Extractor

def console_main(*args, **conf):
    for arg in args:
        # url preprocessing, redirection...
        url = arg
        #extraction = Extractor(url, **conf)
        from you_get import site
        site.youku.extractor().download_by_url(url, **conf)
