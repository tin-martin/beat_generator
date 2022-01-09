import pygame
from pygame import mixer
import math
import time
import os
from tensorflow import keras
from keras.models import load_model
from spectrogram_conversion import convert_spectrogram
from onset_identification import identify_onsets
import datetime
import numpy as np
import bz2
import pickle
import _pickle as cPickle
#midfile = "/Users/martintin/Desktop/beat_generator/MIDI/Kataplik.mid"

#wavfile = os.path.join("/Users/martintin/Desktop/beat_generator/WAV/Kataplik.wav")
#onsets, frame_duration, sr,duration = identify_onsets(midfile)
#--------------------------------------------------------------------------------------------------------

model = load_model('/Users/martintin/Desktop/beat_generator/model.h5')

arr = []
applesauce=25

wavfile = '/Users/martintin/Desktop/beat_generator/WAV/you_dont_have_to_say_you_love_me_gr_kar.wav'
specgram,duration,sr = convert_spectrogram(wavfile)
frame_duration= duration/len(specgram)

for y in range(applesauce - len(specgram[0])%applesauce):
    for a in range(24):
        specgram[a].append(0)
for x in range(int(len(specgram[0])/applesauce)): #AMMOUNT OF 250 GROUPS
    arr.append([[] for x in range(24)])
    for y in range(applesauce):
        for z in range(24):
            placeholder = specgram[z][x*applesauce+y]
            arr[x][z].append(placeholder)
arr = np.asarray(arr)

arr = arr.reshape(arr.shape[0],arr.shape[1],arr.shape[2],1)
onsets = model.predict(arr)

PICKLE_DIRECTORY = '/Users/martintin/Desktop/beat_generator/pickle_data'
with bz2.BZ2File(os.path.join(PICKLE_DIRECTORY,"onsetml1.pbz2"),"w") as f:
    cPickle.dump(onsets,f)
#-------------------------------------------------------------------------------------------------------




print(onsets)






















pygame.init()
mixer.init(frequency=sr)
mixer.music.load(wavfile)
mixer.music.set_volume(0.0)

WIDTH,LENGTH = 200,450
RADIUS = 10
DIAMETER = RADIUS*2
screen = pygame.display.set_mode([200,500])

running = True
leadingy = 450

NUM_FRAMES = int(LENGTH/DIAMETER)

#begin = time.time()
#for i in range(len(onsets)):
#    time.sleep(frame_duration-0.00055)
#    print(time.time()-begin)
#end = time.time()
#print(end-begin)

playmusic = False
print(duration)
while running:
    begin = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    pygame.draw.line(screen,(0,0,0), (0,450),(200,450), 2)
    for i in range(len(onsets)):
        x,y = WIDTH/2,leadingy-(i*DIAMETER) 
        if y > 450:
            pass
        else:
            if onsets[i] == 1: 	 		
                pygame.draw.circle(screen, (0,0,0), (x,y), RADIUS,20)
    leadingy += DIAMETER
    pygame.display.flip()
    if mixer.music.get_busy() == False:
        if playmusic == False:
            playmusic = True
            mixer.music.play(start=0)
            startofprogram = time.time()
        else:
            print(f'actual length: {time.time()-startofprogram}') 
            break
    end = time.time()
    mi = min([frame_duration,(end-begin)])
    ma = max([frame_duration,(end-begin)])
    try:
        time.sleep(ma-mi-0.00125)
    except:
        time.sleep(ma-mi)
    end = time.time()
    print(end-begin)


pygame.quit()
