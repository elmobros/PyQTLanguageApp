"""
Main window for 'Thai for Beginners'
Filename: MainWindow.py
"""

__version__ = '0.1'
__author__ = 'Sean Nomoto'

###############################################################
#################################################################
# import needed libraries, classes, functions, py files
###############################################################
###############################################################

import os, sys, random
import IntroWindow, TOCWindow
import Lesson1Window 

 
from random import choice

from PyQt5.QtWidgets import (
	QMainWindow, QApplication, QWidget, QLabel, QMessageBox, QHBoxLayout, QCheckBox,
	QPushButton, QVBoxLayout, QScrollArea, QStatusBar
)
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import Qt, QSize, QUrl
from PyQt5.Qt import (
	QPixmap, QFont, QCloseEvent, QPalette
)
from PyQt5 import QtCore


#############################################################
#############################################################
#  Audio and Images
#############################################################
#############################################################

#################################################################################
#    image png files
###################################################################################
# read in the png files of the alphabet
pics = os.listdir('AlphaPng/')

# attach 'AlphaPng/' file names
for q in range(len(pics)):
	pics[q] = 'AlphaPng/' + pics[q]



#############################################################################
#  audio mp3 files
#############################################################################

# read in the mp3 files
clips = os.listdir('mp3Files/')

# attach 'mp3Files/' file names
for i in range(len(clips)):
	clips[i] = 'mp3Files/' + clips[i]

# print list to console to be sure list has files
# print(clips)


#############################################################
#############################################################
#  Main Window
#############################################################
#############################################################

class MainWindow(QMainWindow):
	def __init__(self):

		super().__init__()

#############################################################
#  Main Window Properties
#############################################################
		## basic properties of the main window
		
		# size and position
		self.setWindowTitle("Thai for Beginners")
		self.setGeometry(500,100,1000,2000)
		self.setFixedSize(1000,800)


#############################################################
#  Main Window widgets
#############################################################
		# set main window as a widget
		self.widgetMain = QWidget(self)
		

##################  for layoutMain0L
		
		# create Title with QLabel widget
		self.titleMain = QLabel("Thai for Beginners")
		self.titleMain.setFont(QFont('Times', 35, QFont.Bold))
		self.titleMain.setAlignment(Qt.AlignCenter)


		# create picture with QLabel widget and QPixmap
		self.pictureMain = QLabel()
		titlePicture = QPixmap('main.jpg')
		titlePicture = titlePicture.scaled(550,550,Qt.KeepAspectRatio)
		self.pictureMain.setPixmap(titlePicture)
		self.pictureMain.setAlignment(Qt.AlignCenter)

		# Instuctions using QLabel
		self.instructions = QLabel("สวัสดี ครับ!!  Hello!! Welcome to Thai for Beginners! \
			\n To get started click any of the Buttons in the \n Main Menu.")
		self.instructions.setFont(QFont('Times', 18))
		self.instructions.setAlignment(Qt.AlignCenter)

		# create exit button
		self.buttonExit = QPushButton("Close and Exit (แล้ว) Application")
		self.buttonExit.setFont(QFont('Times', 15))
		self.buttonExit.setStatusTip("Close and Exit this Program")
		self.buttonExit.setToolTip("Close and Exit this Program")
		self.buttonExit.setFixedSize(350,50)
		self.buttonExit.setStyleSheet("border-radius : 12; border : 2px solid black")

