from listen.listen import Listen
from replybrain.replybrain import ReplyBrain
from speak.speak import speak

def main():
    while True:
        global reply
        text = Listen().lower()
        reply = ReplyBrain(text)
        print(reply)
        speak(reply)


# def stop():

