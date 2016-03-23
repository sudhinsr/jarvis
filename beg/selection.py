import os
import pkgutil
from tts import TTS
class Selection(object):
	def __init__(self,tts_engine):
		self.tts_engine = tts_engine
		self.extensions=self.loadExtensions()

	def loadExtensions(self):
		modules = []
		locations=os.path.join((os.path.abspath(__file__),"extentions"))
		for finder, name, ispkg in pkgutil.walk_packages(locations):
			try:
				loader = finder.find_module(name)
				mod = loader.load_module(name)
			except:
				print ""	
			else:
				if hasattr(mod,'WORDS'):
					modules.append(mod)	
				else:
					print "Warning"
		modules.sort(key=lambda mod: mod.PRIORITY if hasattr(mod, 'PRIORITY')
                     else 0, reverse=True)
		print modules
		return modules

	def select(self,texts):
		print "selecting"
		for module in self.extensions:
			for text in texts:
				print text
				if module.isValid(text):
					try:
						print module
						module.handle(self.tts_engine)
					except Exception:
						print "Sorry Some Error With Extension"
					else:
						return

"""if __name__ == '__main__':
	tts_engine = TTS()
	App=Selection(tts_engine)
	query=["Time"]
	App.select(query)
"""
	