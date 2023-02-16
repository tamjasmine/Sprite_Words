# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resource_rc
import pyaudio

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(1000, 500)
        MainWindow.setMinimumSize(QSize(1000, 500))
        font = QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top_bar = QFrame(self.centralwidget)
        self.frame_top_bar.setObjectName(u"frame_top_bar")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_top_bar.sizePolicy().hasHeightForWidth())
        self.frame_top_bar.setSizePolicy(sizePolicy)
        self.frame_top_bar.setMaximumSize(QSize(16777215, 40))
        self.frame_top_bar.setStyleSheet(u"background-color: rgb(255, 127, 39)")
        self.frame_top_bar.setFrameShape(QFrame.NoFrame)
        self.frame_top_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_top_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_menu_toggle = QFrame(self.frame_top_bar)
        self.frame_menu_toggle.setObjectName(u"frame_menu_toggle")
        self.frame_menu_toggle.setMaximumSize(QSize(70, 40))
        self.frame_menu_toggle.setStyleSheet(u"background-color: rgb(255, 127, 39)")
        self.frame_menu_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_menu_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_menu_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_menu_toggle = QPushButton(self.frame_menu_toggle)
        self.btn_menu_toggle.setObjectName(u"btn_menu_toggle")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_menu_toggle.sizePolicy().hasHeightForWidth())
        self.btn_menu_toggle.setSizePolicy(sizePolicy1)
        self.btn_menu_toggle.setMaximumSize(QSize(70, 16777215))
        self.btn_menu_toggle.setStyleSheet(u"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"border: 0px solid;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/menu_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu_toggle.setIcon(icon)

        self.verticalLayout_2.addWidget(self.btn_menu_toggle)


        self.horizontalLayout.addWidget(self.frame_menu_toggle)

        self.frame_top = QFrame(self.frame_top_bar)
        self.frame_top.setObjectName(u"frame_top")
        sizePolicy.setHeightForWidth(self.frame_top.sizePolicy().hasHeightForWidth())
        self.frame_top.setSizePolicy(sizePolicy)
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.frame_top_bar)

        self.Contentc = QFrame(self.centralwidget)
        self.Contentc.setObjectName(u"Contentc")
        self.Contentc.setFrameShape(QFrame.NoFrame)
        self.Contentc.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Contentc)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Contentc)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_page_1 = QPushButton(self.frame_top_menus)
        self.btn_page_1.setObjectName(u"btn_page_1")
        self.btn_page_1.setMinimumSize(QSize(0, 40))
        self.btn_page_1.setStyleSheet(u"QPushButton {\n"
"	color: rgb(99, 98, 98);\n"
"	background-color: rgb(217, 217, 217);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 171, 115);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_1)

        self.btn_page_2 = QPushButton(self.frame_top_menus)
        self.btn_page_2.setObjectName(u"btn_page_2")
        self.btn_page_2.setMinimumSize(QSize(0, 40))
        self.btn_page_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(99, 98, 98);\n"
"	background-color: rgb(217, 217, 217);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 171, 115);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_2)

        self.btn_page_3 = QPushButton(self.frame_top_menus)
        self.btn_page_3.setObjectName(u"btn_page_3")
        self.btn_page_3.setMinimumSize(QSize(0, 40))
        self.btn_page_3.setStyleSheet(u"QPushButton {\n"
"	color: rgb(99, 98, 98);\n"
"	background-color: rgb(217, 217, 217);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 171, 115);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_3)

        self.btn_page_4 = QPushButton(self.frame_top_menus)
        self.btn_page_4.setObjectName(u"btn_page_4")
        self.btn_page_4.setMinimumSize(QSize(0, 40))
        self.btn_page_4.setStyleSheet(u"QPushButton {\n"
"	color: rgb(99, 98, 98);\n"
"	background-color: rgb(217, 217, 217);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 171, 115);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_4)


        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignTop)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_8)

        self.label_username = QLabel(self.frame_left_menu)
        self.label_username.setObjectName(u"label_username")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_username.sizePolicy().hasHeightForWidth())
        self.label_username.setSizePolicy(sizePolicy2)
        self.label_username.setMinimumSize(QSize(0, 40))
        self.label_username.setStyleSheet(u"QLabel {\n"
"	color: rgb(99, 98, 98);\n"
"	background-color: rgb(217, 217, 217);\n"
"	border: 0px solid;\n"
"}")
        self.label_username.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_username)

        self.btn_log_out = QPushButton(self.frame_left_menu)
        self.btn_log_out.setObjectName(u"btn_log_out")
        self.btn_log_out.setMinimumSize(QSize(0, 40))
        self.btn_log_out.setStyleSheet(u"QPushButton {\n"
"	color: rgb(99, 98, 98);\n"
"	background-color: rgb(217, 217, 217);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 171, 115);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_log_out)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Contentc)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_7 = QVBoxLayout(self.page_1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.label_3 = QLabel(self.page_1)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)
        self.label_3.setMaximumSize(QSize(100, 100))
        self.label_3.setPixmap(QPixmap(u":/logos/images/logos/sprite_words_light_logo.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_7.addWidget(self.label_3, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_1 = QLabel(self.page_1)
        self.label_1.setObjectName(u"label_1")
        font1 = QFont()
        font1.setFamily(u"Bahnschrift SemiLight Condensed")
        font1.setPointSize(50)
        self.label_1.setFont(font1)
        self.label_1.setStyleSheet(u"color: rgb(255, 171, 115);")
        self.label_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_1)

        self.label_login_2 = QLabel(self.page_1)
        self.label_login_2.setObjectName(u"label_login_2")
        font2 = QFont()
        font2.setFamily(u"Bahnschrift SemiCondensed")
        font2.setPointSize(16)
        font2.setBold(False)
        font2.setWeight(50)
        self.label_login_2.setFont(font2)
        self.label_login_2.setStyleSheet(u"color: rgb(80, 80, 80);")

        self.verticalLayout_7.addWidget(self.label_login_2, 0, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout = QGridLayout(self.page_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 2, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_login = QLabel(self.page_2)
        self.label_login.setObjectName(u"label_login")
        self.label_login.setFont(font2)

        self.verticalLayout_10.addWidget(self.label_login)

        self.lineEdit_user = QLineEdit(self.page_2)
        self.lineEdit_user.setObjectName(u"lineEdit_user")
        self.lineEdit_user.setMinimumSize(QSize(0, 30))
        self.lineEdit_user.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setFamily(u"Bahnschrift SemiLight")
        font3.setPointSize(12)
        self.lineEdit_user.setFont(font3)
        self.lineEdit_user.setStyleSheet(u"border: 1px solid rgb(80, 80, 80);\n"
"border-radius: 5px;\n"
"")
        self.lineEdit_user.setMaxLength(10)

        self.verticalLayout_10.addWidget(self.lineEdit_user)

        self.lineEdit_password = QLineEdit(self.page_2)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setMinimumSize(QSize(0, 30))
        self.lineEdit_password.setMaximumSize(QSize(16777215, 16777215))
        font4 = QFont()
        font4.setFamily(u"Bahnschrift SemiLight")
        font4.setPointSize(12)
        font4.setStrikeOut(False)
        self.lineEdit_password.setFont(font4)
        self.lineEdit_password.setFocusPolicy(Qt.ClickFocus)
        self.lineEdit_password.setStyleSheet(u"border: 1px solid rgb(80, 80, 80);\n"
"border-radius: 5px;\n"
"")
        self.lineEdit_password.setMaxLength(10)
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.lineEdit_password.setDragEnabled(False)
        self.lineEdit_password.setReadOnly(False)

        self.verticalLayout_10.addWidget(self.lineEdit_password)

        self.btn_login = QPushButton(self.page_2)
        self.btn_login.setObjectName(u"btn_login")
        sizePolicy2.setHeightForWidth(self.btn_login.sizePolicy().hasHeightForWidth())
        self.btn_login.setSizePolicy(sizePolicy2)
        self.btn_login.setMinimumSize(QSize(0, 30))
        self.btn_login.setMaximumSize(QSize(16777215, 16777215))
        font5 = QFont()
        font5.setFamily(u"Bahnschrift SemiLight")
        font5.setPointSize(12)
        font5.setStyleStrategy(QFont.PreferDefault)
        self.btn_login.setFont(font5)
        self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_login.setFocusPolicy(Qt.StrongFocus)
        self.btn_login.setStyleSheet(u"QPushButton {\n"
"	color:  rgb(255, 255, 255);\n"
"\n"
"	border-radius: 5px;\n"
"	border: 1px solid rgb(255, 127, 39);\n"
"	background-color: rgb(255, 171, 115);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 1px solid rgb(255, 127, 39);\n"
"	background-color: rgb(255, 127, 39);\n"
"}\n"
"")
        self.btn_login.setAutoDefault(True)
        self.btn_login.setFlat(False)

        self.verticalLayout_10.addWidget(self.btn_login)

        self.label_message = QLabel(self.page_2)
        self.label_message.setObjectName(u"label_message")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_message.sizePolicy().hasHeightForWidth())
        self.label_message.setSizePolicy(sizePolicy4)
        self.label_message.setMinimumSize(QSize(0, 30))
        font6 = QFont()
        font6.setFamily(u"Bahnschrift Light SemiCondensed")
        font6.setPointSize(12)
        self.label_message.setFont(font6)
        self.label_message.setStyleSheet(u"color: rgb(255, 69, 69);")

        self.verticalLayout_10.addWidget(self.label_message)


        self.horizontalLayout_4.addLayout(self.verticalLayout_10)


        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.horizontalLayout_7 = QHBoxLayout(self.page_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_record = QLabel(self.page_3)
        self.label_record.setObjectName(u"label_record")
        sizePolicy.setHeightForWidth(self.label_record.sizePolicy().hasHeightForWidth())
        self.label_record.setSizePolicy(sizePolicy)
        font7 = QFont()
        font7.setFamily(u"Bahnschrift SemiLight Condensed")
        font7.setPointSize(16)
        self.label_record.setFont(font7)
        self.label_record.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_record)

        self.label_audio_tracks = QLabel(self.page_3)
        self.label_audio_tracks.setObjectName(u"label_audio_tracks")
        sizePolicy.setHeightForWidth(self.label_audio_tracks.sizePolicy().hasHeightForWidth())
        self.label_audio_tracks.setSizePolicy(sizePolicy)
        self.label_audio_tracks.setFont(font6)

        self.verticalLayout_6.addWidget(self.label_audio_tracks)

        self.line = QFrame(self.page_3)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_7 = QLabel(self.page_3)
        self.label_7.setObjectName(u"label_7")
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)
        self.label_7.setMinimumSize(QSize(90, 0))
        self.label_7.setFont(font6)

        self.horizontalLayout_14.addWidget(self.label_7)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_astronaut = QLabel(self.page_3)
        self.label_astronaut.setObjectName(u"label_astronaut")
        sizePolicy3.setHeightForWidth(self.label_astronaut.sizePolicy().hasHeightForWidth())
        self.label_astronaut.setSizePolicy(sizePolicy3)
        self.label_astronaut.setMaximumSize(QSize(30, 30))
        self.label_astronaut.setPixmap(QPixmap(u":/icons/images/icons/astronaut_icon.png"))
        self.label_astronaut.setScaledContents(True)

        self.horizontalLayout_15.addWidget(self.label_astronaut)

        self.btn_record_1 = QPushButton(self.page_3)
        self.btn_record_1.setObjectName(u"btn_record_1")
        sizePolicy2.setHeightForWidth(self.btn_record_1.sizePolicy().hasHeightForWidth())
        self.btn_record_1.setSizePolicy(sizePolicy2)
        self.btn_record_1.setMinimumSize(QSize(30, 30))
        self.btn_record_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_record_1.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(217, 217, 217);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/record_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_record_1.setIcon(icon1)

        self.horizontalLayout_15.addWidget(self.btn_record_1)

        self.btn_play_audio_1 = QPushButton(self.page_3)
        self.btn_play_audio_1.setObjectName(u"btn_play_audio_1")
        self.btn_play_audio_1.setMinimumSize(QSize(30, 30))
        self.btn_play_audio_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_play_audio_1.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(217, 217, 217);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/play_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_play_audio_1.setIcon(icon2)

        self.horizontalLayout_15.addWidget(self.btn_play_audio_1)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_15)


        self.verticalLayout_6.addLayout(self.horizontalLayout_14)

        self.line_2 = QFrame(self.page_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line_2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_6 = QLabel(self.page_3)
        self.label_6.setObjectName(u"label_6")
        sizePolicy3.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy3)
        self.label_6.setMinimumSize(QSize(90, 0))
        self.label_6.setFont(font6)

        self.horizontalLayout_8.addWidget(self.label_6)

        self.label_17 = QLabel(self.page_3)
        self.label_17.setObjectName(u"label_17")
        sizePolicy3.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy3)
        self.label_17.setMaximumSize(QSize(30, 30))
        self.label_17.setPixmap(QPixmap(u":/icons/images/icons/bicycle_icon.png"))
        self.label_17.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.label_17)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.btn_record_2 = QPushButton(self.page_3)
        self.btn_record_2.setObjectName(u"btn_record_2")
        sizePolicy2.setHeightForWidth(self.btn_record_2.sizePolicy().hasHeightForWidth())
        self.btn_record_2.setSizePolicy(sizePolicy2)
        self.btn_record_2.setMinimumSize(QSize(30, 30))
        self.btn_record_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_record_2.setIcon(icon1)

        self.horizontalLayout_9.addWidget(self.btn_record_2)

        self.btn_play_audio_2 = QPushButton(self.page_3)
        self.btn_play_audio_2.setObjectName(u"btn_play_audio_2")
        self.btn_play_audio_2.setMinimumSize(QSize(30, 30))
        self.btn_play_audio_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_play_audio_2.setIcon(icon2)

        self.horizontalLayout_9.addWidget(self.btn_play_audio_2)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_9)


        self.verticalLayout_6.addLayout(self.horizontalLayout_8)

        self.line_3 = QFrame(self.page_3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line_3)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_8 = QLabel(self.page_3)
        self.label_8.setObjectName(u"label_8")
        sizePolicy3.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy3)
        self.label_8.setMinimumSize(QSize(90, 0))
        self.label_8.setFont(font6)

        self.horizontalLayout_12.addWidget(self.label_8)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_cemetery = QLabel(self.page_3)
        self.label_cemetery.setObjectName(u"label_cemetery")
        sizePolicy3.setHeightForWidth(self.label_cemetery.sizePolicy().hasHeightForWidth())
        self.label_cemetery.setSizePolicy(sizePolicy3)
        self.label_cemetery.setMaximumSize(QSize(30, 30))
        self.label_cemetery.setPixmap(QPixmap(u":/icons/images/icons/cemetery_icon.png"))
        self.label_cemetery.setScaledContents(True)

        self.horizontalLayout_13.addWidget(self.label_cemetery)

        self.btn_record_3 = QPushButton(self.page_3)
        self.btn_record_3.setObjectName(u"btn_record_3")
        sizePolicy2.setHeightForWidth(self.btn_record_3.sizePolicy().hasHeightForWidth())
        self.btn_record_3.setSizePolicy(sizePolicy2)
        self.btn_record_3.setMinimumSize(QSize(30, 30))
        self.btn_record_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_record_3.setStyleSheet(u"")
        self.btn_record_3.setIcon(icon1)

        self.horizontalLayout_13.addWidget(self.btn_record_3)

        self.btn_play_audio_3 = QPushButton(self.page_3)
        self.btn_play_audio_3.setObjectName(u"btn_play_audio_3")
        self.btn_play_audio_3.setMinimumSize(QSize(30, 30))
        self.btn_play_audio_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_play_audio_3.setIcon(icon2)

        self.horizontalLayout_13.addWidget(self.btn_play_audio_3)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_13)


        self.verticalLayout_6.addLayout(self.horizontalLayout_12)

        self.line_4 = QFrame(self.page_3)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line_4)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_5 = QLabel(self.page_3)
        self.label_5.setObjectName(u"label_5")
        sizePolicy3.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy3)
        self.label_5.setMinimumSize(QSize(90, 0))
        self.label_5.setFont(font6)

        self.horizontalLayout_10.addWidget(self.label_5)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_eraser = QLabel(self.page_3)
        self.label_eraser.setObjectName(u"label_eraser")
        sizePolicy3.setHeightForWidth(self.label_eraser.sizePolicy().hasHeightForWidth())
        self.label_eraser.setSizePolicy(sizePolicy3)
        self.label_eraser.setMaximumSize(QSize(30, 30))
        self.label_eraser.setPixmap(QPixmap(u":/icons/images/icons/eraser_icon.png"))
        self.label_eraser.setScaledContents(True)

        self.horizontalLayout_11.addWidget(self.label_eraser)

        self.btn_record_4 = QPushButton(self.page_3)
        self.btn_record_4.setObjectName(u"btn_record_4")
        sizePolicy2.setHeightForWidth(self.btn_record_4.sizePolicy().hasHeightForWidth())
        self.btn_record_4.setSizePolicy(sizePolicy2)
        self.btn_record_4.setMinimumSize(QSize(30, 30))
        self.btn_record_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_record_4.setStyleSheet(u"")
        self.btn_record_4.setIcon(icon1)

        self.horizontalLayout_11.addWidget(self.btn_record_4)

        self.btn_play_audio_4 = QPushButton(self.page_3)
        self.btn_play_audio_4.setObjectName(u"btn_play_audio_4")
        self.btn_play_audio_4.setMinimumSize(QSize(30, 30))
        self.btn_play_audio_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_play_audio_4.setIcon(icon2)

        self.horizontalLayout_11.addWidget(self.btn_play_audio_4)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_11)


        self.verticalLayout_6.addLayout(self.horizontalLayout_10)

        self.line_5 = QFrame(self.page_3)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.page_3)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)
        self.label_4.setMinimumSize(QSize(90, 0))
        self.label_4.setFont(font6)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_21 = QLabel(self.page_3)
        self.label_21.setObjectName(u"label_21")
        sizePolicy3.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy3)
        self.label_21.setMaximumSize(QSize(30, 30))
        self.label_21.setPixmap(QPixmap(u":/icons/images/icons/scissors_icon.png"))
        self.label_21.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_21)

        self.btn_record_5 = QPushButton(self.page_3)
        self.btn_record_5.setObjectName(u"btn_record_5")
        sizePolicy2.setHeightForWidth(self.btn_record_5.sizePolicy().hasHeightForWidth())
        self.btn_record_5.setSizePolicy(sizePolicy2)
        self.btn_record_5.setMinimumSize(QSize(30, 30))
        self.btn_record_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_record_5.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_record_5)

        self.btn_play_audio_5 = QPushButton(self.page_3)
        self.btn_play_audio_5.setObjectName(u"btn_play_audio_5")
        self.btn_play_audio_5.setMinimumSize(QSize(30, 30))
        self.btn_play_audio_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_play_audio_5.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_play_audio_5)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_5)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.line_6 = QFrame(self.page_3)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line_6)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_9 = QLabel(self.page_3)
        self.label_9.setObjectName(u"label_9")
        sizePolicy3.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy3)
        self.label_9.setMinimumSize(QSize(90, 0))
        self.label_9.setFont(font6)

        self.horizontalLayout_16.addWidget(self.label_9)

        self.label_20 = QLabel(self.page_3)
        self.label_20.setObjectName(u"label_20")
        sizePolicy3.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy3)
        self.label_20.setMaximumSize(QSize(30, 30))
        self.label_20.setPixmap(QPixmap(u":/icons/images/icons/squirrel_icon.png"))
        self.label_20.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.label_20)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.btn_record_6 = QPushButton(self.page_3)
        self.btn_record_6.setObjectName(u"btn_record_6")
        sizePolicy2.setHeightForWidth(self.btn_record_6.sizePolicy().hasHeightForWidth())
        self.btn_record_6.setSizePolicy(sizePolicy2)
        self.btn_record_6.setMinimumSize(QSize(30, 30))
        self.btn_record_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_record_6.setStyleSheet(u"")
        self.btn_record_6.setIcon(icon1)

        self.horizontalLayout_17.addWidget(self.btn_record_6)

        self.btn_play_audio_6 = QPushButton(self.page_3)
        self.btn_play_audio_6.setObjectName(u"btn_play_audio_6")
        self.btn_play_audio_6.setMinimumSize(QSize(30, 30))
        self.btn_play_audio_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_play_audio_6.setIcon(icon2)

        self.horizontalLayout_17.addWidget(self.btn_play_audio_6)


        self.horizontalLayout_16.addLayout(self.horizontalLayout_17)


        self.verticalLayout_6.addLayout(self.horizontalLayout_16)

        self.line_7 = QFrame(self.page_3)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line_7)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_audio_input = QLabel(self.page_3)
        self.label_audio_input.setObjectName(u"label_audio_input")
        sizePolicy.setHeightForWidth(self.label_audio_input.sizePolicy().hasHeightForWidth())
        self.label_audio_input.setSizePolicy(sizePolicy)
        self.label_audio_input.setFont(font6)

        self.horizontalLayout_19.addWidget(self.label_audio_input)

        self.comboBox_audio_input = QComboBox(self.page_3)
        self.comboBox_audio_input.setObjectName(u"comboBox_audio_input")
        sizePolicy2.setHeightForWidth(self.comboBox_audio_input.sizePolicy().hasHeightForWidth())
        self.comboBox_audio_input.setSizePolicy(sizePolicy2)
        self.comboBox_audio_input.setMinimumSize(QSize(30, 30))

        self.horizontalLayout_19.addWidget(self.comboBox_audio_input)

        
        audio = pyaudio.PyAudio()
        global audioInputDevices
        audioInputDevices = []
        info = audio.get_host_api_info_by_index(0)

        numdevices = info.get('deviceCount')
        # Add each audio input device to combo box
        for i in range(0, numdevices):
                self.comboBox_audio_input.setCurrentText(str(0))
                if (audio.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
                        self.comboBox_audio_input.addItem(audio.get_device_info_by_host_api_device_index(0, i).get('name'))

        self.verticalLayout_6.addLayout(self.horizontalLayout_19)

        self.line_8 = QFrame(self.page_3)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line_8)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)


        self.horizontalLayout_6.addLayout(self.verticalLayout_6)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.horizontalLayout_20 = QHBoxLayout(self.page_4)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_9)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_about = QLabel(self.page_4)
        self.label_about.setObjectName(u"label_about")
        sizePolicy3.setHeightForWidth(self.label_about.sizePolicy().hasHeightForWidth())
        self.label_about.setSizePolicy(sizePolicy3)
        self.label_about.setFont(font7)
        self.label_about.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_about, 0, Qt.AlignHCenter)

        self.label_about1 = QLabel(self.page_4)
        self.label_about1.setObjectName(u"label_about1")
        sizePolicy3.setHeightForWidth(self.label_about1.sizePolicy().hasHeightForWidth())
        self.label_about1.setSizePolicy(sizePolicy3)
        self.label_about1.setMinimumSize(QSize(90, 0))
        self.label_about1.setFont(font6)
        self.label_about1.setAlignment(Qt.AlignCenter)
        self.label_about1.setOpenExternalLinks(False)

        self.verticalLayout_12.addWidget(self.label_about1, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_about2 = QLabel(self.page_4)
        self.label_about2.setObjectName(u"label_about2")
        sizePolicy3.setHeightForWidth(self.label_about2.sizePolicy().hasHeightForWidth())
        self.label_about2.setSizePolicy(sizePolicy3)
        self.label_about2.setMinimumSize(QSize(90, 0))
        self.label_about2.setFont(font6)
        self.label_about2.setOpenExternalLinks(False)

        self.verticalLayout_12.addWidget(self.label_about2, 0, Qt.AlignHCenter)


        self.verticalLayout_9.addLayout(self.verticalLayout_12)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_9.addItem(self.verticalSpacer_7)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_support = QLabel(self.page_4)
        self.label_support.setObjectName(u"label_support")
        sizePolicy3.setHeightForWidth(self.label_support.sizePolicy().hasHeightForWidth())
        self.label_support.setSizePolicy(sizePolicy3)
        self.label_support.setFont(font7)
        self.label_support.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_support, 0, Qt.AlignHCenter)

        self.label_support1 = QLabel(self.page_4)
        self.label_support1.setObjectName(u"label_support1")
        sizePolicy3.setHeightForWidth(self.label_support1.sizePolicy().hasHeightForWidth())
        self.label_support1.setSizePolicy(sizePolicy3)
        self.label_support1.setMinimumSize(QSize(90, 0))
        self.label_support1.setFont(font6)
        self.label_support1.setAlignment(Qt.AlignCenter)
        self.label_support1.setOpenExternalLinks(False)

        self.verticalLayout_16.addWidget(self.label_support1, 0, Qt.AlignHCenter)

        self.label_support2 = QLabel(self.page_4)
        self.label_support2.setObjectName(u"label_support2")
        sizePolicy3.setHeightForWidth(self.label_support2.sizePolicy().hasHeightForWidth())
        self.label_support2.setSizePolicy(sizePolicy3)
        self.label_support2.setMinimumSize(QSize(90, 0))
        self.label_support2.setFont(font6)
        self.label_support2.setOpenExternalLinks(True)

        self.verticalLayout_16.addWidget(self.label_support2, 0, Qt.AlignHCenter)


        self.verticalLayout_9.addLayout(self.verticalLayout_16)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_9.addItem(self.verticalSpacer_6)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_project = QLabel(self.page_4)
        self.label_project.setObjectName(u"label_project")
        sizePolicy3.setHeightForWidth(self.label_project.sizePolicy().hasHeightForWidth())
        self.label_project.setSizePolicy(sizePolicy3)
        self.label_project.setFont(font7)
        self.label_project.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_project, 0, Qt.AlignHCenter)

        self.label_project1 = QLabel(self.page_4)
        self.label_project1.setObjectName(u"label_project1")
        sizePolicy3.setHeightForWidth(self.label_project1.sizePolicy().hasHeightForWidth())
        self.label_project1.setSizePolicy(sizePolicy3)
        self.label_project1.setMinimumSize(QSize(90, 0))
        self.label_project1.setFont(font6)
        self.label_project1.setStyleSheet(u"link = QLabel('<a href=\"http://zetcode.com\">zetcode.com</a>')\n"
"link.setOpenExternalLinks(True)")
        self.label_project1.setOpenExternalLinks(True)

        self.verticalLayout_11.addWidget(self.label_project1, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_10)


        self.verticalLayout_9.addLayout(self.verticalLayout_11)


        self.horizontalLayout_18.addLayout(self.verticalLayout_9)


        self.horizontalLayout_20.addLayout(self.horizontalLayout_18)

        self.stackedWidget.addWidget(self.page_4)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Contentc)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)
        self.btn_login.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(accessibility)
        MainWindow.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.btn_menu_toggle.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.btn_page_1.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_page_2.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.btn_page_3.setText(QCoreApplication.translate("MainWindow", u"Record", None))
        self.btn_page_4.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.label_username.setText("")
        self.btn_log_out.setText(QCoreApplication.translate("MainWindow", u"Log out", None))
        self.label_3.setText("")
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"SPRITE WORDS", None))
        self.label_login_2.setText(QCoreApplication.translate("MainWindow", u"Record and play audio", None))
        self.label_login.setText(QCoreApplication.translate("MainWindow", u"Log in to your account", None))
        self.lineEdit_user.setText("")
        self.lineEdit_user.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Username", None))
        self.lineEdit_password.setInputMask("")
        self.lineEdit_password.setText("")
        self.lineEdit_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Password", None))
        self.btn_login.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.label_message.setText("")
        self.label_record.setText(QCoreApplication.translate("MainWindow", u"Record", None))
        self.label_audio_tracks.setText(QCoreApplication.translate("MainWindow", u"Audio Tracks:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Astronaut", None))
        self.label_astronaut.setText("")
