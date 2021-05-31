##

import sys
import os
import time
import pathlib
import pytube
import webbrowser
import time
import ctypes

from pytube import Playlist
from pytube import YouTube
from pathlib import Path
from PyQt5.QtCore import QPoint
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLineEdit 
from PyQt5.QtWidgets import QProgressBar
from PyQt5.QtGui import QImage, QPixmap, QIcon

##

class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.window1 = Mp4_window()
        self.window2 = Mp3_window()
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(MyBar(self))
        self.setLayout(self.layout)
        print(os.path.dirname(__file__))
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.addStretch(-1)
        self.setGeometry(330, 110, 330, 110)
        self.setMinimumSize(330,100)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.pressing = False
        self.setStyleSheet("background:white")

        mp3 = QPushButton("Mp3(ses) İndirmek İçin Tıkla", self)
        mp4 = QPushButton("Mp4(video) İndirmek İçin Tıkla", self)
        github = QPushButton("Github", self)
        
        mp3.setGeometry(10, 45, 150, 30)
        mp4.setGeometry(170, 45, 150, 30)
        github.setGeometry(5, 5, 35, 15)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(5, 90, 160, 15))
        self.label.setObjectName("label")
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Dialog", "Çapan // mp3-mp4_indirici_v0.1"))
        self.label.setStyleSheet("QLabel { color : grey; }");
        
        mp3.clicked.connect(
            lambda checked: self.mp3_event(self.window2)
        )
        mp4.clicked.connect(
            lambda checked: self.mp4_event(self.window1)
        )
        github.clicked.connect(self.github_event)
        
        mp3.setStyleSheet("QPushButton"
                             "{"
                             "background-color: rgba(0, 0, 0, 0);"
                             "border : 0px solid black"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color: rgba(229, 229, 229, 0.9);"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color: rgba(229, 229, 229, 0.5);"
                             "}")
        
        mp4.setStyleSheet("QPushButton"
                             "{"
                             "background-color: rgba(0, 0, 0, 0);"
                             "border : 0px solid black"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color: rgba(229, 229, 229, 0.9);"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color: rgba(229, 229, 229, 0.5);"
                             "}")
        
        github.setStyleSheet("QPushButton"
                             "{"
                             "background-color: rgba(0, 0, 0, 0);"
                             "border : 0px solid black"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color: rgba(229, 229, 229, 0.9);"
                             "color: #1A0DAB"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color: rgba(229, 229, 229, 0.5);"
                             "color: #660099"
                             "}")
        
    def mp3_event(self, window):
        mw.hide()
        if window.isVisible():
            window.hide()

        else:
            window.show()
        
    def mp4_event(self, window):
        mw.hide()
        if window.isVisible():
            window.hide()

        else:
            window.show()

    def github_event(self):
        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://github.com/thescrayx")

