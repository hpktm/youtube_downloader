#!/usr/bin/env python

import pytube

def down(url):
    yt = pytube.YouTube(url)
    stram=yt.streams.first()
    stram.download()


url: str=input("Enter Url ")
down(url)
