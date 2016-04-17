# -*- coding: utf-8-*-
import tempfile
import subprocess
import random
import os
import re
import sys
import pygame as pg


WORDS = ["MUSIC"]


def handle(mic):
	files = os.listdir("music")
	play("music/"+random.choice(files))

def play(TRACKS):
	TRACK_END = pg.USEREVENT+1
	 #Three sound effects I have
	track = 0


	pg.init()
	pg.display.set_mode((500,500))
	pg.mixer.music.set_endevent(TRACK_END)
	pg.mixer.music.load(TRACKS)
	pg.mixer.music.play()

	while 1:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()
			elif event.type == TRACK_END:
				track = (track+1)%len(TRACKS)
				pg.mixer.music.load(TRACKS[track])
				pg.mixer.music.play()

def isValid(text):
    
	return (bool(re.search(r'\bmusic\b', text, re.IGNORECASE)) or bool(re.search(r'\bplay music\b', text, re.IGNORECASE))) 
