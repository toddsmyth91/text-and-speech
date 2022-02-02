import speech_recognition as sr

filename = "16-122828-0002.wav"

# initialise the recogniser
r = sr.Recognizer()

# open the file
with sr.AudioFile(filename) as source:
	# listen for the data (load audio to memory)
	audio_data = r.record(source)
	# recognise (convert from speech to text)
	text = r.recognize_google(audio_data)
	print(text)
