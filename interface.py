from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlaylist
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
import sys 
import os 
import time
import numpy as np
import datetime 

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Tunalyser")
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setFixedSize(500, 300)
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        self._createMenu()
        self._createToolBar()
        self._createProgress()
        self._createButtons()
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
    
    def _createButtons(self):
        self.buttons = {}
        buttonsLayout = QGridLayout()
        buttons = {"Play/Pause":(0,1), "Next Track":(0,2), "Previous Track":(0,0) }

        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            # self.buttons[btnText].setFixedSize(80,80)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
        self.generalLayout.addLayout(buttonsLayout)

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
        
        print(state)
        return state

    def _createProgress(self):
        # pass
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30,40,200,25)
        self.generalLayout.addWidget(self.pbar)
        self.btn = QPushButton('Start', self)
        self.btn.clicked.connect(self.timer)
        
    def timer(self):
        duration = 180  # placeholder value 
        step = 90
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

    def _createListBox(self):
        self.lbox = QListWidget()
        file_names = os.listdir(r"C:\Users\Solom\OneDrive - University of Birmingham\Desktop\Python\Projects\tunalyser\audio")
        playlist = QMediaPlaylist
        
        for name in file_names: 
            self.lbox.addItem(name)
        #     playlist.addMedia(QMediaContent(QUrl.fromLocalFile(name)))
            
        
        
        self.generalLayout.addWidget(self.lbox)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


        


