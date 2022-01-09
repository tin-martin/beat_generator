
	
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
	wav_data = WAV_DIRECTORY+midi_data[44:-3]+"wav"
	midi_data = pretty_midi.PrettyMIDI(midi_data)
	samples, sample_rate = librosa.load(wav_data, sr=None)
	duration = midi_data.get_end_time()
	notes = []
	song_onsets = [0 for i in range(math.trunc(len(samples)/512)+1)]

	for instrument in midi_data.instruments:
		for note in instrument.notes:
	 		#freq = 440 * 2**((note.pitch-81)/12)
	 		notes.append(note.start)
	 	
	frame_number = math.trunc(len(samples)/512)+1
	frame_duration = duration/frame_number
#	print(frame_duration*25)

	notes = [float(note) for note in notes]

	for x in range(frame_number):
		frame_s = frame_duration*x
		frame_e = frame_s + frame_duration
		num = x 
		for i in range(len(notes)):
			if (notes[i] >= frame_s and notes[i] <= frame_e):
				song_onsets[num] = 1
	#plt.plot(song_onsets)
	#plt.show()
	return song_onsets, frame_duration, sample_rate,duration

#                           duration = samples*441000                      
#                            (samples*44100)/math.trunc(samples)/512)+1
#
if __name__ == "__main__":
	MIDI = [x for x in os.listdir(MIDI_DIRECTORY)]


	#MIDI.remove(".DS_Store")
	#arr = []
	#for file in tqdm(MIDI):
	#	arr.append([identify_onsets(os.path.join(MIDI_DIRECTORY,file))])

	arr = []
	length = 5           #250
	len_frames = 0
	counter = 0

	for i in tqdm(MIDI):
		file = os.path.join(MIDI_DIRECTORY, i)
		onsets,frame_duration,sr,duration = identify_onsets(file)
		for z in range(length - len(onsets)%length):
			onsets.append(0)

		for x in range(int(len(onsets)/length)): #groupingn of 25
			counter += 1
			arr.append(0)
			for y in range(length): # iterates over specific 2
				if onsets[x*length+y] == 1:
					arr[len_frames+x] = 1
					break
				     
		len_frames += int(len(onsets)/length)

		print(len(arr))


			
		


		#for length in range(math.trunc(len(onset)/100)):
		#	segment = onset[length*100:length*100+100]
		#	arr.append(segment)

	PICKLE_DIRECTORY = '/Users/martintin/Desktop/beat_generator/pickle_data'

	with bz2.BZ2File(os.path.join(PICKLE_DIRECTORY,"onsets(5).pbz2"),"w") as f:
		cPickle.dump(arr,f)
	
#arr = pd.DataFrame(arr)
#arr.to_csv("/Users/martintin/Desktop/beat_generator/onsets.csv",index=False,header=False)