class Mp4_window(QWidget):

    def __init__(self):
        super(Mp4_window, self).__init__()    
        self.layout  = QVBoxLayout()
        self.layout.addWidget(Mp4_bar(self))
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.addStretch(-1)
        self.setGeometry(330, 110, 330, 110)
        self.setMinimumSize(330,110)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.pressing = False
        self.setStyleSheet("background:white")      
        self.textbox = QLineEdit(self)
        self.textbox.move(25, 40)
        self.textbox.resize(280,20)
        self.textbox.setText(" Youtube Linkini Buraya Gir.")
        
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(25, 80, 125, 15)

        geri = QPushButton("←", self)
        geri.setGeometry(5, 5, 35, 15)
        geri.clicked.connect(self.geri_event)

        geri.setStyleSheet("QPushButton"
                             "{"
                             "background-color: rgba(0, 0, 0, 0);"
                             "border : 0px solid black"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color: rgba(229, 229, 229, 0.9);"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color: rgba(229, 229, 229, 0.5);"
                             "}")
        
        konum = QPushButton("İndirme konumunu aç", self)
        konum.setGeometry(330, 85, 180, 15)
        konum.clicked.connect(self.konum_event)

        konum.setStyleSheet("QPushButton"
                             "{"
                             "background-color: rgba(0, 0, 0, 0);"
                             "border : 1px solid black"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color: rgba(229, 229, 229, 0.9);"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color: rgba(229, 229, 229, 0.5);"
                             "}")
        
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(30, 65, 150, 15))
        self.label.setObjectName("label")
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Dialog", " "))
        
        self.title = QtWidgets.QLabel(self)
        self.title.setGeometry(QtCore.QRect(320, 25, 200, 15))
        self.title.setObjectName("title")
        _translate = QtCore.QCoreApplication.translate
        self.title.setText(_translate("Dialog", " "))
        
        self.kisi = QtWidgets.QLabel(self)
        self.kisi.setGeometry(QtCore.QRect(320, 45, 200, 15))
        self.kisi.setObjectName("kisi")
        _translate = QtCore.QCoreApplication.translate
        self.kisi.setText(_translate("Dialog", " "))

        self.sure = QtWidgets.QLabel(self)
        self.sure.setGeometry(QtCore.QRect(320, 65, 200, 15))
        self.sure.setObjectName("sure")
        _translate = QtCore.QCoreApplication.translate
        self.sure.setText(_translate("Dialog", " "))
        
        indir = QPushButton("İndirmek İçin Tıkla", self)
        indir.setGeometry(155, 70, 150, 30)
        indir.setStyleSheet("QPushButton"
                             "{"
                             "background-color: rgba(0, 0, 0, 0);"
                             "border : 0px solid black"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color: rgba(60, 60, 60, 0.1);"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color: rgba(60, 60, 60, 0.2);"
                             "}")
                
        indir.clicked.connect(self.indir_event)
        
    def indir_event(self):
        url = self.textbox.text()
        i = 0
        try:
            youtube = pytube.YouTube(url)
            i = 1
        except:
            self.label.setStyleSheet("QLabel { color : red; }");
            self.label.setText("Girilen link hatalı.")
        if i == 1:
            self.label.setStyleSheet("QLabel { color : green; }");
            self.label.setText("İndirme başlatıldı.")

            self.setMinimumSize(530,110)
            
            yt = YouTube(url)
            
            self.title.setText(yt.title)
            self.kisi.setText(yt.author)
            self.sure.setText("Video süresi(saniye): " + str(yt.length))

            def on_progress(stream, chunk, bytes_remaining):
                ls = 0
                total_size = stream.filesize
                bytes_downloaded = total_size - bytes_remaining 

                liveprogress = (int)(bytes_downloaded / total_size * 100)
                if liveprogress > ls:
                    ls = liveprogress
                    self.pbar.setValue(liveprogress)
                    if ls == 100:
                        self.label.setText("İndirme bitti.")

            yt.register_on_progress_callback(on_progress)
            yt.streams.get_highest_resolution().download("./Files/Mp4")
        
    def geri_event(self):
        self.hide()
        if mw.isVisible():
            mw.hide()

        else:
            mw.show()
            
    def konum_event(self):
        path = os.path.dirname(__file__) + "\Files"
        os.startfile(path)

