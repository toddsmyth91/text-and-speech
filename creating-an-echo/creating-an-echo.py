# takes input from microphone and then puts it into an output file "output.wav"
import pyaudio
import wave
import pyttsx3
import speech_recognition as sr 

CHUNK = 1024
FORMAT = pyaudio.paInt16
#CHANNELS = 2
CHANNELS = 1 # mac only accepts single channel
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK,
		input_device_index=2) #on mac the 3rd input is mac microphone so index #2

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

# take the output.wav file and convert it to text
filename = "output.wav"

# initialise the recogniser
r = sr.Recognizer()

# create a variable to store the text returned from audio
speechToText = "" 

# open the file
with sr.AudioFile(filename) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognise (convert from speech to text)
        speechToText = r.recognize_google(audio_data)
        print(speechToText)

# make the computer speak the text that has been generated
engine = pyttsx3.init()

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
#print (rate)                        #printing current voice rate
engine.setProperty('rate', 175)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
#print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
#engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

engine.say(speechToText)
engine.runAndWait()
engine.stop()