####################  for layoutMain0R
		
		# label with QLabel
		self.menuMain = QLabel("Main Menu")
		self.menuMain.setFont(QFont('Times',25, QFont.Bold))
		self.menuMain.setAlignment(Qt.AlignCenter)

		# create buttons
		
		self.buttonIntro =QPushButton("Introduction")
		self.buttonIntro.setStatusTip("Brief Preface describing who this app is for what you can expect!")
		self.buttonIntro.setToolTip("Brief Preface describing who this app is for what you can expect!")
		self.buttonIntro.setFixedSize(400,40)
		self.buttonIntro.setFont(QFont('Times', 15))
		self.buttonIntro.setStyleSheet("border-radius : 12; border : 2px solid black;\
											background-color: rgb( 255,255,100)")
		
		self.buttonTOC = QPushButton("Table of Contents")
		self.buttonTOC.setFixedSize(400,40)
		self.buttonTOC.setStatusTip("List of Lessons, Apps, and their contents!")
		self.buttonTOC.setToolTip("List of Lessons, Apps, and their contents!")
		self.buttonTOC.setFont(QFont('Times', 15))
		self.buttonTOC.setStyleSheet("border-radius : 12; border : 2px solid black;\
											background-color: rgb( 255,255,100)")
		
		self.buttonGTP = QPushButton("Guide to Pronunciation")
		self.buttonGTP.setFixedSize(400,40)
		self.buttonGTP.setStatusTip("Tips on Pronunciation and using the Paiboon system for transliteration!")
		self.buttonGTP.setToolTip("Tips on Pronunciation and using the Paiboon system for transliteration!")
		self.buttonGTP.setFont(QFont('Times', 15))
		self.buttonGTP.setStyleSheet("border-radius : 12; border : 2px solid black;\
											background-color: rgb( 255,255,100)")
		
		self.buttonLesson1 = QPushButton("Lesson 1")
		self.buttonLesson1.setFixedSize(400,40)
		self.buttonLesson1.setStatusTip("Greetings, intro to tones, consonant classes, vowels, yes-no questiosn and numbers")
		self.buttonLesson1.setToolTip("Greetings, intro to tones, consonant classes, vowels, yes-no questiosn and numbers")
		self.buttonLesson1.setFont(QFont('Times', 15))
		self.buttonLesson1.setStyleSheet("border-radius : 12; border : 2px solid black;\
											background-color: rgb( 120,140,255)")
		
		self.buttonLesson2 = QPushButton("Lesson 2")
		self.buttonLesson2.setFixedSize(400,40)
		self.buttonLesson2.setStatusTip("'to be' particle, more vowels, live & dead syllables, middle consonant tone rules")
		self.buttonLesson2.setToolTip("Greetings, intro to tones, consonant classes, yes-no questions and numbers")
		self.buttonLesson2.setFont(QFont('Times', 15))
		self.buttonLesson2.setStyleSheet("border-radius : 12; border : 2px solid black;\
											background-color: rgb( 170,245,0)")

		self.buttonLesson3 = QPushButton("Lesson 3")
		self.buttonLesson3.setFixedSize(400,40)
		self.buttonLesson3.setStatusTip("Colors, future particle, `can' verb, complex vowels, changing vowel forms, more tone rules")
		self.buttonLesson3.setToolTip("Colors, future particle, `can' verb, complex vowels, changing vowel forms, more tone rules")
		self.buttonLesson3.setFont(QFont('Times', 15))
		self.buttonLesson3.setStyleSheet("border-radius : 12; border : 2px solid black;\
											background-color: rgb( 225,150,0)")

		self.buttonLesson4 = QPushButton("Lesson 4")
		self.buttonLesson4.setFixedSize(400,40)
		self.buttonLesson4.setStatusTip("Telling time, high consonants and their tone rules")
		self.buttonLesson4.setToolTip("Telling time, high consonants and their tone rules")
		self.buttonLesson4.setFont(QFont('Times', 15))
		self.buttonLesson4.setStyleSheet("border-radius : 12; border : 2px solid black;\
											background-color: rgb( 175,120,255)")

		self.buttonLesson5 = QPushButton("Lesson 5")
		self.buttonLesson5.setFixedSize(400,40)
		self.buttonLesson5.setStatusTip("Days of the week, months, tone marks with high consonants, low consonants")
		self.buttonLesson5.setToolTip("Days of the week, months, tone marks with high consonants, low consonants")
		self.buttonLesson5.setFont(QFont('Times', 15))
		self.buttonLesson5.setStyleSheet("border-radius : 12; border : 2px solid black;\
											background-color: rgb( 150,250,150)")

		self.buttonLesson6 = QPushButton("Lesson 6")
		self.buttonLesson6.setFixedSize(400,40)
		self.buttonLesson6.setStatusTip("`to want' verb; `to be doing' verb, tone rules for low consonants")
		self.buttonLesson6.setToolTip("`to want' verb; `to be doing' verb, tone rules for low consonants")
		self.buttonLesson6.setFont(QFont('Times', 15))
		self.buttonLesson6.setStyleSheet("border-radius : 12; border : 2px solid black;\
											background-color: rgb( 100, 255, 255)")

		self.buttonLesson7 = QPushButton("Lesson 7")
		self.buttonLesson7.setFixedSize(400,40)
		self.buttonLesson7.setStatusTip("`to hear' verb, `to remember' verb, to fall asleep, to look, and more low consonant tone rules")
		self.buttonLesson7.setToolTip("`to hear' verb, `to remember' verb, to fall asleep, to look, and more low consonant tone rules")
		self.buttonLesson7.setFont(QFont('Times', 15))
		self.buttonLesson7.setStyleSheet("border-radius : 12; border : 2px solid black;\
											background-color: rgb( 255,255,100)")

		self.buttonLesson8= QPushButton("Lesson 8")
		self.buttonLesson8.setFixedSize(400,40)
		self.buttonLesson8.setStatusTip("Body parts, everyday life, special particles")
		self.buttonLesson8.setToolTip("Body parts, everyday life, special particles")
		self.buttonLesson8.setFont(QFont('Times', 15))
		self.buttonLesson8.setStyleSheet("border-radius : 12; border : 2px solid black;\
											background-color: rgb( 255,100,255)")

		self.buttonLesson9= QPushButton("Lesson 9")
		self.buttonLesson9.setFixedSize(400,40)
		self.buttonLesson9.setStatusTip("Family & kinship terms, occupations, animals, and another particle and other features of written Thai")
		self.buttonLesson9.setToolTip("Family & kinship terms, occupations, animals, and another particle and other features of written Thai")
		self.buttonLesson9.setFont(QFont('Times', 15))
		self.buttonLesson9.setStyleSheet("border-radius : 12; border : 2px solid black;\
											background-color: rgb( 130,120,255)")

		self.buttonLesson10= QPushButton("Lesson 10")
		self.buttonLesson10.setFixedSize(400,40)
		self.buttonLesson10.setStatusTip("Comparisons, adjectives, and classifiers")
		self.buttonLesson10.setToolTip("Comparisons, adjectives, and classifiers")
		self.buttonLesson10.setFont(QFont('Times', 15))
		self.buttonLesson10.setStyleSheet("border-radius : 12; border : 2px solid black;\
											background-color: rgb( 100,255,100)")

		self.buttonAppx = QPushButton("Appx: Thai Writing System Summary")
		self.buttonAppx.setFixedSize(400,40)
		self.buttonAppx.setStatusTip("Summary of the Thai Writing System")
		self.buttonAppx.setToolTip("Summary of the Thai Writing System")
		self.buttonAppx.setFont(QFont('Times', 15))
		self.buttonAppx.setStyleSheet("border-radius : 12; border : 2px solid black;\
											background-color: rgb(255, 130 , 130)")

		self.buttonIndex = QPushButton("Index")
		self.buttonIndex.setFixedSize(400,40)
		self.buttonIndex.setStatusTip("List of vocabulary words")
		self.buttonIndex.setToolTip("List of vocabulary words")
		self.buttonIndex.setFont(QFont('Times', 15))
		self.buttonIndex.setStyleSheet("border-radius : 12; border : 2px solid black; \
											background-color: yellow")

        # show the button status'
		self.setStatusBar(QStatusBar(self))