class Mp3_window(QWidget):

    def __init__(self):
        super(Mp3_window, self).__init__()    
        self.layout  = QVBoxLayout()
        self.layout.addWidget(Mp3_bar(self))
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.addStretch(-1)
        self.setGeometry(330, 110, 330, 110)
        self.setMinimumSize(330,110)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.pressing = False
        self.setStyleSheet("background:white")      
        self.textbox = QLineEdit(self)
        self.textbox.move(25, 40)
        self.textbox.resize(280,20)
        self.textbox.setText(" Youtube Linkini Buraya Gir.")
        
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(25, 80, 125, 15)
        
        geri = QPushButton("←", self)
        geri.setGeometry(5, 5, 35, 15)
        geri.clicked.connect(self.geri_event)

        geri.setStyleSheet("QPushButton"
                             "{"
                             "background-color: rgba(0, 0, 0, 0);"
                             "border : 0px solid black"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color: rgba(229, 229, 229, 0.9);"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color: rgba(229, 229, 229, 0.5);"
                             "}")
        
        konum = QPushButton("İndirme konumunu aç", self)
        konum.setGeometry(330, 85, 180, 15)
        konum.clicked.connect(self.konum_event)
        
        konum.setStyleSheet("QPushButton"
                            "{"
                            "background-color: rgba(0, 0, 0, 0);"
                            "border : 1px solid black"
                            "}"
                            "QPushButton::hover"
                            "{"
                            "background-color: rgba(229, 229, 229, 0.9);"
                            "}"
                            "QPushButton::pressed"
                            "{"
                            "background-color: rgba(229, 229, 229, 0.5);"
                            "}")
        
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(30, 65, 150, 15))
        self.label.setObjectName("label")
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Dialog", " "))
        
        self.title = QtWidgets.QLabel(self)
        self.title.setGeometry(QtCore.QRect(320, 25, 200, 15))
        self.title.setObjectName("title")
        _translate = QtCore.QCoreApplication.translate
        self.title.setText(_translate("Dialog", " "))
        
        self.kisi = QtWidgets.QLabel(self)
        self.kisi.setGeometry(QtCore.QRect(320, 45, 200, 15))
        self.kisi.setObjectName("kisi")
        _translate = QtCore.QCoreApplication.translate
        self.kisi.setText(_translate("Dialog", " "))

        self.sure = QtWidgets.QLabel(self)
        self.sure.setGeometry(QtCore.QRect(320, 65, 200, 15))
        self.sure.setObjectName("sure")
        _translate = QtCore.QCoreApplication.translate
        self.sure.setText(_translate("Dialog", " "))
        
        indir = QPushButton("İndirmek İçin Tıkla", self)
        indir.setGeometry(155, 70, 150, 30)
        indir.setStyleSheet("QPushButton"
                             "{"
                             "background-color: rgba(0, 0, 0, 0);"
                             "border : 0px solid black"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color: rgba(60, 60, 60, 0.1);"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color: rgba(60, 60, 60, 0.2);"
                             "}")
                
        indir.clicked.connect(self.indir_event)
        
    def indir_event(self):
        url = self.textbox.text()
        i = 0
        try:
            youtube = pytube.YouTube(url)
            i = 1
        except:
            self.label.setStyleSheet("QLabel { color : red; }");
            self.label.setText("Girilen link hatalı.")
        if i == 1:
            self.label.setStyleSheet("QLabel { color : green; }");
            self.label.setText("İndirme başlatıldı.")

            self.setMinimumSize(530,110)
            
            yt = YouTube(url)
            
            self.title.setText(yt.title)
            self.kisi.setText(yt.author)
            self.sure.setText("Video süresi(saniye): " + str(yt.length))

            def on_progress(stream, chunk, bytes_remaining):
                ls = 0
                total_size = stream.filesize
                bytes_downloaded = total_size - bytes_remaining 

                liveprogress = (int)(bytes_downloaded / total_size * 100)
                if liveprogress > ls:
                    ls = liveprogress
                    self.pbar.setValue(liveprogress)                      

            yt.register_on_progress_callback(on_progress)
            yt.streams.get_audio_only().download("./Files/Mp3/", filename="indirilen_mp3_dosya")
            dosya = Path(str(pathlib.Path().absolute()) + "\\Files\\Mp3\\indirilen_mp3_dosya.mp4")
            yol = Path(str(pathlib.Path().absolute()) + "\\Files\\Mp3\\" + str(yt.title) + ".mp3")
            try:
                os.rename(dosya , yol)
            except:
                os.remove(dosya)
                ctypes.windll.user32.MessageBoxW(0, u"Bunu zaten daha önceden indirdin.\n(Hatayı almaya devam ederseniz 'Files/Mp3' dosyasını silin.)", u"Hata(0)(Mp3)", 0)
            
    def geri_event(self):
        self.hide()
        if mw.isVisible():
            mw.hide()

        else:
            mw.show()
            
    def konum_event(self):
        path = os.path.dirname(__file__) + "\Files"
        os.startfile(path)

class Mp4_bar(QWidget):

    def __init__(self, parent):
        super(Mp4_bar, self).__init__()
        self.parent = parent
        print(self.parent.width())
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0,0,5,0)
        self.title = QLabel("Mp4 İndirici")

        btn_size_1 = 25
        btn_size_2 = 40

        self.btn_close = QPushButton("❌")
        self.btn_close.clicked.connect(self.btn_close_clicked)
        self.btn_close.setFixedSize(btn_size_2, btn_size_1)
        self.btn_close.setStyleSheet("QPushButton"
                             "{"
                             "background-color: rgba(0, 0, 0, 0);"
                             "border : 0px solid black"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color: rgba(232, 17, 35, 1);"
                             "color: #ffffff"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color: rgba(232, 17, 35, 0.5);"
                             "color: #ffffff"
                             "}")

        self.btn_min = QPushButton("➖")
        self.btn_min.clicked.connect(self.btn_min_clicked)
        self.btn_min.setFixedSize(btn_size_2, btn_size_1)
        self.btn_min.setStyleSheet("QPushButton"
                             "{"
                             "background-color: rgba(0, 0, 0, 0);"
                             "border : 0px solid black"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color: rgba(60, 60, 60, 0.1);"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color: rgba(60, 60, 60, 0.2);"
                             "}")

        self.title.setFixedHeight(25)
        self.title.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.btn_min)
        self.layout.addWidget(self.btn_close)

        self.title.setStyleSheet("""
            background-color: white;
            color: black;
        """)
        self.setLayout(self.layout)

        self.start = QPoint(0, 0)
        self.pressing = False

    def resizeEvent(self, QResizeEvent):
        super(Mp4_bar, self).resizeEvent(QResizeEvent)
        self.title.setFixedWidth(self.parent.width())

    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end-self.start
            self.parent.setGeometry(self.mapToGlobal(self.movement).x(),
                                self.mapToGlobal(self.movement).y(),
                                self.parent.width(),
                                self.parent.height())
            self.start = self.end

    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False


    def btn_close_clicked(self):
        self.parent.close()

    def btn_min_clicked(self):
        self.parent.showMinimized()

