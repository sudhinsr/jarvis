import os
import tempfile
import subprocess

class TTS(object):
	
    def __init__(self, voice='default+m3', pitch_adjustment=40, words_per_minute=160) :
        
        self.voice = voice
        self.pitch_adjustment = pitch_adjustment
        self.words_per_minute = words_per_minute

    def play(self, filename):

        cmd = ['aplay', '-D', 'plughw:1,0', str(filename)]
        with tempfile.TemporaryFile() as f:
            subprocess.call(cmd, stdout=f, stderr=f)

    def say(self, phrase):
    	with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as f:
			fname = f.name
        cmd = ['espeak', '-v', self.voice,
                         '-p', self.pitch_adjustment,
                         '-s', self.words_per_minute,
                         '-w', fname,
                         phrase ]
        cmd = [str(x) for x in cmd]
        with tempfile.TemporaryFile() as f:
            subprocess.call(cmd, stdout=f, stderr=f)
        self.play(fname)
        os.remove(fname)
        
