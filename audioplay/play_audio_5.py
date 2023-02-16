import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5 import QtCore, QtMultimedia


url = QtCore.QUrl.fromLocalFile("output_5.wav")
content = QtMultimedia.QMediaContent(url)
player = QtMultimedia.QMediaPlayer()
player.setMedia(content)
player.setVolume(int(100.0))
player.play()
