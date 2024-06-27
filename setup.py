from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.uic import loadUi
import requests
from PyQt5.QtGui import QPixmap
import json
import random



def setup_frameTop(self):
    self.frameTop = QtWidgets.QFrame(self.centralwidget)
    self.frameTop.setGeometry(QtCore.QRect(70, 40, 851, 161))
    self.frameTop.setFrameShape(QtWidgets.QFrame.StyledPanel)
    self.frameTop.setFrameShadow(QtWidgets.QFrame.Raised)
    self.frameTop.setObjectName("frame_top")

def setup_logoPicLabel(self):
    self.logoPicLabel = QtWidgets.QLabel(self.frameTop)
    self.logoPicLabel.setGeometry(QtCore.QRect(20, 10, 131, 131))
    font = QtGui.QFont()
    font.setPointSize(12)
    self.logoPicLabel.setFont(font)
    self.logoPicLabel.setText("")
    self.logoPicLabel.setPixmap(QtGui.QPixmap("../../Users/edwma/OneDrive/Pictures/milleniumeye.png"))
    self.logoPicLabel.setScaledContents(True)
    self.logoPicLabel.setObjectName("logoPicLabel")

def setup_logoTextLabel(self):
    self.logoTextLabel = QtWidgets.QLabel(self.frameTop)
    self.logoTextLabel.setGeometry(QtCore.QRect(160, 30, 191, 101))
    font = QtGui.QFont()
    font.setPointSize(20)
    font.setBold(True)
    font.setWeight(75)
    self.logoTextLabel.setFont(font)
    self.logoTextLabel.setObjectName("logoTextLabel")

def setup_homeButton(self):
    self.homeButton = QtWidgets.QPushButton(self.frameTop)
    self.homeButton.setGeometry(QtCore.QRect(630, 10, 75, 23))
    self.homeButton.setStyleSheet("background-color:rgb(105,105,105);\n"
            "color:rgb(230,230,230);\n"
            "font-weight:bold")
    self.homeButton.setObjectName("homeButton")
    self.homeButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))

def setup_browseButton(self):
    self.browseButton = QtWidgets.QPushButton(self.frameTop)
    self.browseButton.setGeometry(QtCore.QRect(740, 10, 75, 23))
    self.browseButton.setStyleSheet("background-color:rgb(105,105,105);\n"
            "color: rgb(230,230,230);\n"
            "font-weight:bold")
    self.browseButton.setObjectName("browseButton")
    self.browseButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))

def setup_searchInput(self):
    self.searchInput = QtWidgets.QLineEdit(self.frameTop)
    self.searchInput.setGeometry(QtCore.QRect(380, 90, 361, 21))
    self.searchInput.setStyleSheet("")
    self.searchInput.setText("")
    self.searchInput.setObjectName("searchInput")

def setup_searchButton(self):
    self.searchButton = QtWidgets.QPushButton(self.frameTop)
    self.searchButton.setGeometry(QtCore.QRect(740, 90, 75, 21))
    self.searchButton.setAutoFillBackground(False)
    self.searchButton.setStyleSheet("background-color:rgb(105,105,105);\n"
            "color: rgb(230,230,230);\n"
            "font-weight:bold")
    self.searchButton.setObjectName("searchButton")
    self.searchButton.clicked.connect(lambda: self.search(self.searchInput.text()))

def setup_randomCardButton(self):
    self.randomButton = QtWidgets.QPushButton(self.frameTop)
                self.randomButton.setGeometry(QtCore.QRect(380, 10, 75, 23))
                self.randomButton.setStyleSheet("background-color:rgb(105,105,105);\n"
                        "color: rgb(230,230,230);\n"
                        "font-weight:bold")
                self.randomButton.setObjectName("randomButton")
                self.randomButton.clicked.connect(lambda: self.search(self.getRandomCard()))
    
def setup_framePages(self):
     self.framePages = QtWidgets.QFrame(self.centralwidget)
                self.framePages.setGeometry(QtCore.QRect(69, 219, 861, 1200))
                self.framePages.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.framePages.setFrameShadow(QtWidgets.QFrame.Raised)
                self.framePages.setObjectName("frame_pages")
                self.stackedWidget = QtWidgets.QStackedWidget(self.framePages)
                self.stackedWidget.setGeometry(QtCore.QRect(19, 19, 821, 651))
                self.stackedWidget.setObjectName("stackedWidget")
     
def setup_homePage(self):
    
                self.homePage = QtWidgets.QWidget()
                self.homePage.setObjectName("homePage")
                self.homeDetailLabel = QtWidgets.QLabel(self.homePage)
                self.homeDetailLabel.setGeometry(QtCore.QRect(10, 10, 211, 71))
                self.homeDetailLabel.setObjectName("homeDetailLabel")
                self.stackedWidget.addWidget(self.homePage)

def setup_top5Label(self):
      self.top5Label = QtWidgets.QLabel(self.homePage)
                self.top5Label.setGeometry(QtCore.QRect(300, 80, 200, 21))
                self.top5Label.setObjectName("top5Label")
                # top 10 table
                self.top5Table = QtWidgets.QTableWidget(self.homePage)
                self.top5Table.setGeometry(QtCore.QRect(10, 100, 800, 1000))
                self.top5Table.setObjectName("top5Table")
      
