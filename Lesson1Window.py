"""
Lesson 1 Window for 'Thai for Beginners'
Filename: Lesson1Window.py
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
from Lesson1Vocab import Lesson1Vocab
from Lesson1Conv import Lesson1Conv
from Lesson1Sent import Lesson1Sent
from Lesson1Test_1 import Lesson1Test1
import os, sys, random, MainWindow 
from random import choice


from PyQt5.QtWidgets import (
	QMainWindow, QApplication, QWidget, QLabel, QMessageBox, QHBoxLayout, QCheckBox,
	QPushButton, QVBoxLayout, QScrollArea, QSlider, QTabWidget
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
#  Introduction Text Files & other media content
#############################################################
#############################################################

# read in the jpg files for this window
texts = os.listdir('textTOCFiles/')

# attach 'textFiles/' to filenames

for i in range(len(texts)):
	texts[i] = 'textTOCFiles/' + texts[i] 

#############################################################
#  audio mp3 files alphabet
############################################################
# read in the mp3 files
clips = os.listdir('mp3Files/')

# attach 'mp3Files/' file names
for i in range(len(clips)):
	clips[i] = 'mp3Files/' + clips[i]

#############################################################
#  audio mp3 files VOCAB
############################################################
# read in the mp3 files
clipsVocab = os.listdir('mp3Files/')

# attach 'mp3Files/' file names
for i in range(len(clipsVocab)):
	clipsVocab[i] = 'mp3Files' + clipsVocab[i]

#############################################################
#    image png files
############################################################
# read in the png files of the alphabet
pics = os.listdir('AlphaPng/')

# attach 'AlphaPng/' file names
for q in range(len(pics)):
	pics[q] = 'AlphaPng/' + pics[q]

#############################################################
#############################################################
#  Lesson 1 Window
#############################################################
#############################################################

class Lesson1Window(QMainWindow):
	def __init__(self,parent=None):
		super().__init__()

		# main window properties

		self.setWindowTitle("Lesson 1")
		self.setGeometry(400,100,1300,800)
		self.setFixedSize(1300,800)

		# set up the tab widget and properties
		self.tabs = QTabWidget()
		self.tabs.setTabPosition(QTabWidget.South)
		self.tabs.setMovable(False)
		self.tabs.setDocumentMode(True)


		# create the media player for Lesson1Window
		self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.StreamPlayback)

########################################################
########################################################
# create content for the individual tabs
########################################################
########################################################

		########################################################
		########################################################
		# Vocabulary tab
		########################################################
		########################################################

		# define the vocab tab wdiget and add it to the tab widget
		self.vocab = QWidget()
		self.tabs.addTab(self.vocab,"Vocabulary")

		########################################################
		# Vocabulary Main Layout
		########################################################
		# create vocab tab layout
		self.layoutVocab = QVBoxLayout()

		########################################################
		# Vocabulary Label
		########################################################
		# create a label for initial instructions for the Lesson1
		self.text = "Welcome to Lesson 1!  Click on the tabs below to complete Lesson 1. It is recommended to go from left to right to get the most out of this Lesson.  In this tab, we begin with some Vocabulary. You can use the scroller on the side view the Vocabulary list.  When you are done,then proceed to the next tab, 'Conversations'.  You may go back and forth between tabs. Click 'X' to return to Main Menu."
		
		self.vocabInstr = Label()
		self.vocabInstr.setText(self.text)
		self.vocabInstr.resize(100, 100)
		font = QtGui.QFont("Times", 14,QFont.Bold)
		font.setStyleHint(QtGui.QFont.TypeWriter)
		self.vocabInstr.setFont(font)
		self.vocabInstr.formatText()
		# add this label to the vocab layout
		self.layoutVocab.addWidget(self.vocabInstr)
		self.layoutVocab.setAlignment(Qt.AlignTop)

			
		########################################################
		# Vocabulary Scroll Area
		########################################################

		#  importing into the scroll area defined in destination
		#  did not work

		#  Try defining the scroll area in the imported widget
		# then add that to the Lesson1Window.py layout

		# import the Lesson1Vocab scroll widget here
		self.Lesson1Vocab = Lesson1Vocab()

		# add imported scroll widget to vocab tab layout
		self.layoutVocab.addWidget(self.Lesson1Vocab)

		# set the layout vocab for the vocab tab
		self.vocab.setLayout(self.layoutVocab)

		########################################################
		# Vocabulary Scroll Area Signals and slots
		########################################################

		# signals go AFTER .setCentralWidget


		########################################################
		########################################################
		# Conversations tab
		########################################################
		########################################################
		
		self.conversations = QWidget()
		self.tabs.addTab(self.conversations,"Conversations")

		
		########################################################
		# Conversation Main Layout
		########################################################
		# create conv tab layout
		self.layoutConv = QVBoxLayout()

		# import and add the Lesson1Conv class object
		self.Lesson1Conv = Lesson1Conv()
		self.layoutConv.addWidget(self.Lesson1Conv)

		# set the layout for the conversations tab
		self.conversations.setLayout(self.layoutConv)

		########################################################
		########################################################
		# Sentences tab
		########################################################
		########################################################
		
		self.sentences = QWidget()
		self.tabs.addTab(self.sentences,"Sentences")

		########################################################
		# Sentences Main Layout
		########################################################
		# create conv tab layout
		self.layoutSent = QVBoxLayout()

		# import and add the Lesson1Conv class object
		self.Lesson1Sent = Lesson1Sent()
		self.layoutSent.addWidget(self.Lesson1Sent)

		# set the layout for the conversations tab
		self.sentences.setLayout(self.layoutSent)

		########################################################
		########################################################
		# Numbers tab
		########################################################
		########################################################

		self.numbers = QWidget()
		self.tabs.addTab(self.numbers,"Numbers")

		########################################################
		########################################################
		# Test 1 tab
		########################################################
		########################################################
		self.test1 = QWidget()
		self.tabs.addTab(self.test1,"Test 1")

		########################################################
		# Test 1 Main Layout
		########################################################
		# create conv tab layout
		self.layoutTest1 = QVBoxLayout()

		# import and add the Lesson1Conv class object
		self.Lesson1Test1 = Lesson1Test1()
		self.layoutTest1.addWidget(self.Lesson1Test1)

		# set the layout for the conversations tab
		self.test1.setLayout(self.layoutTest1)

		########################################################
		########################################################
		# Thai Writing System tab
		########################################################
		########################################################
		self.thaiWriting = QWidget()
		self.tabs.addTab(self.thaiWriting,"Thai Writing System")

		########################################################
		########################################################
		# Middle Consonants tab
		########################################################
		########################################################
		self.MidCon = QWidget()
		self.tabs.addTab(self.MidCon,"MiddleConsonants")


		########################################################
		########################################################
		# Practice Writing Mid Consonants tab
		########################################################
		########################################################
	
		self.pracWriting = QWidget()
		self.tabs.addTab(self.pracWriting,"Practice Writing Mid Consonants")

		
		########################################################
		########################################################
		# Vowels tab
		########################################################
		########################################################
		self.vowels = QWidget()
		self.tabs.addTab(self.vowels,"Vowels")


		########################################################
		########################################################
		# Practice Writing Vowels tab
		########################################################
		########################################################
		self.pracWritingVowels = QWidget()
		self.tabs.addTab(self.pracWritingVowels,"Practice Writing Vowels")


		########################################################
		########################################################
		# Read Aloud tab
		########################################################
		########################################################
		self.readAloud = QWidget()
		self.tabs.addTab(self.readAloud,"Read Aloud")


		########################################################
		########################################################
		# Tone Marks (Thai Script) tab
		########################################################
		########################################################
		self.toneMarks = QWidget()
		self.tabs.addTab(self.toneMarks,"Tone Marks (Thai Script)")


		########################################################
		########################################################
		# Writing Exercise 1 tab
		########################################################
		########################################################
		self.writingExercise1 = QWidget()
		self.tabs.addTab(self.writingExercise1,"Writing Exercise 1")


		self.setCentralWidget(self.tabs)

################################################
#            Vocab tab signals & slots
####### NOTE: the signals and slots for the vocabtab buttons
#######       need to be added AFTER setting the central widget
#######       for the whole Lesson1Window module

		self.Lesson1Vocab.button0.setObjectName('button0')
		self.Lesson1Vocab.button1.setObjectName('button1')
		self.Lesson1Vocab.button2.setObjectName('button2')
		self.Lesson1Vocab.button3.setObjectName('button3')
		self.Lesson1Vocab.button4.setObjectName('button4')
		self.Lesson1Vocab.button5.setObjectName('button5')
		self.Lesson1Vocab.button6.setObjectName('button6')
		self.Lesson1Vocab.button7.setObjectName('button7')
		self.Lesson1Vocab.button8.setObjectName('button8')
		self.Lesson1Vocab.button9.setObjectName('button9')

		self.Lesson1Vocab.button0.clicked.connect(self.play_video)
		self.Lesson1Vocab.button1.clicked.connect(self.play_video)
		self.Lesson1Vocab.button2.clicked.connect(self.play_video)
		self.Lesson1Vocab.button3.clicked.connect(self.play_video)
		self.Lesson1Vocab.button4.clicked.connect(self.play_video)
		self.Lesson1Vocab.button5.clicked.connect(self.play_video)
		self.Lesson1Vocab.button6.clicked.connect(self.play_video)
		self.Lesson1Vocab.button7.clicked.connect(self.play_video)
		self.Lesson1Vocab.button8.clicked.connect(self.play_video)
		self.Lesson1Vocab.button9.clicked.connect(self.play_video)

		self.Lesson1Vocab.button0.setEnabled(True)
		self.Lesson1Vocab.button1.setEnabled(True)
		self.Lesson1Vocab.button2.setEnabled(True)
		self.Lesson1Vocab.button3.setEnabled(True)
		self.Lesson1Vocab.button4.setEnabled(True)
		self.Lesson1Vocab.button5.setEnabled(True)
		self.Lesson1Vocab.button6.setEnabled(True)
		self.Lesson1Vocab.button7.setEnabled(True)
		self.Lesson1Vocab.button8.setEnabled(True)
		self.Lesson1Vocab.button9.setEnabled(True)

		# list to compare in def play_video(self, e):
		self.list = []
		for i in range(10):
			string = 'button' + str(i)
			self.list.append(string)
		# self.buttonList = set(self.list)
		print(self.list)

	def play_video(self, e):
		btn_name = self.Lesson1Vocab.sender()
		name = '%s' % str(btn_name.objectName())
		print(name)
		pos = self.list.index(name)
		print(str(pos))
		self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(clipsVocab[pos])))
		if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
			self.mediaPlayer.pause()
		else:
			self.mediaPlayer.play()


# class to quickly resize text and produce a QLabel
class Label(QLabel):
    def __init__(self, parent=None):
        super(Label, self).__init__(parent)  

    def resizeEvent(self, event):
        self.formatText()
        event.accept()

    def formatText(self):
        width = self.width()
        text = self.text()
        new = ''
        for word in text.split():
            if len(new.split('\n')[-1])<width*0.0775:
                new = new + ' ' + word
            else:
                new = new + '\n' + ' ' + word
        self.setText(new)



# def main():
# 	app = QtWidgets.QApplication(sys.argv)
# 	main = IntroductionWindow()
# 	sys.exit(app.exec_())

# if __name__ == '__main__':
# 	main()
