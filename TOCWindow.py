"""
Table of Contents Window for 'Thai for Beginners'
Filename: TOCWindow.py
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

#############################################################
#############################################################
#  TOC Text Files
#############################################################
#############################################################

# read in the jpg files for this window
texts = os.listdir('textTOCFiles/')

# attach 'textFiles/' to filenames

for i in range(len(texts)):
	texts[i] = 'textTOCFiles/' + texts[i] 


#############################################################
#############################################################
#  TOC Window
#############################################################
#############################################################

class TOCWindow(QMainWindow):
	def __init__(self):

		super().__init__()

#############################################################
#  TOC Window Properties
#############################################################
		## basic properties of the intro window
		
		# size and position
		self.setWindowTitle("Table of Contents")
		self.setGeometry(500,100,1200,2000)
		self.setFixedSize(1000,800)

		####### THIS MODAL POLICY NOT WORKING RIGHT NOW
		# # set up to make it modal (child into to parent main)
		# self.frame = QFrame()
		# self.frame.setWindowModality(QtCore.Qt.ApplicationModal)
		# # show the intro window
		# self.frame.show()	

		self.show()


#############################################################
#  additional widgets
#############################################################
		# exit to main button
		self.buttonExitIntro = QPushButton("Exit (แล้ว) to Main Menu")


#############################################################
#  setup scroll, subwidget and widget 
#############################################################
		
		# this is calling the scroll function
		self.initUI()


	# we define the scroll area function here
	def initUI(self):
		
		
		# create the container for the scroll area, goes inside Scroll
		self.subwidget=QWidget()
		# set the scroll area, goes inside Widget
		self.scroll = QScrollArea()
		# make the larger overall widget
		self.widget = QWidget()

		#set up the layout for subwidget
		self.subvbox = QVBoxLayout()

		# set up layout for widget
		self.vbox = QVBoxLayout()

		# add the introtext files
		for i in range(len(texts)):
			object = QLabel()
			object.setPixmap(QPixmap(texts[i]))
			self.subvbox.addWidget(object)
		
		# set layout for the container subwidget as vbox
		self.subwidget.setLayout(self.subvbox)

		# set scroll properties
		self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn) # V slider ON
		self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # H slider OFF
		self.scroll.setWidgetResizable(False)  # just making resizing unavailable

		# here, we 'add' widget with vbox filled in with labels
		self.scroll.setWidget(self.subwidget)  # to the scroll widget

#############################################################
#  add widgets to layout
#############################################################
		
		self.vbox.addWidget(self.scroll)
		self.vbox.addWidget(self.buttonExitIntro)

		# and set overall layout

		self.widget.setLayout(self.vbox)

		# # set the central widget as the scroll widget now
		self.setCentralWidget(self.widget)

#############################################################
#  signals for widgets
#############################################################	
		
		# signal for exit button
		self.buttonExitIntro.clicked.connect(self.back_to_mainTOC)

#############################################################
#  slots for signals
#############################################################

	def back_to_mainTOC(self):
		self.close()

# def main():
# 	app = QtWidgets.QApplication(sys.argv)
# 	main = IntroductionWindow()
# 	sys.exit(app.exec_())

# if __name__ == '__main__':
# 	main()