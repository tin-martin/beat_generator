from icecream import ic  
import os,os.path
import time
import fluidsynth
from midi2audio import FluidSynth
def convert_audio():

	fs = FluidSynth()

	MIDI = os.listdir('/Users/martintin/Desktop/beat_generator/MIDI')

	for i in MIDI:
		midi_directory = '/Users/martintin/Desktop/beat_generator/MIDI/'
		wav_directory = '/Users/martintin/Desktop/beat_generator/WAV'
		input = os.path.join(midi_directory, i)
		output = os.path.join(wav_directory, f"{i[:-4]}.wav")
		fs.midi_to_audio(input, output)
		print(MIDI)



MIDI = os.listdir('/Users/martintin/Desktop/beat_generator/MIDI')
WAV = os.listdir('/Users/martintin/Desktop/beat_generator/WAV')


mids = ['humop1-2.mid', "Willie-Fugal's-Blues.mid", 'flash3.mid', 'Bagatella op33 n3.mid', 'Cisneros_Zulay.mid', 'rac_op33_6_format0.mid', "I'mWaitingForTheDay.mid", 'Markus Schulz - The New World.mid']
fs = FluidSynth()

MIDI = os.listdir('/Users/martintin/Desktop/beat_generator/MIDI')
for i in mids:
	midi_directory = '/Users/martintin/Desktop/beat_generator/MIDI/'
	wav_directory = '/Users/martintin/Desktop/beat_generator/WAV'
	input = os.path.join(midi_directory, i)
	output = os.path.join(wav_directory, f"{i[:-4]}.wav")
	fs.midi_to_audio(input, output)







	#ic(len(os.listdir('/Users/martintin/Desktop/beat_generator/WAV')))
	#ic(len(os.listdir('/Users/martintin/Desktop/beat_generator/MIDI')))
#I used my google email to submit class 1 homework. Can I switch to my other classkick account for future homework submissions?