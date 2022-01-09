import pygame
from pygame import mixer
import math
import time
import os
from onset_identification import identify_onsets
import datetime
midfile = "/Users/martintin/Desktop/beat_generator/MIDI/jingle_bells_05_bb_gw.mid"

wavfile = os.path.join("/Users/martintin/Desktop/beat_generator/WAV/jingle_bells_05_bb_gw.wav")
onsets, frame_duration, sr,duration = identify_onsets(midfile)

pygame.init()
mixer.init(frequency=sr)
mixer.music.load(wavfile)
mixer.music.set_volume(0.5)

WIDTH,LENGTH = 200,450
RADIUS = 10
DIAMETER = RADIUS*2
screen = pygame.display.set_mode([200,500])

running = True
leadingy = 450

NUM_FRAMES = int(LENGTH/DIAMETER)

print(f'frameduration:{frame_duration}')
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
        time.sleep(ma-mi-0.003)
    except:
        time.sleep(ma-mi)


    end = time.time()
    print(end-begin)

pygame.quit()