#############################################################
#  Main Window layouts
#############################################################	
		# Layout0 for the mainwindow
		self.layoutMain0 = QHBoxLayout()

		
		# set layout for widgetMain
		self.widgetMain.setLayout(self.layoutMain0) 

		## create layout main vertical left
		self.layoutMain0L = QVBoxLayout()
		self.layoutMain0L.setAlignment(Qt.AlignTop)


		## create layout main vertical right
		self.layoutMain0R = QVBoxLayout()
		self.layoutMain0R.setAlignment(Qt.AlignTop)

#############################################################
#  add widgets to layouts
#############################################################

###########for layoutMain0L
		# add titleMain
		self.layoutMain0L.addWidget(self.titleMain)
		# add pictureMain
		self.layoutMain0L.addWidget(self.pictureMain)
		self.layoutMain0L.addWidget(self.instructions)
		self.layoutMain0L.addWidget(self.buttonExit, alignment=QtCore.Qt.AlignBottom | QtCore.Qt.AlignCenter)
		self.layoutMain0L.setSpacing(100)

############# for layoutMain0R
		self.layoutMain0R.addWidget(self.menuMain)
		self.layoutMain0R.addWidget(self.buttonIntro)
		self.layoutMain0R.addWidget(self.buttonTOC)
		self.layoutMain0R.addWidget(self.buttonGTP)
		self.layoutMain0R.addWidget(self.buttonLesson1)
		self.layoutMain0R.addWidget(self.buttonLesson2)
		self.layoutMain0R.addWidget(self.buttonLesson3)
		self.layoutMain0R.addWidget(self.buttonLesson4)
		self.layoutMain0R.addWidget(self.buttonLesson5)
		self.layoutMain0R.addWidget(self.buttonLesson6)
		self.layoutMain0R.addWidget(self.buttonLesson7)
		self.layoutMain0R.addWidget(self.buttonLesson8)
		self.layoutMain0R.addWidget(self.buttonLesson9)
		self.layoutMain0R.addWidget(self.buttonLesson10)
		self.layoutMain0R.addWidget(self.buttonAppx)
		self.layoutMain0R.addWidget(self.buttonIndex)
		self.layoutMain0R.setSpacing(15)

