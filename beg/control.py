import os
import datetime
from tts import TTS

class Control(object):
	
	def __init__(self):
		self.stt_engine=TTS();

	def get(self, input):
		if(input == "hi"):
			self.stt_engine.say("Hello")

			time = datetime.datetime.now().time()
			self.stt_engine.say("It is %s right now." % time )

		