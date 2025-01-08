#   microphonerecognition for word zero
#
#   https://youtu.be/SqVeAxrPAB0?t=757
#   How to Use Vosk for Speech Recognition in Python
#   Código Logo
#
#   C:\va\vosk-git\voicemodel\en-us-small
#   .\voicemodel\en-us-small
#
from vosk import Model, KaldiRecognizer
import pyaudio

# Recognize speech from the microphone
# model		= Model(r'C:\va\vosk-git\voicemodel\en-us-small') # read the model # full path
model		= Model(r'.\voicemodel\en-us-small') # read the model # relative pat
recognizer 	= KaldiRecognizer(model, 16000, '[ "zero", "[unk]" ]')

# Start listening to the microphone
cap = pyaudio.PyAudio()
stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

while True:
    data = stream.read(4096)
    if len(data) == 0:
        break
    
    if recognizer.AcceptWaveform(data):
        print(recognizer.Result())

# You can also specify the possible word list
#rec = KaldiRecognizer(model, wf.getframerate(), '[ "keyphrase", "[unk]" ]')