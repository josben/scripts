#!/usr/bin/env python

# Este script lo hize para convertir los videos de los cursos de coursera.org
# a mp3 y como coursera ofrece las letras de los videos este escript tambien
# aniade las letras a los mp3

from subprocess import call
import os

fileNames = []
videosMp4 = open("videos.txt", "r")
for video in videosMp4:
    name = video[:-5]
    fileNames.append(name)

videosMp4.close()

for name in fileNames:
    #call(["ffmpeg", "-i", "\"" + name + ".mp4\" -q:a 0 -map a \"" + name + ".mp3\""])
    os.system("ffmpeg -i \"" + name + ".mp4\" -q:a 0 -map a \"" + name + ".mp3\"")

for name in fileNames:
    lyrics = ''
    lines = open(name+'.txt', 'r')
    for line in lines:
        lyrics += line
    if name.find('Module 2 Overview') < 0:
        x = name.find(':')
        y = name.find('(')
        title = name[x+2:y-1]
        call(["eyeD3", "--lyrics=eng:" + title + ":"+ lyrics, name + ".mp3"])
    else:
        call(["eyeD3", "--lyrics=eng:Overview:" + lyrics, name + ".mp3"])

