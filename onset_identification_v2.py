import os
import pretty_midi
import librosa.display
import librosa
import math
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
import pandas as pd
import bz2
import pickle
import _pickle as cPickle
import math
MIDI_DIRECTORY = '/Users/martintin/Desktop/beat_generator/MIDI'
WAV_DIRECTORY = '/Users/martintin/Desktop/beat_generator/WAV'

def identify_onsets(midi_data):
	ones = 0
	zeroes = 0
	wav_data = WAV_DIRECTORY+midi_data[44:-3]+"wav"
	midi_data = pretty_midi.PrettyMIDI(midi_data)
	samples, sample_rate = librosa.load(wav_data, sr=None)
	duration = midi_data.get_end_time()
	notes = []
	hop_length=sample_rate/100

	for instrument in midi_data.instruments:
		for note in instrument.notes:
	 		#freq = 440 * 2**((note.pitch-81)/12)
	 		notes.append(note.start)

	frame_number = math.trunc(len(samples)/hop_length)+1
	frame_duration = (1/(sample_rate))*hop_length

	song_onsets = [0 for i in range(frame_number)]

	for x in range(frame_number):
		frame_s = float((frame_duration*x)-(frame_duration/2))
		frame_e = float(frame_s + frame_duration)
		

		for i in range(len(notes)):
			if (notes[i] >= frame_s and notes[i] < frame_e):
				song_onsets[x] = 1
				ones += 1
				break
		if song_onsets[x] != 1:
			zeroes += 1
	
	return song_onsets, frame_duration, sample_rate,duration

if __name__ == "__main__":
	MIDI = [x for x in os.listdir(MIDI_DIRECTORY)]
	
	MIDI = MIDI[600:]
	arr = []

	for i in tqdm(MIDI):
		file = os.path.join(MIDI_DIRECTORY, i)
		onsets,frame_duration,sr,duration = identify_onsets(file)
		arr.append(onsets)

		
		print(len(arr[-1]),file)

	arr = np.array(arr)

	PICKLE_DIRECTORY = '/Users/martintin/Desktop/beat_generator/processed_data'

	with bz2.BZ2File(os.path.join(PICKLE_DIRECTORY,"onsets3.pbz2"),"w") as f:
		cPickle.dump(arr,f)



