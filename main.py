 

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog, QStatusBar, QToolBar, QAction, QWidget, QPushButton
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QDir, Qt, QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer, QMediaPlaylist
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QMainWindow, QWidget, QPushButton, QApplication,
                             QLabel, QFileDialog, QStyle, QVBoxLayout)
import sys
import os
from click import open_file
import pygame
import design
from mutagen.mp3 import MP3 
from pypresence import Presence
import datetime
from PyQt5.QtCore import QUrl, QTime, QTimer, QDir
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from translate import Translator
pygame.init()
pygame.mixer.init()
time = QTime.currentTime()
minute = time.hour()
hour = time.minute()








main_folder = os.getcwd()
calculator_icon_png = os.path.join(main_folder,"elements\icons","calculator.png")
headphones_on_icon_png = os.path.join(main_folder,"elements\icons","HeadPhones.png")
headphones_off_icon_png = os.path.join(main_folder,"elements\icons","HeadPhones_off.png")
music_icon_png = os.path.join(main_folder,"elements\icons","music_icon.png")
volume_player_off_icon_png = os.path.join(main_folder,"elements\icons","volume_player_off.png")
volume_player_on_icon_png = os.path.join(main_folder,"elements\icons","volume_player_on.png")
reapeat_icon_png = os.path.join(main_folder,"elements\icons","repeat.png")
shuffle_icon_png = os.path.join(main_folder,"elements\icons","shuffle.png")
library_import_icon_png = os.path.join(main_folder,"elements\icons","library_plus.png")




