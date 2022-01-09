import matplotlib.pyplot as plt
from scipy.io import wavfile
import os
import librosa
import librosa.display
import numpy as np
from csv import writer
from tqdm import tqdm
import pandas as pd    
import numpy as np
import pickle
import math
from icecream import ic
import tensorflow as tf
import bz2
import pickle
import _pickle as cPickle

WAV_DIRECTORY = '/Users/martintin/Desktop/beat_generator/WAV'

MIDI_DIRECTORY = '/Users/martintin/Desktop/beat_generator/MIDI'
MIDI = os.listdir(MIDI_DIRECTORY)
def convert_spectrogram(file,n_fft):
	print(file)
	samples, sample_rate = librosa.load(file, sr=None)
	
# 15809.160997732426
# 15807
# 15810

	#sgram = np.abs(librosa.core.stft(samples,n_fft=n_fft,hop_length=441,win_length=441,center=False))

	
	sgram = np.abs(librosa.core.stft(samples,n_fft=n_fft,hop_length=441,center=True))


	mel_scale_sgram = librosa.feature.melspectrogram(S=sgram, sr=sample_rate,n_mels=80,n_fft=n_fft,hop_length=441)
	mel_sgram = librosa.amplitude_to_db(mel_scale_sgram, ref=np.min)	

	#librosa.display.specshow(mel_scale_sgram)
	#librosa.display.specshow(mel_sgram, sr=sample_rate, x_axis='time', y_axis='mel')
	#plt.colorbar(format='%+2.0f dB')
	#plt.plot()
	#plt.show()
	return mel_sgram


MIDI = MIDI[:300]

if __name__ == '__main__':
	arr_23ms = []
	arr_46ms = []
	arr_93ms = []
	for file in tqdm(MIDI):
		wavfile = os.path.join(WAV_DIRECTORY,(file[:-4]+".wav"))
		mel_sgram_23ms = convert_spectrogram(wavfile,1014)
	
		mel_sgram_46ms = convert_spectrogram(wavfile,2029)

		mel_sgram_93ms = convert_spectrogram(wavfile,4101)

		arr_23ms.append(mel_sgram_23ms)
		arr_46ms.append(mel_sgram_46ms)
		arr_93ms.append(mel_sgram_93ms)

		

	# 1014,2029,4101
	#f 23 ms, 46 ms and 93 ms
	PICKLE_DIRECTORY = '/Users/martintin/Desktop/beat_generator/processed_data'

	with bz2.BZ2File(os.path.join(PICKLE_DIRECTORY,"sgram1(23).pbz2"),"w") as f:
		cPickle.dump(arr_23ms,f)
	with bz2.BZ2File(os.path.join(PICKLE_DIRECTORY,"sgram1(46).pbz2"),"w") as f:
		cPickle.dump(arr_46ms,f)
	with bz2.BZ2File(os.path.join(PICKLE_DIRECTORY,"sgram1(93).pbz2"),"w") as f:
		cPickle.dump(arr_93ms,f)