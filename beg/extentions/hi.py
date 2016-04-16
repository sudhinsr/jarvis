import re
import random
WORDS = ["HI","HELLO"]


def handle(mic):
	messages = ["Jarvis here How Can I help you sir",
	"Hi Bose, Jervis here to help you"]

	message = random.choice(messages)

	mic.say(message)



def isValid(text):
	return (bool(re.search(r'\bhi\b', text, re.IGNORECASE)) or bool(re.search(r'\bhello\b', text, re.IGNORECASE)))
