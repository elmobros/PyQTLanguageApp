"""
Class file for Lesson 1 Vocabulary for 'Thai for Beginners'
Filename: Lesson1Vocab.py

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

##############################################################
#    TOC files
##############################################################

# read in the jpg files for this window
texts = os.listdir('textTOCFiles/')

# attach 'textFiles/' to filenames

for i in range(len(texts)):
	texts[i] = 'textTOCFiles/' + texts[i] 

print(texts)

##############################################################
#    image png files
##############################################################
# read in the png files of the alphabet
pics = os.listdir('AlphaPng/')

# attach 'AlphaPng/' file names
for q in range(len(pics)):
	pics[q] = 'AlphaPng/' + pics[q]

#############################################################
#############################################################
#  Lesson 1 Vocab class
#############################################################
#############################################################

class Lesson1Vocab(QWidget):
	def __init__(self):

		super().__init__()

#############################################################
#  Create the media Player
#############################################################

		# self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.StreamPlayback)

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
		self.subwidgetLayout = QHBoxLayout()

#############################################################
#  Create the subsubwidgets, layout
#############################################################

		# This section is working but the spacings NEEDS WORK

		# layout for two first columns
		# self.text0text1Layout = QHBoxLayout()

		###################  add label widgets thai
		# text0 = "PlaceHolder0"
		self.text0Layout = QVBoxLayout()
		self.v00 = QLabel("ผม")
		self.v00.setFont(QFont('Times', 28))
		self.text0Layout.addWidget(self.v00)

		self.v01 = QLabel("ดิฉัน ดิชั้น / ฉัน ")
		self.v01.setFont(QFont('Times', 28))
		self.text0Layout.addWidget(self.v01)

		self.v02 = QLabel("คุณ")
		self.v02.setFont(QFont('Times', 28))
		self.text0Layout.addWidget(self.v02)

		self.v03 = QLabel("ชื่อ")
		self.v03.setFont(QFont('Times', 28))
		self.text0Layout.addWidget(self.v03)


		self.v04 = QLabel("สวัสดี")
		self.v04.setFont(QFont('Times', 28))
		self.text0Layout.addWidget(self.v04)

		self.v05 = QLabel("สบายดีไหม / สบายดีหรือ")
		self.v05.setFont(QFont('Times', 28))
		self.text0Layout.addWidget(self.v05)

		self.v06 = QLabel("สบายดี")
		self.v06.setFont(QFont('Times', 28))
		self.text0Layout.addWidget(self.v06)

		self.v07 = QLabel("ยินดีที่ได้รู้จัก")
		self.v07.setFont(QFont('Times', 28))
		self.text0Layout.addWidget(self.v07)

		self.v08 = QLabel("เช่นกัน")
		self.v08.setFont(QFont('Times', 28))
		self.text0Layout.addWidget(self.v08)

		self.v09 = QLabel("ขอโทษ")
		self.v09.setFont(QFont('Times', 28))
		self.text0Layout.addWidget(self.v09)

		# self.text0Layout.addWidget(QLabel("ไม่เป็นไร"))
		# for i in range(10):
		# 	picture = QPixmap(pics[i])
		# 	picture = picture.scaled(100,100,Qt.KeepAspectRatio)
		# 	label = QLabel()
		# 	label.setPixmap(picture) 
		# 	self.text0Layout.addWidget(label)

		# titlePicture = QPixmap('main.jpg')
		# titlePicture = titlePicture.scaled(550,550,Qt.KeepAspectRatio)
		# self.pictureMain.setPixmap(titlePicture)
		

		# add label widgets english pronunciation
		text1 = "PlaceHolder1"
		self.text1Layout = QVBoxLayout()
		epSize = 16
		self.ep00 = QLabel(u"po\u030Cm ")
		# self.ep00 = QLabel("pom")
		self.ep00.setFont(QFont('Times',epSize))
		self.text1Layout.addWidget(self.ep00)

		self.ep01 = QLabel(u"di\u0300-cha\u0301n / cha\u0301n")
		# self.ep01 = QLabel("di-chan / chan")
		self.ep01.setFont(QFont('Times',epSize))
		self.text1Layout.addWidget(self.ep01)

		self.ep02 = QLabel("kun")
		self.ep02.setFont(QFont('Times',epSize))
		self.text1Layout.addWidget(self.ep02)

		self.ep03 = QLabel(u"chu\u0302\u0330u\u0330")
		# self.ep03 = QLabel("chuu")
		self.ep03.setFont(QFont('Times',epSize))
		self.text1Layout.addWidget(self.ep03)

		self.ep04 = QLabel(u"sa\u0300-wa\u0300tdii")
		# self.ep04 = QLabel("sa-watdii")
		self.ep04.setFont(QFont('Times',epSize))
		self.text1Layout.addWidget(self.ep04)

		self.ep05 = QLabel(u"sa\u0300-baai dii ma\u0301i /\n sa\u0300-baai dii ru\u0330\u030Cu\u0330")
		# self.ep05 = QLabel("sa-baai dii mai /\n sa-baai dii ruu")
		self.ep05.setFont(QFont('Times',epSize))
		self.text1Layout.addWidget(self.ep05)

		self.ep06 = QLabel(u"sa\u0300-baai dii")
		# self.ep06 = QLabel("sa-baai dii")
		self.ep06.setFont(QFont('Times',epSize))
		self.text1Layout.addWidget(self.ep06)

		self.ep07 = QLabel(u"yindii ti\u0302i da\u0302ai\n ru\u0301u-ja\u0300k")
		# self.ep07 = QLabel("yindii tii dai\n ruu-jak")
		self.ep07.setFont(QFont('Times',epSize))
		self.text1Layout.addWidget(self.ep07)

		self.ep08 = QLabel(u"che\u0302n-gan")
		# self.ep08 = QLabel("chen-gan")
		self.ep08.setFont(QFont('Times',epSize))
		self.text1Layout.addWidget(self.ep08)

		self.ep09 = QLabel(u"k\u2184\u030C\u2184-to\u0302ot")
		# self.ep09 = QLabel("kcc-toot")
		self.ep09.setFont(QFont('Times',epSize))
		self.text1Layout.addWidget(self.ep09)

		# self.ep09 = QLabel(u"ma\u032Di bpenrai")
		# self.ep09 = QLabel("mai bpenrai")
		# self.ep09.setFont(QFont('Times',epSize))
		# self.text1Layout.addWidget(QLabel(self.ep09))

		# add the two first columns to their layout
		# self.text0text1Layout.addLayout(self.text0Layout)
		# self.text0text1Layout.addLayout(self.text1Layout)
		# self.text0text1Layout.setSpacing(40)

		##################### add label english definition
		text2 = "PlaceHolder2"
		self.text2Layout = QVBoxLayout()
		eSize = 18
		self.e00 = QLabel("I, me (Male speaker)")
		self.e00.setFont(QFont('Times', eSize))
		self.text2Layout.addWidget(self.e00)

		self.e01 = QLabel("I, me (Female speaker)")
		self.e01.setFont(QFont('Times', eSize))
		self.text2Layout.addWidget(self.e01)

		self.e02 = QLabel("you")
		self.e02.setFont(QFont('Times', eSize))
		self.text2Layout.addWidget(self.e02)

		self.e03 = QLabel("name")
		self.e03.setFont(QFont('Times', eSize))
		self.text2Layout.addWidget(self.e03)

		self.e04 = QLabel("'Good day.'")
		self.e04.setFont(QFont('Times', eSize))
		self.text2Layout.addWidget(self.e04)

		self.e05 = QLabel("'How are you?'")
		self.e05.setFont(QFont('Times', eSize))
		self.text2Layout.addWidget(self.e05)

		self.e06 = QLabel("to be fine")
		self.e06.setFont(QFont('Times', eSize))
		self.text2Layout.addWidget(self.e06)

		self.e07 = QLabel("Nice to meet you.")
		self.e07.setFont(QFont('Times', eSize))
		self.text2Layout.addWidget(self.e07)

		self.e08 = QLabel("Same here.")
		self.e08.setFont(QFont('Times', eSize))
		self.text2Layout.addWidget(self.e08)

		self.e09 = QLabel("Excuse me.")
		self.e09.setFont(QFont('Times', eSize))
		self.text2Layout.addWidget(self.e09)

		# for i in range(10):
		# 	self.text2Layout.addWidget(QLabel(text2))

		############# add button for thai audio
		
		##### text3 = "PlaceHolder3"
		self.text3Layout = QVBoxLayout()
		# most likely needs a lambda function solution
		# definitely prefer a for loop solution
		# for i in range(20):
		# 	string = 'button' + str(i)
		# 	self.string = QPushButton(string)
		# 	self.text3Layout.addWidget(self.string)


		self.button0 = QPushButton("Play Audio")
		self.button0.setFixedSize(120,40)
		self.button0.setFont(QFont('Times', 15))
		self.button0.setStyleSheet("border-radius : 12; border : 2px solid black;\
											background-color: rgb( 130,120,255)")
		self.button1 = QPushButton("Play Audio")
		self.button1.setFixedSize(120,40)
		self.button1.setFont(QFont('Times', 15))
		self.button1.setStyleSheet("border-radius : 12; border : 2px solid black;\
											background-color: rgb( 130,120,255)")
		self.button2 = QPushButton("Play Audio")
		self.button2.setFixedSize(120,40)
		self.button2.setFont(QFont('Times', 15))
		self.button2.setStyleSheet("border-radius : 12; border : 2px solid black;\
											background-color: rgb( 130,120,255)")
		self.button3 = QPushButton("Play Audio")
		self.button3.setFixedSize(120,40)
		self.button3.setFont(QFont('Times', 15))
		self.button3.setStyleSheet("border-radius : 12; border : 2px solid black;\
											background-color: rgb( 130,120,255)")
		self.button4 = QPushButton("Play Audio")
		self.button4.setFixedSize(120,40)
		self.button4.setFont(QFont('Times', 15))
		self.button4.setStyleSheet("border-radius : 12; border : 2px solid black;\
											background-color: rgb( 130,120,255)")
		self.button5 = QPushButton("Play Audio")
		self.button5.setFixedSize(120,40)
		self.button5.setFont(QFont('Times', 15))
		self.button5.setStyleSheet("border-radius : 12; border : 2px solid black;\
											background-color: rgb( 130,120,255)")	
		self.button6 = QPushButton("Play Audio")
		self.button6.setFixedSize(120,40)
		self.button6.setFont(QFont('Times', 15))
		self.button6.setStyleSheet("border-radius : 12; border : 2px solid black;\
											background-color: rgb( 130,120,255)")	
		self.button7 = QPushButton("Play Audio")
		self.button7.setFixedSize(120,40)
		self.button7.setFont(QFont('Times', 15))
		self.button7.setStyleSheet("border-radius : 12; border : 2px solid black;\
											background-color: rgb( 130,120,255)")
		self.button8 = QPushButton("Play Audio")
		self.button8.setFixedSize(120,40)
		self.button8.setFont(QFont('Times', 15))
		self.button8.setStyleSheet("border-radius : 12; border : 2px solid black;\
											background-color: rgb( 130,120,255)")
		self.button9 = QPushButton("Play Audio")
		self.button9.setFixedSize(120,40)
		self.button9.setFont(QFont('Times', 15))
		self.button9.setStyleSheet("border-radius : 12; border : 2px solid black;\
											background-color: rgb( 130,120,255)")

		# self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(clips[9])))
		# self.button9.setEnabled(True)

		self.text3Layout.addWidget(self.button0)
		self.text3Layout.addWidget(self.button1)
		self.text3Layout.addWidget(self.button2)
		self.text3Layout.addWidget(self.button3)
		self.text3Layout.addWidget(self.button4)
		self.text3Layout.addWidget(self.button5)
		self.text3Layout.addWidget(self.button6)
		self.text3Layout.addWidget(self.button7)
		self.text3Layout.addWidget(self.button8)
		self.text3Layout.addWidget(self.button9)		

		# add those layouts to the subwidget layout
		self.subwidgetLayout.addLayout(self.text0Layout)
		self.subwidgetLayout.addLayout(self.text1Layout)
		self.subwidgetLayout.addLayout(self.text2Layout)
		self.subwidgetLayout.addLayout(self.text3Layout)


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
		# self.subwidgetLayout.setAlignment(Qt.AlignVCenter)

		# set spacing for columns
		self.subwidgetLayout.setSpacing(60)

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

	



# def main():
# 	app = QApplication(sys.argv)
# 	main = Lesson1Vocab()
# 	sys.exit(app.exec_())

# if __name__ == '__main__':
# 	main()
