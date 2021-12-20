import sys
from PyQt5 import QtMultimedia, QtCore, QtWidgets
import time

app = QtWidgets.QApplication(sys.argv)
filename = "audio/song.mp3"
fullpath = QtCore.QDir.current().absoluteFilePath(filename)
url = QtCore.QUrl.fromLocalFile(fullpath)
content = QtMultimedia.QMediaContent(url)
# playlist = QtMultimedia.QMediaPlaylist
player=QtMultimedia.QMediaPlayer()
player.setMedia(content)

sys.exit(app.exec_())


def play():
    player.play()