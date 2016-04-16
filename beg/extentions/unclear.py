from sys import maxint
import random

WORDS = []

PRIORITY = -(maxint + 1)


def handle(mic):

    messages = ["I'm sorry, could you repeat that?",
                "My apologies, could you try saying that again?",
                "Say that again?", "I beg your pardon?"]

    message = random.choice(messages)

    mic.say(message)


def isValid(text):
    return True