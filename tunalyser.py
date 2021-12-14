from pygame import mixer
import tkinter as tk
import librosa
import matplotlib.pyplot as plt
from librosa import display
from scipy.ndimage.measurements import label


mixer.init()

# audio_location = mixer.music.load("audio/song.mp3")
# mixer.music.play()
# 'C:\Users\Solom\OneDrive - University of Birmingham\Desktop\Python\Projects\tunalyser\audio\song.mp3'
data, sr = librosa.load(r'audio/song.mp3', duration=300)
fig, ax = plt.subplots(1,1, figsize=(12,9) )
ax.set_xlim(xmin=0, xmax=25)
data_harm, data_perc = librosa.effects.hpss(data)
tempo, beats =librosa.beat.beat_track(data, sr)
beat_times = librosa.frames_to_time(beats, sr)
ax.vlines(beat_times, ymax=1.2, ymin = -1.2, color='black', linestyle='--', alpha=0.8, label='beats')
display.waveshow(data_harm, sr=sr, ax=ax, alpha=0.5, label='Harmonics')
display.waveshow(data_perc, sr=sr, ax=ax, color='r', alpha=0.5, label='Percussives')
ax.legend()
plt.show()