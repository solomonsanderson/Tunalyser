from pygame import mixer
import tkinter as tk
import librosa
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from librosa import display
from scipy.ndimage.measurements import label
import time 

mixer.init()

# audio_location = mixer.music.load("audio/song.mp3")
# mixer.music.play()
# 'C:\Users\Solom\OneDrive - University of Birmingham\Desktop\Python\Projects\tunalyser\audio\song.mp3'
data, sr = librosa.load(r'audio/Skr.mp3')
duration = librosa.get_duration(data, sr) # duration in seconds
print(sr)
print(len(data))
print(duration * sr)
print(f'len of data point {1/sr}')
# times = np.arange(0,22050 * duration)

fig, ax = plt.subplots(1,1, figsize=(12,9) )
# ax.set_xlim(xmin=0, xmax=25)
data_harm, data_perc = librosa.effects.hpss(data)
tempo, beats =librosa.beat.beat_track(data, sr)
beat_times = librosa.frames_to_time(beats, sr)
# ax.vlines(beat_times, ymax=1.2, ymin = -1.2, color='black', linestyle='--', alpha=0.8, label='beats')
# display.waveshow(data_harm, sr=sr, ax=ax, alpha=0.5, label='Harmonics')
# display.waveshow(data_perc, sr=sr, ax=ax, color='r', alpha=0.5, label='Percussives')
# ax.plot(data,times)

ax.set_xlabel('Timestamp (seconds)')
ax.set_ylabel('Amplitude')
ax.set_title('Waveform from a section of "Layer Cake" by Kano.')
ax.legend()

display.waveshow(data_harm[0:int(20/(1/sr))], sr=sr, ax=ax, alpha=0.5, label='Harmonics')
display.waveshow(data_perc[0:int(20/(1/sr))], sr=sr, ax=ax, color='r', alpha=0.5, label='Percussives')

plt.ion()
for i in range(0,len(data)):
    plt.clf()
    display.waveshow(data_harm[0+i:int(20+i)], sr=sr, ax=ax, alpha=0.5, label='Harmonics')
    display.waveshow(data_perc[0+i:int(20+i)], sr=sr, ax=ax, color='r', alpha=0.5, label='Percussives')
    time.delay(20)

interval = 20
frames = duration / ( interval / 1000)
x = np.linspace(0,duration, int(frames))

plt.show()

# for i in x:
#     ax.set_xlim(0 + i, 20 + i)
#     time.sleep(interval/1000)
#     plt.draw()
#     print(i)



# def init():
#     ax.set_xlim(0,20)

# def animate(i):
#     ax.set_xlim(0 + i, 20 + i)
# anim = FuncAnimation(fig, animate, init_func=init, frames=frames, interval=interval, blit=True )
# plt.show()