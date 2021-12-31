'''
Code to create an interface for an mp3 player including basic media controls,
 album cover display, song selection and other functions
'''


from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlaylist
from PyQt5 import QtCore, QtMultimedia
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
import sys 
import os 
import time
import numpy as np
import datetime 
from PyQt5.QtCore import Qt

# import stagger
from PIL import Image
import io

from player import playpause, load, duration
#

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.setWindowTitle("Tunalyser")
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setFixedSize(500, 500)
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        self._createMenu()
        self._createToolBar()
        self._createSongInfo()
        # self._createProgress()
        self._createSlider()
        self._addButtons()
        # self._createButtons()
        self._createRadio()
        self._createListBox()
        # self._createStatusBar()

    def _createMenu(self):
        self.menu = self.menuBar().addMenu("&Menu")
        self.menu.addAction("&Exit", self.close)
        
    def _createToolBar(self):
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction('Exit', self.close)
    
    def _createSongInfo(self):
        self.songTitle = QLabel()
        self.songTitle.setText("Please Load a Song")
       
        self.coverLabel = QLabel(self)
        self.pixmap = QtGui.QPixmap('cover.png')
        self.coverLabel.setPixmap(self.pixmap)
        
        layout = QGridLayout()
        layout.addWidget(self.coverLabel, 0, 0)
        layout.addWidget(self.songTitle, 0, 1)
        self.generalLayout.addLayout(layout)
        # self.generalLayout.addWidget(self.songTitle)

    def _addButtons(self):
        buttonsLayout = QGridLayout()
        self.playbtn = QPushButton('Play/Pause')
        buttonsLayout.addWidget(self.playbtn, 0, 1)
        self.generalLayout.addLayout(buttonsLayout)
        # self.playbtn.clicked.connect(self.timer)
        self.playbtn.clicked.connect(playpause)
        # self.playbtn.clicked.connect(play())
        self.prevbtn = QPushButton('Previous')
        buttonsLayout.addWidget(self.prevbtn, 0, 0)
        
        self.nextbtn = QPushButton('Next')
        buttonsLayout.addWidget(self.nextbtn, 0 , 2)


    def _createRadio(self):
        self.b1 = QRadioButton('Sequential')
        self.b1.setChecked(True)
        self.b2 = QRadioButton('Shuffle')
        self.b3 = QRadioButton('Loop')
        radioLayout = QGridLayout()
        radioLayout.addWidget(self.b1, 1, 0)
        radioLayout.addWidget(self.b2, 1, 2)
        radioLayout.addWidget(self.b3, 1, 3)
        self.b1.toggled.connect(self.radioState)
        self.b2.toggled.connect(self.radioState)
        self.b3.toggled.connect(self.radioState)
        self.generalLayout.addLayout(radioLayout)
    
    def radioState(self):
        # dont think this is gonna work 
    
        button = self.sender()
        state = button.isChecked()
        print(self.b2)
        if self.b1.isChecked == True:
            QMediaPlaylist.PlaybackMode.Sequential

        elif self.b2.isChecked == True:
            QMediaPlaylist.PlaybackMode.Random

        elif self.b3.isChecked == True:
            QMediaPlaylist.PlaybackMode.Loop
        
        # print(state)
        return state

    # def _createProgress(self):
    #     # pass
    #     self.pbar = QProgressBar(self)
    #     self.pbar.setGeometry(30,40,200,25)
    #     self.generalLayout.addWidget(self.pbar)
    #     self.timer
        
        
    def timer(self):
        duration = 180  # placeholder value 
        step = 1
        indicies = np.arange(0, duration + 1, step)
        
        # self.pbar.setMinimum(indicies[0])
        # self.pbar.setMaximum(indicies[-1])
        self.pbar.setFormat(f'00:00')
        for t in indicies:
            time.sleep(step)
            self.pbar.setValue(t)
            self.pbar.text()
            self.pbar.setFormat(f'{str(datetime.timedelta(seconds=step))[2:]}')
        self.pbar.reset()
        self.generalLayout.addWidget(self.pbar)

    def _createSlider(self):
        layout = QGridLayout()
        self.slider = QSlider(Qt.Horizontal)
        # self.slider.setRange(0, 0)
        layout.addWidget(self.slider, 0, 1)

        # Labelling slider
        self.currentLabel = QLabel()
        self.currentLabel.setText('t')
        self.durationLabel = QLabel()
        # self.durationLabel.setText(duration())
        layout.addWidget(self.currentLabel, 0, 0)
        layout.addWidget(self.durationLabel, 0, 2)
        self.generalLayout.addLayout(layout)

    # def getCover(self, item):
    #     path = 'audio/' + item
    #     mp3 = stagger.read_tag(path)
    #     by_data = mp3[stagger.id3.APIC][0].data
    #     im = io.BytesIO(by_data)
    #     self.cover.setPixmap(QtGui.QPixmap(im))
        


    def _createListBox(self):
        self.lbox = QListWidget()
        file_names = os.listdir(r"C:\Users\Solom\OneDrive - University of Birmingham\Desktop\Python\Projects\tunalyser\audio")
        playlist = QMediaPlaylist
        
        for name in file_names: 
            self.lbox.addItem(name)
        #     playlist.addMedia(QMediaContent(QUrl.fromLocalFile(name)))
        self.lbox.clicked.connect(self.lboxClicked)
        self.generalLayout.addWidget(self.lbox)

    def lboxClicked(self, qmodelindex):
        # make so when clicked, song is played
        item = self.lbox.currentItem().text()
        self.songTitle.setText(item)
        load(item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())




