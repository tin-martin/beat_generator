from icecream import ic  
import os
import time
import fluidsynth
from midi2audio import FluidSynth

fs = FluidSynth()

MIDI = os.listdir('/Users/martintin/Desktop/beat_generator/MIDI')

for i in MIDI:
	midi_directory = '/Users/martintin/Desktop/beat_generator/MIDI/'
	mp3_directory = '/Users/martintin/Desktop/beat_generator/MP3'
	input = os.path.join(midi_directory, i)
	output = os.path.join(mp3_directory, f"{i[:-4]}.mp3")
	fs.midi_to_audio(input, output)
	print(len(os.listdir('/Users/martintin/Desktop/beat_generator/MP3')))
