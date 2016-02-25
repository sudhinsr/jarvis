import pocketsphinx as ps
from os import path

class STT(object):
	
	def __init__(self):

		modeldir = '/home/sudhin/pocketsphinx-5prealpha/model'
		config = ps.Decoder.default_config()
		config.set_string('-hmm', path.join(modeldir, 'en-us/en-us'))
		config.set_string('-lm', path.join(modeldir, 'en-us/en-us.lm.bin'))
		config.set_string('-dict', path.join(modeldir, 'en-us/cmudict-en-us.dict'))
		self._decoder = ps.Decoder(config)


	def translate(self, fp):

		#fp = open("test.wav",'rb')
		fp.seek(44)
		data = fp.read()
		self._decoder.start_utt()
		self._decoder.process_raw(data, False, True)
		self._decoder.end_utt()
		hypothesis = self._decoder.hyp()
		result = "0"
		if hasattr ( hypothesis , 'hypstr' ) :
			result = hypothesis.hypstr
		print result
		return result
