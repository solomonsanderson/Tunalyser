import sys
from PyQt5 import QtMultimedia, QtCore, QtWidgets
import time

app = QtWidgets.QApplication(sys.argv)
filename = "audio/song.mp3"
fullpath = QtCore.QDir.current().absoluteFilePath(filename)
url = QtCore.QUrl.fromLocalFile(fullpath)
content = QtMultimedia.QMediaContent(url)
player=QtMultimedia.QMediaPlayer()
player.setMedia(content)
player.play()
# time.sleep(5)
# print(player.position())
sys.exit(app.exec_())