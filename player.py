import sys
from PyQt5 import QtMultimedia, QtCore, QtWidgets
import time
import os

app = QtWidgets.QApplication(sys.argv)
filename = "audio/song.mp3"
fullpath = QtCore.QDir.current().absoluteFilePath(filename)
url = QtCore.QUrl.fromLocalFile(fullpath)
content = QtMultimedia.QMediaContent(url)
# playlist = QtMultimedia.QMediaPlaylist
player=QtMultimedia.QMediaPlayer()
player.setMedia(content)


def load(path):
    print(path)
    filename = 'audio/' + path
    fullpath = QtCore.QDir.current().absoluteFilePath(filename)
    url = QtCore.QUrl.fromLocalFile(fullpath)
    content = QtMultimedia.QMediaContent(url)
    player.setMedia(content)

def playpause():
    play_state = player.state()
    playing = QtMultimedia.QMediaPlayer.PlayingState
    if play_state == playing:
        player.pause()
    else:
        player.play()
