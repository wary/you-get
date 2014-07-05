#!/usr/bin/env python

from .common import match1, download_urls

class Extractor():
    def __init__(self, *args):
        self.url = None
        self.title = None
        self.vid = None
        self.streams = {}
        self.streams_sorted = []

        if args:
            self.url = args[0]

class VideoExtractor():
    def __init__(self, *args):
        self.url = None
        self.title = None
        self.vid = None
        self.streams = {}
        self.streams_sorted = []

        if args:
            self.url = args[0]

    def download_by_url(self, url, **kwargs):
        self.url = url

        #global extractor_proxy
        #if extractor_proxy:
        #    set_proxy(parse_host(extractor_proxy))
        self.prepare(**kwargs)
        self.streams_sorted = [dict([('id', stream_type['id'])] + list(self.streams[stream_type['id']].items())) for stream_type in self.__class__.stream_types if stream_type['id'] in self.streams]
        self.extract(**kwargs)
        #if extractor_proxy:
        #    unset_proxy()

        self.download(**kwargs)

    def download_by_vid(self, vid, **kwargs):
        self.vid = vid

        #global extractor_proxy
        #if extractor_proxy:
        #    set_proxy(parse_host(extractor_proxy))
        self.prepare(**kwargs)
        self.streams_sorted = [dict([('id', stream_type['id'])] + list(self.streams[stream_type['id']].items())) for stream_type in self.__class__.stream_types if stream_type['id'] in self.streams]
        #self.extract(**kwargs)
        #if extractor_proxy:
        #    unset_proxy()

        self.download(**kwargs)

    def prepare(self, **kwargs):
        pass
        #raise NotImplementedError()

    def extract(self, **kwargs):
        pass
        #raise NotImplementedError()

    def p_stream(self, stream_id):
        stream = self.streams[stream_id]
        print("    - id:            \033[7m%s\033[0m" % stream_id)
        print("      container:     %s" % stream['container'])
        print("      video-profile: %s" % stream['video_profile'])
        if 'size' in stream:
            print("      size:          %s MiB (%s bytes)" % (round(stream['size'] / 1048576, 1), stream['size']))
        else:
            print("      size:          Unknown")
        print("    # download-with: \033[4myou-get --format=%s [URL]\033[0m" % stream_id)
        print()

    def p(self, stream_id=None):
        print("site:                %s" % self.__class__.name)
        print("title:               %s" % self.title)
        if stream_id:
            # Print the stream
            print("stream:")
            self.p_stream(stream_id)

        elif stream_id is None:
            # Print stream with best quality
            print("stream:              # Best quality")
            stream_id = self.streams_sorted[0]['id']
            self.p_stream(stream_id)

        elif stream_id == []:
            # Print all available streams
            print("streams:             # Available quality and codecs")
            for stream in self.streams_sorted:
                self.p_stream(stream['id'])

    def download(self, **kwargs):
        if 'info_only' in kwargs and kwargs['info_only']:
            if 'stream_id' in kwargs and kwargs['stream_id']:
                # Display the stream
                stream_id = kwargs['stream_id']
                self.p(stream_id)
            else:
                # Display all available streams
                self.p([])

        else:
            if 'stream_id' in kwargs and kwargs['stream_id']:
                # Download the stream
                stream_id = kwargs['stream_id']
            else:
                # Download stream with the best quality
                stream_id = self.streams_sorted[0]['id']

            self.p(None)

            urls = self.streams[stream_id]['src']
            if not urls:
                log.e('[Failed] Cannot extract video source.')
                log.e('This is most likely because the video has not been made available in your country.')
                log.e('You may try to use a proxy via \'-y\' for extracting stream data.')
                exit(1)
            #download_urls(urls, self.title, self.streams[stream_id]['container'], self.streams[stream_id]['size'], output_dir=kwargs['output_dir'], merge=kwargs['merge'])
            download_urls(urls, self.title, self.streams[stream_id]['container'], self.streams[stream_id]['size'])

        self.__init__()