#if QT_CONFIG(tooltip)
        self.btn_record_1.setToolTip(QCoreApplication.translate("MainWindow", u"Record Audio", None))
#endif // QT_CONFIG(tooltip)
        self.btn_record_1.setText("")
#if QT_CONFIG(tooltip)
        self.btn_play_audio_1.setToolTip(QCoreApplication.translate("MainWindow", u"Play Audio", None))
#endif // QT_CONFIG(tooltip)
        self.btn_play_audio_1.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Bicycle", None))
        self.label_17.setText("")
#if QT_CONFIG(tooltip)
        self.btn_record_2.setToolTip(QCoreApplication.translate("MainWindow", u"Record Audio", None))
#endif // QT_CONFIG(tooltip)
        self.btn_record_2.setText("")
#if QT_CONFIG(tooltip)
        self.btn_play_audio_2.setToolTip(QCoreApplication.translate("MainWindow", u"Play Audio", None))
#endif // QT_CONFIG(tooltip)
        self.btn_play_audio_2.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Cemetery", None))
        self.label_cemetery.setText("")
#if QT_CONFIG(tooltip)
        self.btn_record_3.setToolTip(QCoreApplication.translate("MainWindow", u"Record Audio", None))
#endif // QT_CONFIG(tooltip)
        self.btn_record_3.setText("")