################ for layoutMain0
		self.layoutMain0.addLayout(self.layoutMain0L)
		self.layoutMain0.addLayout(self.layoutMain0R)

#############################################################
#  setup the main widget and its layout
#############################################################
	
		self.widgetMain.setLayout(self.layoutMain0)
		self.setCentralWidget(self.widgetMain)

#############################################################
#  signals for MainWindow Widgets
#############################################################
		
##########   layoutMain0L Widgets
		self.buttonExit.clicked.connect(self.exit_program)

#########    layoutMain0R Widgets
		self.buttonIntro.clicked.connect(self.open_introduction)
		self.buttonTOC.clicked.connect(self.open_TOC)
		# self.buttonGTP.clicked.connect(self.open_GTP)
		self.buttonLesson1.clicked.connect(self.open_Lesson1)
		# self.buttonLesson2.clicked.connect(self.open_Lesson2)
		# self.buttonLesson3.clicked.connect(self.open_Lesson3)
		# self.buttonLesson4.clicked.connect(self.open_Lesson4)
		# self.buttonLesson5.clicked.connect(self.open_Lesson5)
		# self.buttonLesson6.clicked.connect(self.open_Lesson6)
		# self.buttonLesson7.clicked.connect(self.open_Lesson7)
		# self.buttonLesson8.clicked.connect(self.open_Lesson8)
		# self.buttonLesson9.clicked.connect(self.open_Lesson9)
		# self.buttonLesson10.clicked.connect(self.open_Lesson10)
		# self.buttonAppx.clicked.connect(self.open_Appx)
		# self.buttonIndex.clicked.connect(self.open_Index)

#############################################################
#  slots for MainWindow Widgets' signals
#############################################################	

	def exit_program(self):
		self.close()

	def open_introduction(self, checked):
		self.w = IntroWindow.IntroductionWindow()
		self.w.show()

	def open_TOC(self, checked):
		self.w = TOCWindow.TOCWindow()
		self.w.show()

	# def open_GTP(self, checked):
	# 	self.w = GTPWindow.GTPWindow()
	# 	self.w.show()

	def open_Lesson1(self, checked):
		self.w = Lesson1Window.Lesson1Window()
		self.w.show()

	# def open_Lesson2(self, checked):
	# 	self.w = Lesson1Window.Lesson2Window()
	# 	self.w.show()

	# def open_Lesson3(self, checked):
	# 	self.w = Lesson1Window.Lesson3Window()
	# 	self.w.show()

	# def open_Lesson4(self, checked):
	# 	self.w = Lesson1Window.Lesson4Window()
	# 	self.w.show()

	# def open_Lesson5(self, checked):
	# 	self.w = Lesson1Window.Lesson5Window()
	# 	self.w.show()

	# def open_Lesson6(self, checked):
	# 	self.w = Lesson1Window.Lesson6Window()
	# 	self.w.show()

	# def open_Lesson7(self, checked):
	# 	self.w = Lesson1Window.Lesson7Window()
	# 	self.w.show()

	# def open_Lesson8(self, checked):
	# 	self.w = Lesson1Window.Lesson8Window()
	# 	self.w.show()

	# def open_Lesson9(self, checked):
	# 	self.w = Lesson1Window.Lesson9Window()
	# 	self.w.show()

	# def open_Lesson10(self, checked):
	# 	self.w = Lesson1Window.Lesson10Window()
	# 	self.w.show()

	# def open_Appx(self, checked):
	# 	self.w = AppxWindow.AppxWindow()
	# 	self.w.show()

	# def open_Index(self, checked):
	# 	self.w = IndexWindow.IndexWindow()
	# 	self.w.show()

#############################################################
#############################################################
#  Introduction Window
#############################################################
#############################################################

"""
Make this a separate script IntroWindow.py and import this 
like this:  "import IntroWindow" and it will be called as
IntroWindow.IntroductionWindow()
"""

#############################################################
#############################################################
#  TOC Window
#############################################################
#############################################################

"""
Make this a separate script TOCWindow.py and import this 
like this:  "import TOCWindow" and it will be called as
TOCWindow.TOCWindow()
"""

#############################################################
#############################################################
#  Lesson Windows 1 through 10
#############################################################
#############################################################

"""
Make this a separate script TOCWindow.py and import this 
like this:  "import LessonXWindow" and it will be called as
LessonXWindow.LessonXWindow()
"""

#############################################################
#############################################################
#  main function for the application/program
#############################################################
#############################################################

def main():
	mainwindow = QApplication(sys.argv)
	w = MainWindow()
	w.show()
	sys.exit(mainwindow.exec())

if __name__ == '__main__':
	main()

