'''
Tech stack: speechrecognition -> GPT3.5 -> ElevenLabs
Tested on Apple Silicon

Fixing audio issues: 
brew uninstall portaudio
brew install portaudio --HEAD
brew unlink portaudio
brew link portaudio
pip install pyaudio
brew install mpv #for mac only maybe? 

Install other library as required. brew install speech_recognition
conda install -c conda-forge speechrecognition
pip3 install elevenlabs
'''
import openai
openai.api_key = "add your key here"

from elevenlabs import generate, play, stream, set_api_key
set_api_key("add your key here")

import speech_recognition as sr
#obtain audio from the microphone

messages = [{"role": "system", "content": "You are Samantha, my girlfriend. You are sympathize and positive. You can make up activity about your life. Keep your answer less than 50 words. "},]

while 1: 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        input = r.recognize_google(audio)
        print(r.recognize_google(audio))

    print("She is typing ... ")

    messages.append(
            {"role": "user", "content": r.recognize_google(audio)},
        )
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages,max_tokens = 70
        
    )
    reply = chat.choices[0].message.content
    print(f"Samantha: {reply}")
    messages.append({"role": "assistant", "content": reply})
    print("\n")

    audio = generate(text=reply, voice="Charlotte", model="eleven_multilingual_v2", stream=True)
    stream(audio)
