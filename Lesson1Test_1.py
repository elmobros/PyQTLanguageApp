"""
Class file for Lesson 1 Test 1 for 'Thai for Beginners'
Filename:Lesson1Test_1.py

"""


###############################################################
#################################################################
# import needed libraries, classes, functions
###############################################################
###############################################################

import os, sys, random
from random import choice

from PyQt5.QtWidgets import (
	QComboBox, QLineEdit, QMainWindow, QApplication, QWidget, QLabel, QMessageBox, QHBoxLayout, QCheckBox,
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


#############################################################
#############################################################
#  Lesson 1 Test 1 class
#############################################################
#############################################################


class Lesson1Test1(QWidget):
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

        # set the layout for the subwidget inside the scroll area
        self.subwidgetLayout = QVBoxLayout()

#############################################################
#  Create the subsubwidgets, layout
#############################################################

        # Title for Test 1
        self.title = QLabel("Test 1") 
        self.title.setFont(QFont('Times', 30))
        # add the title QLabel widget to subwidget layout
        self.subwidgetLayout.addWidget(self.title)

        # create instructions for matching part
        self.matchInstruct = QLabel("Match the English with the Thai words.\
        \nThere are more words shown than needed.\nUse the drop-down menus to choose the correct translation and then click submit below.")
        self.matchInstruct.setFont(QFont('Times',16))
        # add the instruction to the subwidgetLayout
        self.subwidgetLayout.addWidget(self.matchInstruct)

        # create the blanks and the match items for it,
        #  and make a sub layouts for the matching section
        # match layout contains layout for blanks, and items layout
        self.matchLayout = QHBoxLayout()
        self.matchBlankLayout = QHBoxLayout()
        self.matchLayoutBlanksNums = QVBoxLayout()
        self.matchLayoutBlanks = QVBoxLayout()
        self.matchLayoutItems = QVBoxLayout()

        # create QLabels for numebering the blanks
        self.match00Num = QLabel('1. watch')
        self.match00Num.setFont(QFont('Helvetica', 22))
        self.matchLayoutBlanksNums.addWidget(self.match00Num)
        self.match01Num = QLabel('2. book')
        self.match01Num.setFont(QFont('Helvetica', 22))
        self.matchLayoutBlanksNums.addWidget(self.match01Num)
        self.match02Num = QLabel('3. pen')
        self.match02Num.setFont(QFont('Helvetica', 22))
        self.matchLayoutBlanksNums.addWidget(self.match02Num)
        self.match03Num = QLabel('4. this')
        self.match03Num.setFont(QFont('Helvetica', 22))
        self.matchLayoutBlanksNums.addWidget(self.match03Num)
        self.match04Num = QLabel('5. I (male speaker)')
        self.match04Num.setFont(QFont('Helvetica', 22))
        self.matchLayoutBlanksNums.addWidget(self.match04Num)
        self.match05Num = QLabel('6. also')
        self.match05Num.setFont(QFont('Helvetica', 22))
        self.matchLayoutBlanksNums.addWidget(self.match05Num)
        self.match06Num = QLabel('7. map')
        self.match06Num.setFont(QFont('Helvetica', 22))
        self.matchLayoutBlanksNums.addWidget(self.match06Num)
        self.match07Num = QLabel('8. name')
        self.match07Num.setFont(QFont('Helvetica', 22))
        self.matchLayoutBlanksNums.addWidget(self.match07Num)
        self.match08Num = QLabel('9. what')
        self.match08Num.setFont(QFont('Helvetica', 22))
        self.matchLayoutBlanksNums.addWidget(self.match08Num)
        self.match09Num = QLabel('10. bag')
        self.match09Num.setFont(QFont('Helvetica', 22))
        self.matchLayoutBlanksNums.addWidget(self.match09Num)


        # create the blanks (QComboboxes and add them, to Blank layout)
        # and create label for numbering the boxes
        
        self.match00 = QComboBox()
        self.match00.addItems(["a","b","c","d","e","f","g",\
        "h","i","j","k","l","m"])
        self.match00.setFont(QFont('Helvetica',22))
        self.match00.setEditable(False)
        self.match00.setFixedSize(100,75)
        self.match00.setStyleSheet("margin: 10px; padding: 10px; \
                                 background-color: \
                                 rgba(150,150,250,155);\
                                 color: rgba(100,0,0,255); \
                                 border-style: solid; \
                                 border-radius: 15px; \
                                 border-width: 1px; \
                                 border-color: \
                                 rgba(255,255,155,255);")
        self.matchLayoutBlanks.addWidget(self.match00)
        self.match01 = QComboBox()
        self.match01.addItems(["a","b","c","d","e","f","g",\
        "h","i","j","k","l","m"])
        self.match01.setFont(QFont('Helvetica',22))
        self.match01.setEditable(False)
        self.match01.setFixedSize(100,75)
        self.match01.setStyleSheet("margin: 10px; padding: 10px; \
                                 background-color: \
                                 rgba(150,150,250,155);\
                                 color: rgba(100,0,0,255); \
                                 border-style: solid; \
                                 border-radius: 15px; \
                                 border-width: 1px; \
                                 border-color: \
                                 rgba(255,255,155,255);")
        self.matchLayoutBlanks.addWidget(self.match01)
        self.match02 = QComboBox()
        self.match02.addItems(["a","b","c","d","e","f","g",\
        "h","i","j","k","l","m"])
        self.match02.setFont(QFont('Helvetica',22))
        self.match02.setEditable(False)
        self.match02.setFixedSize(100,75)
        self.match02.setStyleSheet("margin: 10px; padding: 10px; \
                                 background-color: \
                                 rgba(150,150,250,155);\
                                 color: rgba(100,0,0,255); \
                                 border-style: solid; \
                                 border-radius: 15px; \
                                 border-width: 1px; \
                                 border-color: \
                                 rgba(255,255,155,255);")
        self.matchLayoutBlanks.addWidget(self.match02)
        self.match03 = QComboBox()
        self.match03.addItems(["a","b","c","d","e","f","g",\
        "h","i","j","k","l","m"])
        self.match03.setFont(QFont('Helvetica',22))
        self.match03.setEditable(False)
        self.match03.setFixedSize(100,75)
        self.match03.setStyleSheet("margin: 10px; padding: 10px; \
                                 background-color: \
                                 rgba(150,150,250,155);\
                                 color: rgba(100,0,0,255); \
                                 border-style: solid; \
                                 border-radius: 15px; \
                                 border-width: 1px; \
                                 border-color: \
                                 rgba(255,255,155,255);")
        self.matchLayoutBlanks.addWidget(self.match03)
        self.match04 = QComboBox()
        self.match04.addItems(["a","b","c","d","e","f","g",\
        "h","i","j","k","l","m"])
        self.match04.setFont(QFont('Helvetica',22))
        self.match04.setEditable(False)
        self.match04.setFixedSize(100,75)
        self.match04.setStyleSheet("margin: 10px; padding: 10px; \
                                 background-color: \
                                 rgba(150,150,250,155);\
                                 color: rgba(100,0,0,255); \
                                 border-style: solid; \
                                 border-radius: 15px; \
                                 border-width: 1px; \
                                 border-color: \
                                 rgba(255,255,155,255);")
        self.matchLayoutBlanks.addWidget(self.match04)
        self.match05 = QComboBox()
        self.match05.addItems(["a","b","c","d","e","f","g",\
        "h","i","j","k","l","m"])
        self.match05.setFont(QFont('Helvetica',22))
        self.match05.setEditable(False)
        self.match05.setFixedSize(100,75)
        self.match05.setStyleSheet("margin: 10px; padding: 10px; \
                                 background-color: \
                                 rgba(150,150,250,155);\
                                 color: rgba(100,0,0,255); \
                                 border-style: solid; \
                                 border-radius: 15px; \
                                 border-width: 1px; \
                                 border-color: \
                                 rgba(255,255,155,255);")
        self.matchLayoutBlanks.addWidget(self.match05)
        self.match06 = QComboBox()
        self.match06.addItems(["a","b","c","d","e","f","g",\
        "h","i","j","k","l","m"])
        self.match06.setFont(QFont('Helvetica',22))
        self.match06.setEditable(False)
        self.match06.setFixedSize(100,75)
        self.match06.setStyleSheet("margin: 10px; padding: 10px; \
                                 background-color: \
                                 rgba(150,150,250,155);\
                                 color: rgba(100,0,0,255); \
                                 border-style: solid; \
                                 border-radius: 15px; \
                                 border-width: 1px; \
                                 border-color: \
                                 rgba(255,255,155,255);")
        self.matchLayoutBlanks.addWidget(self.match06)
        self.match07 = QComboBox()
        self.match07.addItems(["a","b","c","d","e","f","g",\
        "h","i","j","k","l","m"])
        self.match07.setFont(QFont('Helvetica',22))
        self.match07.setEditable(False)
        self.match07.setFixedSize(100,75)
        self.match07.setStyleSheet("margin: 10px; padding: 10px; \
                                 background-color: \
                                 rgba(150,150,250,155);\
                                 color: rgba(100,0,0,255); \
                                 border-style: solid; \
                                 border-radius: 15px; \
                                 border-width: 1px; \
                                 border-color: \
                                 rgba(255,255,155,255);")
        self.matchLayoutBlanks.addWidget(self.match07)
        self.match08 = QComboBox()
        self.match08.addItems(["a","b","c","d","e","f","g",\
        "h","i","j","k","l","m"])
        self.match08.setFont(QFont('Helvetica',22))
        self.match08.setEditable(False)
        self.match08.setFixedSize(100,75)
        self.match08.setStyleSheet("margin: 10px; padding: 10px; \
                                 background-color: \
                                 rgba(150,150,250,155);\
                                 color: rgba(100,0,0,255); \
                                 border-style: solid; \
                                 border-radius: 15px; \
                                 border-width: 1px; \
                                 border-color: \
                                 rgba(255,255,155,255);")
        self.matchLayoutBlanks.addWidget(self.match08)
        self.match09 = QComboBox()
        self.match09.addItems(["a","b","c","d","e","f","g",\
        "h","i","j","k","l","m"])
        self.match09.setFont(QFont('Helvetica',22))
        self.match09.setEditable(False)
        self.match09.setFixedSize(100,75)
        self.match09.setStyleSheet("margin: 10px; padding: 10px; \
                                 background-color: \
                                 rgba(150,150,250,155);\
                                 color: rgba(100,0,0,255); \
                                 border-style: solid; \
                                 border-radius: 15px; \
                                 border-width: 1px; \
                                 border-color: \
                                 rgba(255,255,155,255);")
        self.matchLayoutBlanks.addWidget(self.match09)

        # create the items

        self.item00 = QLabel(u"a. a\u0300-rai อะไร")
        self.item00.setFont(QFont('Helvetica',24))
        self.matchLayoutItems.addWidget(self.item00)
        self.item01 = QLabel(u"b. bpa\u0300akgaa ปากกา")
        self.item01.setFont(QFont('Helvetica',24))
        self.matchLayoutItems.addWidget(self.item01)
        self.item02 = QLabel(u"c. ni\u0302i นี่")
        self.item02.setFont(QFont('Helvetica',24))
        self.matchLayoutItems.addWidget(self.item02)
        self.item03 = QLabel(u"d. di\u0300-cha\u030Cn ดิฉัน")
        self.item03.setFont(QFont('Helvetica',24))
        self.matchLayoutItems.addWidget(self.item03)
        self.item04 = QLabel(u"e. naa-li\u0301-gaa นาฬีกา")
        self.item04.setFont(QFont('Helvetica',24))
        self.matchLayoutItems.addWidget(self.item04)
        self.item05 = QLabel(u"f. na\u0302n นั่น")
        self.item05.setFont(QFont('Helvetica',24))
        self.matchLayoutItems.addWidget(self.item05)
        self.item06 = QLabel(u"g. po\u030Cm ผม")
        self.item06.setFont(QFont('Helvetica',24))
        self.matchLayoutItems.addWidget(self.item06)
        self.item07 = QLabel(u"h. chu\u0302\u0330u\u0330 ชื่อ")
        self.item07.setFont(QFont('Helvetica',24))
        self.matchLayoutItems.addWidget(self.item07)
        self.item08 = QLabel(u"i. gra\u0300-bpa\u030Co กระเป๋า")
        self.item08.setFont(QFont('Helvetica',24))
        self.matchLayoutItems.addWidget(self.item08)
        self.item09 = QLabel(u"j. na\u030Cngsu\u0302\u0330u\u0330 หนังสือ")
        self.item09.setFont(QFont('Helvetica',24))
        self.matchLayoutItems.addWidget(self.item09)
        self.item10 = QLabel(u"k. p\u0395\u030C\u0395nti\u0302i แผนที่ ")
        self.item10.setFont(QFont('Helvetica',24))
        self.matchLayoutItems.addWidget(self.item10)
        self.item11 = QLabel(u"l. g\u2184\u0302\u2164 ก็")
        self.item11.setFont(QFont('Helvetica',24))
        self.matchLayoutItems.addWidget(self.item11)
        self.item12 = QLabel(u"m. sa\u0300-mu\u0300t สมูด")
        self.item12.setFont(QFont('Helvetica',24))
        self.matchLayoutItems.addWidget(self.item12)


        # add blank and numbering layouts together
        # and set the spacing/alignment
        self.matchBlankLayout.addLayout(self.matchLayoutBlanksNums)
        self.matchBlankLayout.addLayout(self.matchLayoutBlanks)
        self.matchBlankLayout.setAlignment(Qt.AlignLeft)

        

        # add the blank and item layouts to the matchLayout
        self.matchLayout.addLayout(self.matchBlankLayout)
        self.matchLayout.addLayout(self.matchLayoutItems)

        #add matchLayout to the subwidgetLayout
        self.subwidgetLayout.addLayout(self.matchLayout)

        # create the Submit button
        self.buttonSubmit = QPushButton("Click here\nSubmit your Answers")
        self.buttonSubmit.setFont(QFont('Helvetica',16))
        self.buttonSubmit.setFixedSize(300,100)
        self.buttonSubmit.setStyleSheet("margin: 10px; padding: 10px; \
                                 background-color: \
                                 rgba(250,150,250,155);\
                                 color: rgba(100,0,0,255); \
                                 border-style: solid; \
                                 border-radius: 15px; \
                                 border-width: 1px; \
                                 border-color: \
                                 rgba(255,255,155,255);")
        self.subwidgetLayout.addWidget(self.buttonSubmit)


        # Now create the translation section of five short sentences
        
        #QLabel for translation instructions
        self.transInstruct = QLabel("Translate the following sentences into English.\
            \nUse the boxes below to type your answer.\
            \nClick on the button below to submit your answers.")
        self.transInstruct.setFont(QFont('Times',16))    

        # add this translation Instruction QLabel to the subwidget layout
        self.subwidgetLayout.addWidget(self.transInstruct)

        # make a sublayout just for the translation problems
        self.transInstructLayout = QVBoxLayout()
        # Now add in the five translation problems
        self.trans00 = QLabel(u"1. kun sa\u0300-baai dii ma\u0301i  คุณ สบาย ดี ไหม")
        self.trans00.setFont(QFont('Helvetica',18))
        self.trans00Edit = QLineEdit()
        self.trans00Edit.setFont(QFont('Helvetica',18))
        self.transInstructLayout.addWidget(self.trans00)
        self.transInstructLayout.addWidget(self.trans00Edit)

        self.trans01 = QLabel(u"2. k\u0302o-jai ma\u0301i  เข้าใจ ไหม")
        self.trans01.setFont(QFont('Helvetica',18))
        self.trans01Edit = QLineEdit()
        self.trans01Edit.setFont(QFont('Helvetica',18))
        self.transInstructLayout.addWidget(self.trans01)
        self.transInstructLayout.addWidget(self.trans01Edit)

        self.trans02 = QLabel(u"3. ni\u0302i na\u030Cngsu\u0302\u0330u\u0330-pim cha\u0302i ma\u0301i   นี่ หนังสือพิมพ์ ืทม ใช่ ไหม")
        self.trans02.setFont(QFont('Helvetica',18))
        self.trans02Edit = QLineEdit()
        self.trans02Edit.setFont(QFont('Helvetica',18))
        self.transInstructLayout.addWidget(self.trans02)
        self.transInstructLayout.addWidget(self.trans02Edit)

        self.trans03 = QLabel(u"4. kun chu\u0302\u0330u\u0330 a\u0300-rai  คุณ ชื่อ อะไร")
        self.trans03.setFont(QFont('Helvetica',18))
        self.trans03Edit = QLineEdit()
        self.trans03Edit.setFont(QFont('Helvetica',18))
        self.transInstructLayout.addWidget(self.trans03)
        self.transInstructLayout.addWidget(self.trans03Edit)

        self.trans04 = QLabel(u"5. na\u0301n p\u0395\u030C\u0395nti\u0302i r\u030C\u0330u\0330u dins\u2184\u030C\u2184   นี่ แผนที่ หรือ ดินสอ")
        self.trans04.setFont(QFont('Helvetica',18))
        self.trans04Edit = QLineEdit()
        self.trans04Edit.setFont(QFont('Helvetica',18))
        self.transInstructLayout.addWidget(self.trans04)
        self.transInstructLayout.addWidget(self.trans04Edit)

        #Now add this translation layout to subwidget layout
        self.subwidgetLayout.addLayout(self.transInstructLayout)
#############################################################
#  set the subwidget layout, add it to scroll area
#############################################################

		# set alignment for the subwidget layout
		# self.subwidgetLayout.setAlignment(Qt.AlignVCenter)

		# set spacing for columns
		# self.subwidgetLayout.setSpacing(60)

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
