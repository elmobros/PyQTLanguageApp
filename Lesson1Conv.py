"""
Class file for Lesson 1 Conversation for 'Thai for Beginners'
Filename: Lesson1Conv.py

This is to be imported into Lesson 1 

This file is to have the needed vocabulary text and accompanying sound files for the
user to click to listen to pronunciation

"""
"""
Scroll widget.  

	This is the hierarchy:
	subsub-widgets < subwidgets < scroll widget < widget (main)
"""

###############################################################
#################################################################
# import needed libraries, classes, functions
###############################################################
###############################################################


import os, sys, random
from random import choice

from PyQt5.QtWidgets import (
	QMainWindow, QApplication, QWidget, QLabel, QMessageBox, QHBoxLayout, QCheckBox,
	QPushButton, QVBoxLayout, QScrollArea, QSlider, QGridLayout
)
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import Qt, QSize, QUrl
from PyQt5.Qt import (
	QPixmap, QFont, QCloseEvent, QPalette
)
from PyQt5 import QtCore, uic, QtGui

#############################################################
#############################################################
# Media content Files Text/Audio
#############################################################
#############################################################

# read in the jpg files for this window
texts = os.listdir('textTOCFiles/')

# attach 'textFiles/' to filenames

for i in range(len(texts)):
	texts[i] = 'textTOCFiles/' + texts[i] 

print(texts)

###########################################################
#    image png files
##############################################################
# read in the png files of the alphabet
pics = os.listdir('AlphaPng/')

# attach 'AlphaPng/' file names
for q in range(len(pics)):
	pics[q] = 'AlphaPng/' + pics[q]

#############################################################
#############################################################
#  Lesson 1 Conversation Class
#############################################################
#############################################################

class Lesson1Conv(QWidget):
	def __init__(self):

		super().__init__()

#############################################################
#  Setup the scroll area, subwidget and scroll properties
#############################################################		
	
		self.widgetLayout = QVBoxLayout()

		# create the scroll area 
		self.scroll = QScrollArea()

		# set scroll properties
		self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
		self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		self.scroll.setWidgetResizable(False)

		# create subwidget for inside scroll
		self.subwidget = QWidget()

		# set the layout for the subwidget
		self.subwidgetLayout = QVBoxLayout()

#############################################################
#  Create the subsubwidgets, layout
#############################################################

		# create a label for Convo 1
		self.text = "Conversation 1"
		
		self.labelConv = QLabel()
		self.labelConv.setText(self.text)
		self.labelConv.resize(100, 100)
		self.font = QtGui.QFont("Times", 18,QFont.Bold)
		self.font.setUnderline(True)
		self.font.setStyleHint(QtGui.QFont.TypeWriter)
		self.labelConv.setFont(self.font)
		
		# conversation 1
		self.conv1 = QLabel()
		picture1 = QPixmap(pics[0])
		picture1 = picture1.scaled(700,700,Qt.KeepAspectRatio)
		self.conv1.setPixmap(picture1)
		self.conv1.setAlignment(Qt.AlignCenter)

		self.subwidgetLayout.addWidget(self.labelConv)
		self.subwidgetLayout.addWidget(self.conv1)

		# create a label for Convo 2
		self.text = "Conversation 2"
		
		self.labelConv2 = QLabel()
		self.labelConv2.setText(self.text)
		self.labelConv2.resize(100, 100)
		self.font2 = QtGui.QFont("Times", 18,QFont.Bold)
		self.font2.setUnderline(True)
		self.font2.setStyleHint(QtGui.QFont.TypeWriter)
		self.labelConv2.setFont(self.font)
		
		# conversation 2
		self.conv2 = QLabel()
		picture2 = QPixmap(pics[1])
		picture2 = picture2.scaled(700,700,Qt.KeepAspectRatio)
		self.conv2.setPixmap(picture2)
		self.conv2.setAlignment(Qt.AlignCenter)

		
		self.subwidgetLayout.addWidget(self.labelConv2)
		self.subwidgetLayout.addWidget(self.conv2)


#############################################################
#  signals, slots
#############################################################

	# 	self.button.clicked.connect(self.button_click)

	# def button_click(self, checked):
	# 	print("OK")

#############################################################
#  set the subwidget layout, add it to scroll area
#############################################################

		# set alignment for the subwidget layout
		self.subwidgetLayout.setAlignment(Qt.AlignVCenter)

		# set the layout for the subwidget
		self.subwidget.setLayout(self.subwidgetLayout)

		# now 'add' the subwidget to the scroll area wdiget
		self.scroll.setWidget(self.subwidget)

#############################################################
#  add scroll area to widget layout, and set Widget layout
#############################################################
		
		# now add the QScrollArea widget to the container QWidget layout
		self.widgetLayout.addWidget(self.scroll)

		# set the container widget layout
		self.setLayout(self.widgetLayout)