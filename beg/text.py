from stt import STT
from tts import TTS
from mic import Mic
from control import Control

class Text(object):
	
	def __init__(self):
		
		self.stt_engine = STT()
		self.tts_engine = TTS()
		self.mic = Mic(self.tts_engine, self.stt_engine, self.stt_engine)
		self.control = Control() 

	def handle(self):

		while True:
			threshold, translate = self.mic.passiveListen("hello")
			if not translate or not threshold:
				continue
			input = self.mic.activeListen(threshold)
			print input
			if input:
				string = self.control.get(input);
			else :
				self.tts_engine.say("Pardon?")


app = Text()
app.handle()

