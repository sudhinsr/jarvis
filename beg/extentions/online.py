import re
import random
WORDS = ["ARE","YOU","THERE"]


def handle(mic):
	messages = ["Yes Bose      How may assist you",
	"Yes I am Alive      tell me some thing Bose"]

	message = random.choice(messages)

	mic.say(message)



def isValid(text):
	return (bool(re.search(r'\bare you there\b', text, re.IGNORECASE)) or bool(re.search(r'\bonline\b', text, re.IGNORECASE)))