#if QT_CONFIG(tooltip)
        self.btn_play_audio_3.setToolTip(QCoreApplication.translate("MainWindow", u"Play Audio", None))
#endif // QT_CONFIG(tooltip)
        self.btn_play_audio_3.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Eraser", None))
        self.label_eraser.setText("")
#if QT_CONFIG(tooltip)
        self.btn_record_4.setToolTip(QCoreApplication.translate("MainWindow", u"Record Audio", None))
#endif // QT_CONFIG(tooltip)
        self.btn_record_4.setText("")
#if QT_CONFIG(tooltip)
        self.btn_play_audio_4.setToolTip(QCoreApplication.translate("MainWindow", u"Play Audio", None))
#endif // QT_CONFIG(tooltip)
        self.btn_play_audio_4.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Scissors", None))
        self.label_21.setText("")
#if QT_CONFIG(tooltip)
        self.btn_record_5.setToolTip(QCoreApplication.translate("MainWindow", u"Record Audio", None))
#endif // QT_CONFIG(tooltip)
        self.btn_record_5.setText("")
#if QT_CONFIG(tooltip)
        self.btn_play_audio_5.setToolTip(QCoreApplication.translate("MainWindow", u"Play Audio", None))
#endif // QT_CONFIG(tooltip)
        self.btn_play_audio_5.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Squirrel", None))
        self.label_20.setText("")
