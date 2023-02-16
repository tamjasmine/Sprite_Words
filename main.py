import PyQt5.sip

# -------------------------------------------------------------------- #
#                             Sprite Words                             #
#                  A program to play and record audio                  #
# -------------------------------------------------------------------- #
# Developed by Jasmine Tam                                             #
# Made with Python 3                                                   #
# Released on June 24, 2022                                            #
# -------------------------------------------------------------------- #

# ------------------------------ IMPORTS ------------------------------ #
# PYTHON MODULES
import os
import csv
import hashlib
import importlib
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation)

from PySide2.QtWidgets import *

# GUI FILE
from ui_main import Ui_MainWindow

# FUNCTIONS FILE
from ui_functions import *

# RESOURCES FILE
import resource_rc


# ------------------------------ CLASSES ------------------------------ #
class MainWindow(QMainWindow):
    # ------------------------------ FUNCTIONS ------------------------------ #
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # MENU TOGGLE
        self.ui.btn_menu_toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))

        # ------------------------------ PAGES ------------------------------ #
        # SET PAGE
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_1)
        # ---------------------------------------
        # PAGE 1 - HOME
        self.ui.btn_page_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))
        # ---------------------------------------
        # PAGE 2 - LOGIN
        self.ui.btn_page_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        # ---------------------------------------
        # PAGE 3 - RECORD
        # --------------- BUTTONS --------------- #
        self.ui.btn_page_3.hide()
        self.ui.btn_log_out.hide()
        self.ui.comboBox_audio_input.activated.connect(self.button_click_input_device)

        # LOGIN BUTTON
        self.ui.btn_login.clicked.connect(self.button_click_login)

        # RECORD PAGE BUTTONS
        self.ui.btn_record_1.clicked.connect(self.button_click_record)
        self.ui.btn_record_2.clicked.connect(self.button_click_record)
        self.ui.btn_record_3.clicked.connect(self.button_click_record)
        self.ui.btn_record_4.clicked.connect(self.button_click_record)
        self.ui.btn_record_5.clicked.connect(self.button_click_record)
        self.ui.btn_record_6.clicked.connect(self.button_click_record)

        # PLAY AUDIO BUTTONS
        self.ui.btn_play_audio_1.clicked.connect(self.button_click_play)
        self.ui.btn_play_audio_2.clicked.connect(self.button_click_play)
        self.ui.btn_play_audio_3.clicked.connect(self.button_click_play)
        self.ui.btn_play_audio_4.clicked.connect(self.button_click_play)
        self.ui.btn_play_audio_5.clicked.connect(self.button_click_play)
        self.ui.btn_play_audio_6.clicked.connect(self.button_click_play)
        # ---------------------------------------
        # PAGE 4 - ABOUT
        self.ui.btn_page_4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_4))

        self.show() # Show main window

    # ------------------------------------------------------------
    def button_click_input_device(self):
        """
        Button click for selecting the audio input device
        """
        # Loop through audio input devices
        for i in range(self.ui.comboBox_audio_input.count()):
            # Index of the audio input device selected
            if self.ui.comboBox_audio_input.currentIndex() == i:
                with open("vardata.txt", "r") as file:
                    audio_device_index = file.readlines()
                    audio_device_index[0] = str(i) + "\n"
                    with open("vardata.txt", "w") as file:
                        # Write the new index to the txt file
                        file.writelines(audio_device_index)

    # ------------------------------------------------------------
    def button_click_record(self):

        # Check the value of index 1 of vardatac 
        with open("vardata.txt", "r") as file:
            text = file.readlines()
            global check_reload
            check_reload = text[1]
        # ---------------------------------------
        # Get the object name that triggered the button_click_record event
        sending_record_button = self.sender()
        if sending_record_button == self.ui.btn_record_1:
            if int(check_reload) == 0:
                from audiorecord import record_audio_1
                with open("vardata.txt", "r") as file:
                    text = file.readlines()
                    text[1] = "1\n"
                    with open("vardata.txt", "w") as file:
                        file.writelines(text)   # Write the new index to the txt file
            else:
                from audiorecord import record_audio_1
                importlib.reload(record_audio_1)
        # ---------------------------------------
        if sending_record_button == self.ui.btn_record_2:
            if int(check_reload) == 0:
                from audiorecord import record_audio_2
                with open("vardata.txt", "r") as file:
                    text = file.readlines()
                    text[1] = "1\n"
                    with open("vardata.txt", "w") as file:
                        file.writelines(text)   # Write the new index to the txt file
            else:
                from audiorecord import record_audio_2

        # ---------------------------------------
        if sending_record_button == self.ui.btn_record_3:
            if int(check_reload) == 0:
                from audiorecord import record_audio_3
                with open("vardata.txt", "r") as file:
                    text = file.readlines()
                    text[1] = "1\n"
                    with open("vardata.txt", "w") as file:
                        file.writelines(text)   # Write the new index to the txt file
            else:
                from audiorecord import record_audio_3
                importlib.reload(record_audio_3)
        # ---------------------------------------
        if sending_record_button == self.ui.btn_record_4:
            if int(check_reload) == 0:
                from audiorecord import record_audio_4
                with open("vardata.txt", "r") as file:
                    text = file.readlines()
                    text[1] = "1\n"
                    with open("vardata.txt", "w") as file:
                        # Write the new index to the txt file
                        file.writelines(text)
            else:
                from audiorecord import record_audio_4
                importlib.reload(record_audio_4)
        # ---------------------------------------
        if sending_record_button == self.ui.btn_record_5:
            if int(check_reload) == 0:
                from audiorecord import record_audio_5
                with open("vardata.txt", "r") as file:
                    text = file.readlines()
                    text[1] = "1\n"
                    with open("vardata.txt", "w") as file:
                        file.writelines(text)   # Write the new index to the txt file
            else:
                from audiorecord import record_audio_5
                importlib.reload(record_audio_5)
        # ---------------------------------------
        if sending_record_button == self.ui.btn_record_6:
            if int(check_reload) == 0:
                from audiorecord import record_audio_6
                with open("vardata.txt", "r") as file:
                    text = file.readlines()
                    text[1] = "1\n"
                    with open("vardata.txt", "w") as file:
                        file.writelines(text)   # Write the new index to the txt file
            else:
                from audiorecord import record_audio_6
                importlib.reload(record_audio_6)

    # ------------------------------------------------------------
    def button_click_play(self):
        """
        Play button click
        """
        # Check the value of index 1 of vardatac 
        with open("vardata.txt", "r") as file:
            text = file.readlines()
            global check_play_reload
            check_play_reload = text[2]
        # ---------------------------------------
        # Get the object name that triggered the button_click_play event
        sending_play_button = self.sender()
        if sending_play_button == self.ui.btn_play_audio_1:
            if int(check_play_reload) == 0:
                from audioplay import play_audio_1
                with open("vardata.txt", "r") as file:
                    text = file.readlines()
                    text[2] = "1\n"
                    with open("vardata.txt", "w") as file:
                        # Write the new index to the txt file
                        file.writelines(text)
            else:
                from audioplay import play_audio_1
                importlib.reload(play_audio_1)
        # ---------------------------------------
        elif sending_play_button == self.ui.btn_play_audio_2:
            if int(check_play_reload) == 0:
                from audioplay import play_audio_2
                with open("vardata.txt", "r") as file:
                    text = file.readlines()
                    text[2] = "1\n"
                    with open("vardata.txt", "w") as file:
                        # Write the new index to the txt file
                        file.writelines(text)
            else:
                from audioplay import play_audio_2
                importlib.reload(play_audio_2)
        # ---------------------------------------
        elif sending_play_button == self.ui.btn_play_audio_3:
            if int(check_play_reload) == 0:
                from audioplay import play_audio_3
                with open("vardata.txt", "r") as file:
                    text = file.readlines()
                    text[2] = "1\n"
                    with open("vardata.txt", "w") as file:
                        # Write the new index to the txt file
                        file.writelines(text)
            else:
                from audioplay import play_audio_3
                importlib.reload(play_audio_3)
        # ---------------------------------------
        elif sending_play_button == self.ui.btn_play_audio_4:
            if int(check_play_reload) == 0:
                from audioplay import play_audio_4
                with open("vardata.txt", "r") as file:
                    text = file.readlines()
                    text[2] = "1\n"
                    with open("vardata.txt", "w") as file:
                        # Write the new index to the txt file
                        file.writelines(text)
            else:
                from audioplay import play_audio_4
                importlib.reload(play_audio_4)
        # ---------------------------------------
        elif sending_play_button == self.ui.btn_play_audio_5:
            if int(check_play_reload) == 0:
                from audioplay import play_audio_5
                with open("vardata.txt", "r") as file:
                    text = file.readlines()
                    text[2] = "1\n"
                    with open("vardata.txt", "w") as file:
                        # Write the new index to the txt file
                        file.writelines(text)
            else:
                from audioplay import play_audio_5
                importlib.reload(play_audio_5)
        # ---------------------------------------
        elif sending_play_button == self.ui.btn_play_audio_6:
            if int(check_play_reload) == 0:
                from audioplay import play_audio_6
                with open("vardata.txt", "r") as file:
                    text = file.readlines()
                    text[2] = "1\n"
                    with open("vardata.txt", "w") as file:
                        # Write the new index to the txt file
                        file.writelines(text)
            else:
                from audioplay import play_audio_6
                importlib.reload(play_audio_6)

    # ------------------------------------------------------------
    def button_click_login(self):
        def encrypt_string(user_password):
            """
            This function encrypts the user's chosen password
            Args:
                user_password
                String of the user's password
            Returns:
                sha_signature
                String of the hashed password
            """

            sha_signature = hashlib.sha256(user_password.encode()).hexdigest()
            return sha_signature

        # ------------------------------------------------------------
        def accountLogin():
            # Check if the username inputted exists
            with open('user_info.csv') as csvfile:
                readCSV = csv.reader(csvfile)
                valid_user = False
                index = 0 # Set index to 0 to count row number

                # Loop through usernames in user_info.csv to see if there is a match
                for row in readCSV:
                    # Add 1 to index every time it passes through a row
                    index+= 1
                    # Valid if inputted username matches username in user_info.csv
                    if user_username == row[0]:
                        userRow = index-1
                        valid_user = True
                    # Invalid if the username is not found in user_info.csv
                if valid_user == False:
                    self.ui.label_message.setText("Username or password is invalid.")
                    # Exit function
                    return

                # Encrypt the login password
                encrypt_password = encrypt_string(user_password)

                with open('user_info.csv') as csvfile:
                    readCSV = csv.reader(csvfile)
                    login_database = list(readCSV)
                    # Compare hashed login password to hash password value in user_info.csv database
                    if encrypt_password == login_database[userRow][1]:
                        # SWITCH TO PAGE 3
                        self.ui.label_username.setText(user_username)
                        self.ui.btn_page_2.hide()

                        self.ui.btn_log_out.show()
                        self.ui.btn_log_out.clicked.connect(self.button_click_log_out)
                        
                        self.ui.btn_page_3.show()
                        self.ui.btn_page_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))
                        self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)
                    # If the password is invalid
                    else:
                        self.ui.label_message.setText("Username or password is invalid.")

        # Get username and password inputted by the user
        user_username = self.ui.lineEdit_user.text()
        user_password = self.ui.lineEdit_password.text()

        # Call the function check account login
        accountLogin()

    # ------------------------------------------------------------
    def button_click_log_out(self):
        """
        tells the application to exit
        """
        QApplication.quit()


# ------------------------------ MAIN PROGRAM ------------------------------ #
if __name__ == "__main__":
    cwd = os.getcwd()  # Get the cwd (current working directory)
    
    # Set variables in vardata
    with open("vardata.txt", "r") as file:
        text = file.readlines()
        text[1] = "0\n"
        text[2] = "0\n"
        with open("vardata.txt", "w") as file:
            file.writelines(text)   # Write the new index to the txt file

    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("Sprite Words")
    window.setWindowIcon(QtGui.QIcon(u":/logos/images/logos/sprite_words_light_logo.png"))  # Set the Sprite Words logo
    
    sys.exit(app.exec_())