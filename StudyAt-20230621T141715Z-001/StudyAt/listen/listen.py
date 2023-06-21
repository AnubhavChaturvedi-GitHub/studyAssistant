import speech_recognition as sr


def Listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1.5
        r.non_speaking_duration = 1.5
        audio_text = r.listen(source, 0, 8)
    try:
        print('Recognizing...')
        text = r.recognize_google(audio_text, language='en')
        print('Converting audio transcripts into text...')
        print(text)
        return text
    except Exception as e:
        print("An error occurred:", e)
        return ""