def setup_browsePage(self):
       
                self.browsePage = QtWidgets.QWidget()
                self.browsePage.setObjectName("browsePage")
                self.browseLabel = QtWidgets.QLabel(self.browsePage)
                self.browseLabel.setGeometry(QtCore.QRect(20, 50, 61, 21))
                self.browseLabel.setObjectName("browseLabel")
                self.stackedWidget.addWidget(self.browsePage)

def setup_attributeLabel(self):
       self.attributeLabel = QtWidgets.QLabel(self.browsePage)
                self.attributeLabel.setGeometry(QtCore.QRect(20, 80, 61, 21))
                self.attributeLabel.setObjectName("attributeLabel")
                self.attributeLabel.setText("<b>Attributes:</b>")
       
def setup_browseDarkButton(self):
       self.browseDarkButton = QtWidgets.QPushButton(self.browsePage)
                self.browseDarkButton.setGeometry(QtCore.QRect(20, 100, 60, 20))
                self.browseDarkButton.setObjectName("browseDarkButton")
                self.browseDarkButton.setText("Dark")
                self.browseDarkButton.setStyleSheet("background-color:transparent; color:blue;")
       
def setup_browseDivineButton(self):
       self.browseDivineButton = QtWidgets.QPushButton(self.browsePage)
                self.browseDivineButton.setGeometry(QtCore.QRect(70, 100, 60, 20))
                self.browseDivineButton.setObjectName("browseDivineButton")
                self.browseDivineButton.setText("Divine")
                self.browseDivineButton.setStyleSheet("background-color:transparent; color:blue;")

def setup_browseEarthButton(self):
       self.browseEarthButton = QtWidgets.QPushButton(self.browsePage)
                self.browseEarthButton.setGeometry(QtCore.QRect(120, 100, 60, 20))
                self.browseEarthButton.setObjectName("browseEarthButton")
                self.browseEarthButton.setText("Earth")
                self.browseEarthButton.setStyleSheet("background-color:transparent; color:blue;")
       
def setup_browseFireButton(self):
       self.browseFireButton = QtWidgets.QPushButton(self.browsePage)
                self.browseFireButton.setGeometry(QtCore.QRect(170, 100, 60, 20))
                self.browseFireButton.setObjectName("browseFireButton")
                self.browseFireButton.setText("Fire")
                self.browseFireButton.setStyleSheet("background-color:transparent; color:blue;")

def setup_browseLightButton(self):
        self.browseLightButton = QtWidgets.QPushButton(self.browsePage)
                self.browseLightButton.setGeometry(QtCore.QRect(220, 100, 60, 20))
                self.browseLightButton.setObjectName("browseLightButton")
                self.browseLightButton.setText("Light")
                self.browseLightButton.setStyleSheet("background-color:transparent; color:blue;")

def setup_browseWaterButton(self):
        self.browseWaterButton = QtWidgets.QPushButton(self.browsePage)
                self.browseWaterButton.setGeometry(QtCore.QRect(270, 100, 60, 20))
                self.browseWaterButton.setObjectName("browseWaterButton")
                self.browseWaterButton.setText("Water")
                self.browseWaterButton.setStyleSheet("background-color:transparent; color:blue;")
        
def setup_browseWindButton(self):
        self.browseWindButton = QtWidgets.QPushButton(self.browsePage)
                self.browseWindButton.setGeometry(QtCore.QRect(320, 100, 60, 20))
                self.browseWindButton.setObjectName("browseWindButton")
                self.browseWindButton.setText("Wind")
                self.browseWindButton.setStyleSheet("background-color:transparent; color:blue;")
def setup_browseTable(self):
        self.browseTable = QtWidgets.QTableWidget(self.browsePage)
        self.browseTable.setGeometry(QtCore.QRect(280, 130, 300, 600))
        self.browseTable.setObjectName("browseTable")

def setup_searchPage(self):
        self.searchPage = QtWidgets.QWidget()
                self.searchPage.setObjectName("searchPage")
                self.searchLabel = QtWidgets.QLabel(self.searchPage)
                self.searchLabel.setGeometry(QtCore.QRect(390, 40, 51, 41))
                self.searchLabel.setObjectName("searchLabel")
                self.stackedWidget.addWidget(self.searchPage)
def setup_searchPicLabel(self):
        self.searchPicLabel = QtWidgets.QLabel(self.searchPage)
                self.searchPicLabel.setGeometry(QtCore.QRect(0, 80, 300, 450))

def setup_searchNameLabel(self):
        self.searchNameLabel = QtWidgets.QLabel(self.searchPage)
                self.searchNameLabel.setGeometry(QtCore.QRect(320, 70, 300, 40))
        
def setup_searchDescriptionLabel(self):
        self.searchDescriptionLabel = QtWidgets.QLabel(self.searchPage)
                self.searchDescriptionLabel.setGeometry(QtCore.QRect(320, 20, 400, 400))
                self.searchDescriptionLabel.setWordWrap(True)
        
def setup_searchPriceLabel(self):
        self.searchPriceLabel = QtWidgets.QLabel(self.searchPage)
                self.searchPriceLabel.setGeometry(QtCore.QRect(320, 500, 400, 40))