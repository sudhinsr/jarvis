import sys,os
import pyaudio
import wave
import time

from os import environ, path
 
def decodeSpeech(wavfile):
 
    
    from pocketsphinx.pocketsphinx import *
    from sphinxbase.sphinxbase import *
    modeldir = '/home/sudhin/pocketsphinx-5prealpha/model'
    config = Decoder.default_config()
    config.set_string('-hmm', path.join(modeldir, 'en-us/en-us'))
    config.set_string('-lm', path.join(modeldir, 'en-us/en-us.lm.bin'))
    config.set_string('-dict', path.join(modeldir, 'en-us/cmudict-en-us.dict'))
    decoder = Decoder(config)

    #print ("Pronunciation for word 'hello' is ", decoder.lookup_word("switch"))
    time.sleep(5)
    decoder.start_utt()
    stream = open(wavfile, 'rb')
    while True:
      buf = stream.read(1024)
      if buf:
        decoder.process_raw(buf, False, False)
      else:
        break
    decoder.end_utt()
    
    hypothesis = decoder.hyp()
    #print ('Best hypothesis: ', hypothesis.hypstr, " model score: ", hypothesis.best_score, " confidence: ", hypothesis.prob)
    if hasattr ( hypothesis , 'hypstr' ) :
    	result = hypothesis.hypstr
    else :
    	result = "0"
    # print ('Best hypothesis segments: ', [seg.word for seg in decoder.seg()])
    # Access N best decodings.
    #print ('Best 10 hypothesis: ')
    #for best, i in zip(decoder.nbest(), range(10)):
    #print (best.hypstr, best.score)
    print result
    return result
 
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
RECORD_SECONDS = 3

while 1:
    fn = "test.wav"
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    print("* recording")
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("* done recording")
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(fn, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    wavfile = fn
    recognised = decodeSpeech(wavfile)
    print recognised
    cm = 'espeak "'+recognised+'"'
    os.system(cm)
    os.remove('test.wav')