#if QT_CONFIG(tooltip)
        self.btn_record_6.setToolTip(QCoreApplication.translate("MainWindow", u"Record Audio", None))
#endif // QT_CONFIG(tooltip)
        self.btn_record_6.setText("")
#if QT_CONFIG(tooltip)
        self.btn_play_audio_6.setToolTip(QCoreApplication.translate("MainWindow", u"Play Audio", None))
#endif // QT_CONFIG(tooltip)
        self.btn_play_audio_6.setText("")
        self.label_audio_input.setText(QCoreApplication.translate("MainWindow", u"Audio Input:", None))
        self.label_about.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.label_about1.setText(QCoreApplication.translate("MainWindow", u"By Jasmine Tam", None))
        self.label_about2.setText(QCoreApplication.translate("MainWindow", u"Sprite Words is program built using Python.", None))
        self.label_support.setText(QCoreApplication.translate("MainWindow", u"Support", None))
        self.label_support1.setText(QCoreApplication.translate("MainWindow", u"jasminetam1@icloud.com", None))
        self.label_support2.setText(QCoreApplication.translate("MainWindow", u"https://github.com/tamjasmine", None))
        self.label_project.setText(QCoreApplication.translate("MainWindow", u"Project", None))
        self.label_project1.setText(QCoreApplication.translate("MainWindow", u"https://github.com/tamjasmine/Sprite_Words\n"
"", None))
    # retranslateUi

