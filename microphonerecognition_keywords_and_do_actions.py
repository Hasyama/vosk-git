#   microphonerecognition for words "zero", "one", "two" and do some action currently print 'You said: x'
#
#   https://youtu.be/SqVeAxrPAB0?t=757
#   How to Use Vosk for Speech Recognition in Python
#   Código Logo
#
#   Paths to voicemodels
#   C:\va\vosk-git\voicemodel\en-us-small
#   .\voicemodel\en-us-small
#
#   Target words
#   "zero", "one", "two",
#
import json
from vosk import Model, KaldiRecognizer
import pyaudio

# Recognize speech from the microphone
# model		= Model(r'C:\va\vosk-git\voicemodel\en-us-small') # read the model # full path
model		= Model(r'.\voicemodel\en-us-small') # read the model # relative pat
keywords    = '[ "zero", "one", "two", "[unk]" ]'
recognizer 	= KaldiRecognizer(model, 16000, keywords)

# Start listening to the microphone
# That's pyaudio
# open a stream on the desired device with the desired audio parameters
capture = pyaudio.PyAudio()
stream = capture.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

while True:
    datajson = stream.read(4096)
    
    if len(datajson) == 0:
        break
    
    if recognizer.AcceptWaveform(datajson):
        #1# print(recognizer.Result()) # json output
        # removes json
        data = json.loads(recognizer.Result())
        word = data['text']
        # do something if word is x
        if word=='[unk]':
         print('word not listed')
        #
        if word=='zero':
         print('You said: ' + word)
        #
        if word=='one':
         print('You said: ' + word)
        #
        if word=='two':
         print('You said: ' + word)
        #

# You can also specify the possible word list
#rec = KaldiRecognizer(model, wf.getframerate(), '[ "keyphrase", "[unk]" ]')