class Mp3_bar(QWidget):

    def __init__(self, parent):
        super(Mp3_bar, self).__init__()
        self.parent = parent
        print(self.parent.width())
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0,0,5,0)
        self.title = QLabel("Mp3 İndirici")

        btn_size_1 = 25
        btn_size_2 = 40

        self.btn_close = QPushButton("❌")
        self.btn_close.clicked.connect(self.btn_close_clicked)
        self.btn_close.setFixedSize(btn_size_2, btn_size_1)
        self.btn_close.setStyleSheet("QPushButton"
                             "{"
                             "background-color: rgba(0, 0, 0, 0);"
                             "border : 0px solid black"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color: rgba(232, 17, 35, 1);"
                             "color: #ffffff"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color: rgba(232, 17, 35, 0.5);"
                             "color: #ffffff"
                             "}")

        self.btn_min = QPushButton("➖")
        self.btn_min.clicked.connect(self.btn_min_clicked)
        self.btn_min.setFixedSize(btn_size_2, btn_size_1)
        self.btn_min.setStyleSheet("QPushButton"
                             "{"
                             "background-color: rgba(0, 0, 0, 0);"
                             "border : 0px solid black"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color: rgba(60, 60, 60, 0.1);"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color: rgba(60, 60, 60, 0.2);"
                             "}")

        self.title.setFixedHeight(25)
        self.title.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.btn_min)
        self.layout.addWidget(self.btn_close)

        self.title.setStyleSheet("""
            background-color: white;
            color: black;
        """)
        self.setLayout(self.layout)

        self.start = QPoint(0, 0)
        self.pressing = False

    def resizeEvent(self, QResizeEvent):
        super(Mp3_bar, self).resizeEvent(QResizeEvent)
        self.title.setFixedWidth(self.parent.width())

    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end-self.start
            self.parent.setGeometry(self.mapToGlobal(self.movement).x(),
                                self.mapToGlobal(self.movement).y(),
                                self.parent.width(),
                                self.parent.height())
            self.start = self.end

    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False


    def btn_close_clicked(self):
        self.parent.close()

    def btn_min_clicked(self):
        self.parent.showMinimized()

class MyBar(QWidget):

    def __init__(self, parent):
        super(MyBar, self).__init__()
        self.parent = parent
        print(self.parent.width())
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0,0,5,0)
        self.title = QLabel("Dosya Türünü Seç")

        btn_size_1 = 25
        btn_size_2 = 40

        self.btn_close = QPushButton("❌")
        self.btn_close.clicked.connect(self.btn_close_clicked)
        self.btn_close.setFixedSize(btn_size_2, btn_size_1)
        self.btn_close.setStyleSheet("QPushButton"
                             "{"
                             "background-color: rgba(0, 0, 0, 0);"
                             "border : 0px solid black"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color: rgba(232, 17, 35, 1);"
                             "color: #ffffff"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color: rgba(232, 17, 35, 0.5);"
                             "color: #ffffff"
                             "}")

        self.btn_min = QPushButton("➖")
        self.btn_min.clicked.connect(self.btn_min_clicked)
        self.btn_min.setFixedSize(btn_size_2, btn_size_1)
        self.btn_min.setStyleSheet("QPushButton"
                             "{"
                             "background-color: rgba(0, 0, 0, 0);"
                             "border : 0px solid black"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color: rgba(60, 60, 60, 0.1);"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color: rgba(60, 60, 60, 0.2);"
                             "}")

        self.title.setFixedHeight(25)
        self.title.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.btn_min)
        self.layout.addWidget(self.btn_close)

        self.title.setStyleSheet("""
            background-color: white;
            color: black;
        """)
        self.setLayout(self.layout)

        self.start = QPoint(0, 0)
        self.pressing = False

    def resizeEvent(self, QResizeEvent):
        super(MyBar, self).resizeEvent(QResizeEvent)
        self.title.setFixedWidth(self.parent.width())

    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end-self.start
            self.parent.setGeometry(self.mapToGlobal(self.movement).x(),
                                self.mapToGlobal(self.movement).y(),
                                self.parent.width(),
                                self.parent.height())
            self.start = self.end

    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False


    def btn_close_clicked(self):
        self.parent.close()

    def btn_min_clicked(self):
        self.parent.showMinimized()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())