class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(1200, 711)
        global track_filename
        track_filename = ""
        global dirlisted
        dirlisted = ""
        global photo_path
        photo_path = ""
        self.allow_play_files = False

        self.alarm_sound = "elements\\sfx\\default_alarm.mp3"
        self.frame_10.hide()
        self.frame_9.hide()
        self.second_list_enable = True
        self.dict_alarm = {}
        time = QTime.currentTime()
        hour = time.hour()
        minute = time.minute()
        if len(str(minute)) == 1:
            minute = "0"+str(minute)
        if len(str(hour)) == 1:
            hour = "0"+str(hour)

        text_label_8 =f'''{hour}:{minute}'''

        self.label_8.setText(text_label_8)

        self.STOPPED_PLAYING = pygame.USEREVENT + 1

        pygame.mixer.music.set_endevent(self.STOPPED_PLAYING)

        self.track_play = ""

        global track
        track = ""
        today = datetime.datetime.today()
        today = today.strftime("%d/%m/%Y")


        self.label_9.setText(today)
        self.frame_7.move(5,5)

        #hide apps
        self.frame_2.hide()
        self.frame_3.hide()
        self.frame_4.hide()
        self.frame_6.hide()
        self.frame.hide()
        self.frame_5.hide()
        self.frame_8.hide()
        self.frame_7.hide()
        #statuses
        self.browser_enable = False
        self.volume_gui = 0
        self.mutestatus = False
        self.textnote_enable = False
        self.calculator_enable = False
        self.audio_player_enable = False
        self.change_pos_enable = False
        self.pause_enable = True
        self.repeat_enable = False
        self.audioplayer_mutestatus = False
        self.photo_viewer_enable = False
        self.photo_fullscreen_enable = False
        self.translate_toggle = False
        self.alarm_enable = False
        #icon_for_labels
        self.calculator_icon = QPixmap(calculator_icon_png)
        self.headphones_on_icon = QPixmap(headphones_on_icon_png)
        self.headphones_off_icon = QPixmap(headphones_off_icon_png)
        self.music_icon = QPixmap(music_icon_png)
        self.volume_player_off_icon = QPixmap(volume_player_off_icon_png)
        self.volume_player_on_icon = QPixmap(volume_player_on_icon_png)
        
        #icon_for_button
        self.calculator_icon = QIcon(calculator_icon_png)
        self.headphones_on_icon = QIcon(headphones_on_icon_png)
        self.headphones_off_icon = QIcon(headphones_off_icon_png)
        self.music_icon = QIcon(music_icon_png)
        self.volume_player_off_icon = QIcon(volume_player_off_icon_png)
        self.volume_player_on_icon = QIcon(volume_player_on_icon_png)
        self.reapeat_icon = QIcon(reapeat_icon_png)
        self.shuffle_icon = QIcon(shuffle_icon_png)
        self.library_import_icon = QIcon(library_import_icon_png)
        

        #change_pos
        self.audioplayer_pos_change_enable = False
        self.texnote_pos_change_enable = False
        self.calculator_pos_change_enable = False
        self.translate_pos_change_enable = False
        self.gallery_pos_change_enable = False


        #conenct
        self.pushButton.clicked.connect(self.mute_status_change)
        self.horizontalSlider.valueChanged.connect(self.volume_change)
        self.horizontalSlider.valueChanged.connect(self.volume_change)
        self.pushButton_4.clicked.connect(self.text_note_toggle)
        self.pushButton_7.clicked.connect(self.clear_textnote_all)
        self.pushButton_8.clicked.connect(self.clear_textnote_big)
        self.pushButton_9.clicked.connect(self.clear_textnote_middle)
        self.pushButton_10.clicked.connect(self.clear_textnote_small)
        self.pushButton_2.clicked.connect(self.calculator_toggle)
        self.pushButton_6.clicked.connect(self.audio_player_toggle)
        self.pushButton_30.clicked.connect(self.get_music_list)
        self.dial.valueChanged.connect(self.player_change_volume)
        self.listWidget.currentRowChanged.connect(self.track_change)
        self.pushButton_11.clicked.connect(self.audio_player_play)
        self.pushButton_28.clicked.connect(self.audio_player_pause)
        self.pushButton_33.clicked.connect(self.audio_player_pause)
        self.pushButton_31.clicked.connect(self.skip_left)
        self.pushButton_40.clicked.connect(self.skip_right)
        self.pushButton_41.clicked.connect(self.skip_right)
        self.pushButton_47.clicked.connect(self.change_pos_textnote)
        self.pushButton_46.clicked.connect(self.change_pos_calculator)
        self.pushButton_44.clicked.connect(self.change_pos_audio)
        self.pushButton_43.clicked.connect(self.change_pos_translate)
        self.pushButton_45.clicked.connect(self.change_pos_gallery)
        self.pushButton_50.clicked.connect(self.moveto_up)
        self.pushButton_29.clicked.connect(self.moveto_left)
        self.pushButton_51.clicked.connect(self.moveto_right)
        self.pushButton_42.clicked.connect(self.moveto_down)
        self.pushButton_34.clicked.connect(self.toggle_change_pos_menu)
        self.pushButton_39.clicked.connect(self.browser_open)
        self.pushButton_52.clicked.connect(self.photos_import)
        self.pushButton_53.clicked.connect(self.photo_path_clear)
        self.listWidget_2.currentItemChanged.connect(self.change_photo_fun)
        self.listWidget_3.currentItemChanged.connect(self.change_photo_fun_2)
        self.pushButton_3.clicked.connect(self.photo_viwer_toggle)
        self.pushButton_49.clicked.connect(self.photo_fullscreen)
        self.pushButton_48.clicked.connect(self.photo_fullscreen_second_button)
        self.pushButton_56.clicked.connect(self.photo_path_clear)
        self.pushButton_54.clicked.connect(self.second_list_hide)
        self.pushButton_55.clicked.connect(self.photos_import)
        self.pushButton_32.clicked.connect(self.aurora_mute)
        self.pushButton_59.clicked.connect(self.repeat_change_status)
        self.pushButton_60.clicked.connect(self.repeat_change_status)
        self.pushButton_61.clicked.connect(self.translate_text)
        self.pushButton_5.clicked.connect(self.show_translator)
        self.pushButton_38.clicked.connect(self.take_information_alarm)
        self.pushButton_63.clicked.connect(self.delete_all)
        self.pushButton_64.clicked.connect(self.delete_item)
        self.pushButton_35.clicked.connect(self.alarm_show)
        #1-Calculator_ 
        self.pushButton_12.clicked.connect(self.action1)
        #2
        self.pushButton_17.clicked.connect(self.action2)
        #3
        self.pushButton_19.clicked.connect(self.action3)
        #4
        self.pushButton_16.clicked.connect(self.action4)
        #5
        self.pushButton_15.clicked.connect(self.action5)
        #6
        self.pushButton_14.clicked.connect(self.action6)
        #7
        self.pushButton_21.clicked.connect(self.action7)
        #8
        self.pushButton_23.clicked.connect(self.action8)
        #9
        self.pushButton_22.clicked.connect(self.action9)
        #0
        self.pushButton_24.clicked.connect(self.action0)
        #-
        self.pushButton_20.clicked.connect(self.action_minus)
        #+
        self.pushButton_25.clicked.connect(self.action_plus)
        #=
        self.pushButton_13.clicked.connect(self.action_equal)
        #//
        self.pushButton_27.clicked.connect(self.action_div)
        #. 
        self.pushButton_26.clicked.connect(self.action_point)
        #clear
        self.pushButton_57.clicked.connect(self.action_clear)
        #del
        self.pushButton_58.clicked.connect(self.action_del)
        #*
        self.pushButton_18.clicked.connect(self.action_mul)

        #qtimers
        self.timer = QTimer()
        self.timer.timeout.connect(self.hours_change)
        self.timer.timeout.connect(self.time_month)
        self.timer.start(1000)

        self.timer_2 = QTimer()
        self.timer_2.start(1000)
        self.timer_2.timeout.connect(self.check_event)

        self.timer_3 = QTimer()
        self.timer_3.start(10)
        self.timer_3.timeout.connect(self.update_txt_audio)

        self.timer_4 = QTimer()
        self.timer_4.start(100)
        self.timer_4.timeout.connect(self.alarm_chcker)

    def browser_open(self):
        print("In WN 1.7.")


    def alarm_show(self):
        if self.alarm_enable:
            self.alarm_enable = False
            self.frame_9.hide()
        elif self.alarm_enable == False:
            self.alarm_enable = True
            self.frame_9.show()


    def show_translator(self):
        if self.translate_toggle:
            self.frame_8.hide()
            self.translate_toggle = False
        elif self.translate_toggle == False:
            self.frame_8.show()
            self.translate_toggle = True

    def photo_fullscreen(self):
        if self.photo_fullscreen_enable:
            self.frame_7.hide()
            self.photo_fullscreen_enable = False
        elif self.photo_fullscreen_enable == False:
            self.photo_fullscreen_enable = True
            self.frame_7.show()
    def photo_fullscreen_second_button(self):
        if self.photo_fullscreen_enable:
            self.frame_7.hide()
            self.photo_fullscreen_enable = False
        elif self.photo_fullscreen_enable == False:
            self.photo_fullscreen_enable = True
            self.frame_7.show()
    def translate_text(self):
        try:
            lang_from = self.comboBox.currentText().lower()
            lang_to = self.comboBox_2.currentText().lower()
            if lang_from == lang_to:
                self.textBrowser_6.setText("the language from which they are being translated and the language into which they are being translated cannot match. Please change one of section.")
            else:
                translator= Translator(from_lang=lang_from,to_lang=lang_to)
                translation = translator.translate(self.textEdit_2.toPlainText())
                self.textBrowser_6.setText(translation)

        except:
            self.textBrowser_6.setText("Translate Error. Check your text for mistakes.")
    def second_list_hide(self):
        if self.second_list_enable:
            self.second_list_enable = False
            self.listWidget_3.hide()
        elif self.second_list_enable == False:
            self.second_list_enable = True
            self.listWidget_3.show()
            
    def photo_viwer_toggle(self):
        if self.photo_viewer_enable:
            self.frame_5.hide()
            self.photo_viewer_enable = False
        elif self.photo_viewer_enable == False:
            self.photo_viewer_enable = True
            self.frame_5.show()

    def photos_import(self):
        try:
            self.listWidget_2.clear()
            self.listWidget_3.clear()
            global photo_path
            photo_path = QFileDialog.getExistingDirectory(self)
            photos = os.listdir(photo_path)
            for photo in photos:
                if ".png" in photo or ".jpg" in photo or ".tiff" in photo:
                    self.listWidget_2.addItem(photo)
                    self.listWidget_3.addItem(photo)
        except: 
            pass
    def photo_path_clear(self):
        self.listWidget_2.clear()
        self.listWidget_3.clear()
        self.label_11.clear()
        self.label_12.clear()
        self.textBrowser_5.setText(f"""Choosen File:""")
        self.label_13.setText(f"""Choosen File:""")

    def music_presence(self):
        rpc = Presence("967046869417099304")
        rpc.connect()
        rpc.update(state="WN OS 1.6",details=f"Listening {self.listWidget_2.currentItem().text()}")
    def music_presence(self):
        rpc.close()
    def repeat_change_status(self):

        if self.repeat_enable:
            self.repeat_enable = False
            self.pushButton_59.setIcon(self.shuffle_icon)
            self.pushButton_60.setIcon(self.shuffle_icon)

        elif self.repeat_enable == False:
            self.repeat_enable = True
            self.pushButton_59.setIcon(self.reapeat_icon)
            self.pushButton_60.setIcon(self.reapeat_icon)

    def change_photo(self):
        self.change_photo_fun()
    def change_photo_fun_2(self): 
        try:
            photo = self.listWidget_3.currentItem().text()
            self.textBrowser_5.setText(f"""Choosen File: {photo}""")
            self.label_13.setText(f"""Choosen File: {photo}""")
            self.listWidget_2.setCurrentRow(self.listWidget_3.currentRow())
            global photo_path
            photo = os.path.join(photo_path, photo)
            photo = QPixmap(photo)
            self.label_11.setPixmap(photo)
            self.label_12.setPixmap(photo)
        except:
            pass

    def change_photo_fun(self): 
        try:
            photo = self.listWidget_2.currentItem().text()
            self.textBrowser_5.setText(f"""Choosen File: {photo}""")
            self.label_13.setText(f"""Choosen File: {photo}""")
            self.listWidget_3.setCurrentRow(self.listWidget_2.currentRow())
            global photo_path
            photo = os.path.join(photo_path, photo)
            photo = QPixmap(photo)
            self.label_11.setPixmap(photo)
            self.label_12.setPixmap(photo)
        except:
            pass

    def time_month(self):
        self.today = datetime.datetime.today()
        self.today = self.today.strftime("%d/%m/%Y")
        self.label_9.setText(self.today)

    def hours_change(self):
        time = QTime.currentTime()
        hour = time.hour()
        minute = time.minute()
        if len(str(minute)) == 1:
            minute = "0"+str(minute)
        if len(str(hour)) == 1:
            hour = "0"+str(hour)

        text_label_8 =f'''{hour}:{minute}'''
        self.label_8.setText(text_label_8)

    def change_pos_audio(self):
        self.audioplayer_pos_change_enable = True
        self.texnote_pos_change_enable = False
        self.calculator_pos_change_enable = False
        self.translate_pos_change_enable = False
        self.gallery_pos_change_enable = False
        self.label_6.setText("Choosen: AudioPlayer Widget")
        self.label_2.setText(f"X:{self.frame_4.x()}")
        self.label_3.setText(f"X:{self.frame_4.y()}")

    def change_pos_textnote(self):
        self.audioplayer_pos_change_enable = False
        self.texnote_pos_change_enable = True
        self.calculator_pos_change_enable = False
        self.translate_pos_change_enable = False
        self.gallery_pos_change_enable = False
        self.label_6.setText("Choosen: Textnote Widget")
        self.label_2.setText(f"X:{self.frame_2.x()}")
        self.label_3.setText(f"X:{self.frame_2.y()}")

    def change_pos_calculator(self):
        self.audioplayer_pos_change_enable = False
        self.texnote_pos_change_enable = False
        self.calculator_pos_change_enable = True
        self.translate_pos_change_enable = False
        self.gallery_pos_change_enable = False
        self.label_6.setText("Choosen: Calculator Widget")
        self.label_2.setText(f"X:{self.frame_3.x()}")
        self.label_3.setText(f"X:{self.frame_3.y()}")

    def change_pos_translate(self):
        self.audioplayer_pos_change_enable = False
        self.texnote_pos_change_enable = False
        self.calculator_pos_change_enable = False
        self.translate_pos_change_enable = True
        self.gallery_pos_change_enable = False
        self.label_6.setText("Choosen: Translate Widget")
        self.label_2.setText(f"X:{self.frame_8.x()}")
        self.label_3.setText(f"X:{self.frame_8.y()}")

    def change_pos_gallery(self):
        self.audioplayer_pos_change_enable = False
        self.texnote_pos_change_enable = False
        self.calculator_pos_change_enable = False
        self.translate_pos_change_enable = False
        self.gallery_pos_change_enable = True
        self.label_6.setText("Choosen: Gallery Widget")
        self.label_2.setText(f"X:{self.frame_5.x()}")
        self.label_3.setText(f"X:{self.frame_5.y()}")
    def take_information_alarm(self):
        
        self.alarm_add_allow = True
        hour = int(self.lineEdit_2.text())
        minute = int(self.lineEdit_3.text())
        if self.alarm_add_allow:
            if minute >= 60 or minute < 0 or hour >= 25 or hour < 0:
                self.textBrowser_7.setText("Now allow for upload")
            else:
                minute = str(minute)
                hour = str(hour)
                if len(minute) == 1:
                    minute = "0"+minute
                if len(hour) == 1:
                    hour = "0"+hour
                alarm_time = (f"{hour}:{minute}")
                self.textBrowser_7.setText("Alarm Added")
                self.listWidget_4.addItem("Alarm: "+alarm_time)
                self.dict_alarm[alarm_time] = self.alarm_sound
                print(self.dict_alarm)
    def delete_item(self):
        row = self.listWidget_4.currentRow()
        print(row)
        self.listWidget_4.takeItem(row)
    def delete_all(self):
        self.listWidget_4.clear()
    
    def alarm_chcker(self):
        times = self.dict_alarm.keys()

        time = QTime.currentTime()
        hour = time.hour()
        minute = time.minute()

        if len(str(minute)) == 1:
            minute = "0"+str(minute)
        if len(str(hour)) == 1:
            hour = "0"+str(hour)

        self.current_time =f'''{hour}:{minute}'''


        if self.current_time in times:

            self.dict_alarm.pop(self.current_time)
            self.frame_10.show()
            self.label_7.setText("Alarm: "+self.current_time)
     
    def moveto_up(self):
        if self.audioplayer_pos_change_enable:
            self.frame_4.move(self.frame_4.x(),self.frame_4.y()-15)
            self.label_2.setText(f"X:{self.frame_4.x()}")
            self.label_3.setText(f"X:{self.frame_4.y()}")
        if self.texnote_pos_change_enable:
            self.frame_2.move(self.frame_2.x(),self.frame_2.y()-15)
            self.label_2.setText(f"X:{self.frame_2.x()}")
            self.label_3.setText(f"X:{self.frame_2.y()}")
        if self.calculator_pos_change_enable:
            self.frame_3.move(self.frame_3.x(),self.frame_3.y()-15)
            self.label_2.setText(f"X:{self.frame_3.x()}")
            self.label_3.setText(f"X:{self.frame_3.y()}")
        if self.gallery_pos_change_enable:
           self.frame_5.move(self.frame_5.x(),self.frame_5.y()-15)
           self.label_2.setText(f"X:{self.frame_5.x()}")
           self.label_3.setText(f"X:{self.frame_5.y()}")
        if self.translate_pos_change_enable:
            self.frame_8.move(self.frame_8.x(),self.frame_8.y()-15)
            self.label_2.setText(f"X:{self.frame_8.x()}")
            self.label_3.setText(f"X:{self.frame_8.y()}")

    def moveto_down(self):
        if self.audioplayer_pos_change_enable:
            self.frame_4.move(self.frame_4.x(),self.frame_4.y()+15)
            self.label_2.setText(f"X:{self.frame_4.x()}")
            self.label_3.setText(f"X:{self.frame_4.y()}")
        if self.texnote_pos_change_enable:
            self.frame_2.move(self.frame_2.x(),self.frame_2.y()+15)
            self.label_2.setText(f"X:{self.frame_2.x()}")
            self.label_3.setText(f"X:{self.frame_2.y()}")
        if self.calculator_pos_change_enable:
            self.frame_3.move(self.frame_3.x(),self.frame_3.y()+15)
            self.label_2.setText(f"X:{self.frame_3.x()}")
            self.label_3.setText(f"X:{self.frame_3.y()}")
        if self.gallery_pos_change_enable:
            self.frame_5.move(self.frame_5.x(),self.frame_5.y()+15)
            self.label_2.setText(f"X:{self.frame_5.x()}")
            self.label_3.setText(f"X:{self.frame_5.y()}")
        if self.translate_pos_change_enable:
            self.frame_8.move(self.frame_8.x(),self.frame_8.y()+15)
            self.label_2.setText(f"X:{self.frame_8.x()}")
            self.label_3.setText(f"X:{self.frame_8.y()}")

    def moveto_left(self):
        if self.audioplayer_pos_change_enable:
            self.frame_4.move(self.frame_4.x()-15,self.frame_4.y())
            self.label_2.setText(f"X:{self.frame_4.x()}")
            self.label_3.setText(f"X:{self.frame_4.y()}")
        if self.texnote_pos_change_enable:
            self.frame_2.move(self.frame_2.x()-15,self.frame_2.y())
            self.label_2.setText(f"X:{self.frame_2.x()}")
            self.label_3.setText(f"X:{self.frame_2.y()}")
        if self.calculator_pos_change_enable:
            self.frame_3.move(self.frame_3.x()-15,self.frame_3.y())
            self.label_2.setText(f"X:{self.frame_3.x()}")
            self.label_3.setText(f"X:{self.frame_3.y()}")
        if self.gallery_pos_change_enable:
            self.frame_5.move(self.frame_5.x()-15,self.frame_5.y())
            self.label_2.setText(f"X:{self.frame_5.x()}")
            self.label_3.setText(f"X:{self.frame_5.y()}")
        if self.translate_pos_change_enable:
            self.frame_8.move(self.frame_8.x()-15,self.frame_8.y())
            self.label_2.setText(f"X:{self.frame_8.x()}")
            self.label_3.setText(f"X:{self.frame_8.y()}")

    def moveto_right(self):
        if self.audioplayer_pos_change_enable:
            self.frame_4.move(self.frame_4.x()+15,self.frame_4.y())
            self.label_2.setText(f"X:{self.frame_4.x()}")
            self.label_3.setText(f"X:{self.frame_4.y()}")
        if self.texnote_pos_change_enable:
            self.frame_2.move(self.frame_2.x()+15,self.frame_2.y())
            self.label_2.setText(f"X:{self.frame_4.x()}")
            self.label_3.setText(f"X:{self.frame_4.y()}")
        if self.calculator_pos_change_enable:
            self.frame_3.move(self.frame_3.x()+15,self.frame_3.y())
            self.label_2.setText(f"X:{self.frame_3.x()}")
            self.label_3.setText(f"X:{self.frame_3.y()}")
        if self.gallery_pos_change_enable:
            self.frame_5.move(self.frame_5.x()+15,self.frame_5.y())
            self.label_2.setText(f"X:{self.frame_5.x()}")
            self.label_3.setText(f"X:{self.frame_5.y()}")
        if self.translate_pos_change_enable:
            self.frame_8.move(self.frame_8.x()+15,self.frame_8.y())
            self.label_2.setText(f"X:{self.frame_8.x()}")
            self.label_3.setText(f"X:{self.frame_8.y()}")

    def clear_textnote_all(self):
        self.textEdit.clear()
        self.plainTextEdit.clear()
        self.lineEdit.clear()

    def clear_textnote_big(self):
        self.textEdit.clear()
    
    
    def clear_textnote_middle(self):
        self.plainTextEdit.clear()

    def clear_textnote_small(self):
        self.lineEdit.clear()

    def audio_player_play(self):
        if self.allow_play_files:
            try:
                pygame.mixer.music.set_volume(self.dial.value()/100)
                pygame.mixer.music.unpause()
                self.frame_6.show()
                print(pygame.mixer.music.get_pos() / 1000)
            except:
                pass
    def audio_player_pause(self):
        try:
            pygame.mixer.music.pause()
            self.frame_6.hide()
        except:
            pass

    def check_event(self):
        if self.repeat_enable:
            for event in pygame.event.get():
                if event.type == self.STOPPED_PLAYING:
                    pygame.mixer.music.play()
        elif self.repeat_enable == False:
            for event in pygame.event.get():
                if event.type == self.STOPPED_PLAYING:
                    self.frame_6.hide()

    def mute_status_change(self):
        if self.mutestatus:
            self.mutestatus = False
            self.pushButton.setIcon(self.headphones_on_icon)
            self.horizontalSlider.setValue(self.last_volume)
            self.label.setText(str(self.horizontalSlider.value())+"%")
        elif self.mutestatus == False:
            self.last_volume = self.horizontalSlider.value()
            self.mutestatus = True
            self.pushButton.setIcon(self.headphones_off_icon)
            self.horizontalSlider.setValue(0)
            self.label.setText("MUTE")

 
    def calculator_toggle(self):
        if self.calculator_enable:
            self.calculator_enable = False
            self.frame_3.hide()
        elif self.calculator_enable == False:
            self.calculator_enable = True
            self.frame_3.show()

    def text_note_toggle(self):
        if self.textnote_enable:
            self.textnote_enable = False
            self.frame_2.hide()
        elif self.textnote_enable == False:
            self.textnote_enable = True
            self.frame_2.show()

    def audio_player_toggle(self):
        if self.audio_player_enable:
            self.audio_player_enable = False
            self.frame_4.hide()
        elif self.audio_player_enable == False:
            self.audio_player_enable = True
            self.frame_4.show()

    def volume_change(self):
        if self.mutestatus:
            self.horizontalSlider.setValue(0)
        else:
            self.label.setText(str(self.horizontalSlider.value())+"%")

    def get_music_list(self):
        try:
            self.listWidget.clear()
            global dirlisted
            dirlisted = QFileDialog.getExistingDirectory(self)
            all_items = os.listdir(dirlisted)
            for item in all_items:
                self.listWidget.addItem(item)
        except:
            pass

    def player_change_volume(self):
        if self.audioplayer_mutestatus == False:
            pygame.mixer.music.set_volume(self.dial.value()/100)
            text = "Volume: "+str(self.dial.value())+"%"
            self.label_5.setText(text)
        elif self.audioplayer_mutestatus == True:
            self.dial.setValue(0)
        
    def toggle_change_pos_menu(self):
        if self.change_pos_enable:
            self.change_pos_enable = False
            self.frame.hide()
        else:
            self.change_pos_enable = True
            self.frame.show()

    def track_change(self):
        try:
            pygame.mixer.stop()
            global track

            track = self.listWidget.currentItem().text()

            self.frame_6.show()

            self.track_play = os.path.join(dirlisted, track)

            pygame.mixer.music.load(self.track_play)
            self.track_mutagen = MP3(self.track_play)
            pygame.mixer.music.set_volume(self.dial.value()/100)
            pygame.mixer.music.play()
            self.allow_play_files = True
        except:
            pass

    def update_txt_audio(self):
        try:
            conversion = datetime.timedelta(seconds=int(pygame.mixer.music.get_pos()/1000))
            converted_time = str(conversion)
            self.textBrowser_2.setText(f'''
Playing Now:
{track}

{converted_time} secs.
        ''')

            self.textBrowser_3.setText(f'''Now: {track}''')
        except:
            pass

    def skip_left(self):
        if self.listWidget.currentRow() != 0:
            current_row_now = self.listWidget.currentRow()
            self.listWidget.setCurrentRow(current_row_now-1)
            text = "Volume: "+str(self.dial.value())+"%"
            self.frame_6.show()
            self.label_5.setText(text)
        else:
            current_row_now = self.listWidget.count()-1
            self.listWidget.setCurrentRow(current_row_now)
            self.frame_6.show()
            text = "Volume: "+str(self.dial.value())+"%"
            self.label_5.setText(text)

    def skip_right(self):
        if self.listWidget.currentRow() != self.listWidget.count()-1:
            current_row_now = self.listWidget.currentRow()
            self.listWidget.setCurrentRow(current_row_now+1)
            self.frame_6.show()
            text = "Volume: "+str(self.dial.value())+"%"
            self.label_5.setText(text)
        else:
            current_row_now = 0
            self.listWidget.setCurrentRow(current_row_now)
            self.frame_6.show()
            text = "Volume: "+str(self.dial.value())+"%"
            self.label_5.setText(text)

    def aurora_mute(self):
        if self.audioplayer_mutestatus:
            self.audioplayer_mutestatus = False
            self.pushButton_32.setIcon(self.headphones_on_icon)
            self.label_5.setText(f"Volume: {self.last_volume_player}%")
            self.dial.setValue(self.last_volume_player)
            pygame.mixer.music.set_volume(self.dial.value()/100)
        elif self.audioplayer_mutestatus == False:
            pygame.mixer.music.set_volume(0)
            self.audioplayer_mutestatus = True
            self.pushButton_32.setIcon(self.headphones_off_icon)
            self.last_volume_player = self.dial.value()
            self.dial.setValue(0)
            self.label_5.setText("Volume: Muted")
    #CALCULATOR
    


    def action_equal(self):
  
        # get the label text
        equation = self.textBrowser.toPlainText()
  
        try:
            # getting the ans
            ans = eval(equation)
  
            # setting text to the label
            self.textBrowser.setText(str(ans))
  
        except:
            # setting text to the label
            self.textBrowser.setText("Wrong Input")
  
    def action_plus(self):
        # appending label text
        text = self.textBrowser.toPlainText()
        self.textBrowser.setText(text + " + ")
  
    def action_minus(self):
        # appending label text
        text = self.textBrowser.toPlainText()
        self.textBrowser.setText(text + " - ")
  
    def action_div(self):
        # appending label text
        text = self.textBrowser.toPlainText()
        self.textBrowser.setText(text + " / ")
  
    def action_mul(self):
        # appending label text
        text = self.textBrowser.toPlainText()
        self.textBrowser.setText(text + " * ")
  
    def action_point(self):
        # appending label text
        text = self.textBrowser.toPlainText()
        self.textBrowser.setText(text + ".")
  
    def action0(self):
        # appending label text
        text = self.textBrowser.toPlainText()
        self.textBrowser.setText(text + "0")
  
    def action1(self):
        # appending label text
        text = self.textBrowser.toPlainText()
        self.textBrowser.setText(text + "1")
  
    def action2(self):
        # appending label text
        text = self.textBrowser.toPlainText()
        self.textBrowser.setText(text + "2")
  
    def action3(self):
        # appending label text
        text = self.textBrowser.toPlainText()
        self.textBrowser.setText(text + "3")
  
    def action4(self):
        # appending label text
        text = self.textBrowser.toPlainText()
        self.textBrowser.setText(text + "4")
  
    def action5(self):
        # appending label text
        text = self.textBrowser.toPlainText()
        self.textBrowser.setText(text + "5")
  
    def action6(self):
        # appending label text
        text = self.textBrowser.toPlainText()
        self.textBrowser.setText(text + "6")
  
    def action7(self):
        # appending label text
        text = self.textBrowser.toPlainText()
        self.textBrowser.setText(text + "7")
  
    def action8(self):
        # appending label text
        text = self.textBrowser.toPlainText()
        self.textBrowser.setText(text + "8")
  
    def action9(self):
        # appending label text
        text = self.textBrowser.toPlainText()
        self.textBrowser.setText(text + "9")
  
    def action_clear(self):
        # clearing the label text
        self.textBrowser.setText("")
  
    def action_del(self):
        # clearing a single digit
        text = self.textBrowser.toPlainText()
        self.textBrowser.setText(text[:len(text)-1])

def main():
    app = QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
    