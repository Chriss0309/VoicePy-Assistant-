import os
import tempfile
import playsound
import speech_recognition as sr
from gtts import gTTS

def speak(text, lang="en"):
    try:
        # Create a temporary file
        temp = tempfile.NamedTemporaryFile(delete=False, suffix='.mp3')
        temp.close()  # Close the file so it can be reopened by gTTS

        # Generate TTS and save to temporary file
        tts = gTTS(text=text, lang=lang)
        tts.save(temp.name)

        # Play the sound
        playsound.playsound(temp.name)

        # Remove the temporary file
        os.remove(temp.name)

    except Exception as e:
        print(f"An error occurred: {e}")

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        try:
            return r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

speak("Hello, how are you?", lang="en")
print(get_audio())





