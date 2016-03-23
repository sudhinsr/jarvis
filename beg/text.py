from stt import STT
from tts import TTS
from mic import Mic
from selection import Selection

class Text(object):
	
	def __init__(self):
		
		self.stt_engine = STT()
		self.tts_engine = TTS()
		self.mic = Mic(self.tts_engine, self.stt_engine, self.stt_engine)
		self.selection = Selection(self.tts_engine) 

	def handle(self):

		while True:
			threshold, translate = self.mic.passiveListen("JARVIS")
			if not translate or not threshold:
				continue
			input = self.mic.activeListen(threshold)
			print input
			if input:
				string = self.selection.select(input);
			else :
				self.tts_engine.say("Pardon?")


app = Text()
app.handle()

