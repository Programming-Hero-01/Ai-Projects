import googletrans
import speech_recognition as sr
import gtts
import playsound

recognizer = sr.Recognizer()
translator = googletrans.Translator()
input_lang = 'en'
output_lang = 'fr'

try:
    with sr.Microphone() as source:
        print("Speak now: ")
        voice = recognizer.listen(source)
        text = recognizer.recognize_google(voice, language=input_lang)
        print(text)
except:
    pass

translated = translator.translate(text, dest=output_lang)
print(translated.text)
converted_audio = gtts.gTTS(translated.text, lang=input_lang)
converted_audio.save('audio_saved.mp3')
playsound.playsound('audio_saved.mp3')
