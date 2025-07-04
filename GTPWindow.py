"""
Guide to Pronunciation Window for 'Thai for Beginners'
Filename: GTPWindow.py
"""
"""
So, what we did was first define a scroll widget and a separate widget to put
inside the scroll widget.  We then make subwidgets that go inside widget that then
goes inside the scroll widget.  

	This is the hierarchy:
	subsub-widgets < subwidgets < scroll widget < widget (main)

This allows us to then put what ever widgets we want inside the scroll widget.
We can even setup layouts and spaceings of subwidgets inside widgets to create the 
desired space/functionality
"""

###############################################################
#################################################################
# import needed libraries, classes, functions
###############################################################
###############################################################

import os, sys, random, MainWindow 
from random import choice

from PyQt5.QtWidgets import (
	QMainWindow, QApplication, QWidget, QLabel, QMessageBox, QHBoxLayout, QCheckBox,
	QPushButton, QVBoxLayout, QScrollArea, QSlider
)
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import Qt, QSize, QUrl
from PyQt5.Qt import (
	QPixmap, QFont, QCloseEvent, QPalette
)
from PyQt5 import QtCore, uic, QtGui
