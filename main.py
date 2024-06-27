from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import requests
from PyQt5.QtGui import QPixmap
import json
import random


class Ui_mainWindow(object):
        def setupUi(self, mainWindow):
                self.setupInitial()
                self.setupHomeComponents()
                self.setupRandomCardButton()
                self.setupBrowseComponents()
                self.setupAttributeButtons() 
                self.setupSearchComponents()
                mainWindow.setCentralWidget(self.centralwidget)
                self.retranslateUi(mainWindow)
                self.stackedWidget.setCurrentIndex(0)
                QtCore.QMetaObject.connectSlotsByName(mainWindow)

        def retranslateUi(self, mainWindow):
                _translate = QtCore.QCoreApplication.translate
                self.setupLogo(mainWindow, _translate)
                self.setupButtonAndInputText(_translate)
                self.setupTop5Table()
                self.populateTop5Table()

        def setupInitial(self):
                self.setupMainWindow()
                self.setupFrameTop()
                self.setupLogoPicLabel()
                self.setupLogoTextLabel()
                self.setupFramePages()
        
        def setupHomeComponents(self):
                self.setupHomePage()
                self.setupHomeButton()
                self.setupTop5Label()  

        def setupBrowseComponents(self):
                self.setupBrowsePage()
                self.setupBrowseButton()
                self.setupBrowseTable()
                self.setupAttributeLabel()

        def setupAttributeButtons(self):
                self.setupBrowseDarkButton()
                self.setupBrowseDivineButton()
                self.setupBrowseEarthButton()
                self.setupBrowseFireButton()
                self.setupBrowseLightButton()
                self.setupBrowseWaterButton()
                self.setupBrowseWindButton()

        def setupSearchComponents(self):
                self.setupSearchInput()
                self.setupSearchButton()
                self.setupSearchPage()
                self.setupSearchPicLabel()
                self.setupSearchNameLabel()
                self.setupSearchDescriptionLabel()
                self.setupSearchPriceLabel()
        
        def setupMainWindow(self):
                mainWindow.setObjectName("mainWindow")
                mainWindow.setEnabled(True)
                mainWindow.resize(980, 918)
                self.centralwidget = QtWidgets.QWidget(mainWindow)
                self.centralwidget.setObjectName("centralwidget")

        def setupFrameTop(self):
                self.frameTop = QtWidgets.QFrame(self.centralwidget)
                self.frameTop.setGeometry(QtCore.QRect(70, 40, 851, 161))
                self.frameTop.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frameTop.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frameTop.setObjectName("frame_top")

        def setupLogoPicLabel(self):
                self.logoPicLabel = QtWidgets.QLabel(self.frameTop)
                self.logoPicLabel.setGeometry(QtCore.QRect(20, 10, 131, 131))
                font = QtGui.QFont()
                font.setPointSize(12)
                self.logoPicLabel.setFont(font)
                self.logoPicLabel.setText("")
                self.logoPicLabel.setPixmap(QtGui.QPixmap("../../Users/edwma/OneDrive/Pictures/milleniumeye.png"))
                self.logoPicLabel.setScaledContents(True)
                self.logoPicLabel.setObjectName("logoPicLabel")

        def setupLogoTextLabel(self):
                self.logoTextLabel = QtWidgets.QLabel(self.frameTop)
                self.logoTextLabel.setGeometry(QtCore.QRect(160, 30, 191, 101))
                font = QtGui.QFont()
                font.setPointSize(20)
                font.setBold(True)
                font.setWeight(75)
                self.logoTextLabel.setFont(font)
                self.logoTextLabel.setObjectName("logoTextLabel")

        def setupHomeButton(self):
                self.homeButton = QtWidgets.QPushButton(self.frameTop)
                self.homeButton.setGeometry(QtCore.QRect(630, 10, 75, 23))
                self.homeButton.setStyleSheet("background-color:rgb(105,105,105);\n"
                        "color:rgb(230,230,230);\n"
                        "font-weight:bold")
                self.homeButton.setObjectName("homeButton")
                self.homeButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))

        def setupBrowseButton(self):
                self.browseButton = QtWidgets.QPushButton(self.frameTop)
                self.browseButton.setGeometry(QtCore.QRect(740, 10, 75, 23))
                self.browseButton.setStyleSheet("background-color:rgb(105,105,105);\n"
                        "color: rgb(230,230,230);\n"
                        "font-weight:bold")
                self.browseButton.setObjectName("browseButton")
                self.browseButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))

        def setupSearchInput(self):
                self.searchInput = QtWidgets.QLineEdit(self.frameTop)
                self.searchInput.setGeometry(QtCore.QRect(380, 90, 361, 21))
                self.searchInput.setStyleSheet("")
                self.searchInput.setText("")
                self.searchInput.setObjectName("searchInput")
        
        def setupSearchButton(self):
                self.searchButton = QtWidgets.QPushButton(self.frameTop)
                self.searchButton.setGeometry(QtCore.QRect(740, 90, 75, 21))
                self.searchButton.setAutoFillBackground(False)
                self.searchButton.setStyleSheet("background-color:rgb(105,105,105);\n"
                        "color: rgb(230,230,230);\n"
                        "font-weight:bold")
                self.searchButton.setObjectName("searchButton")
                self.searchButton.clicked.connect(lambda: self.search(self.searchInput.text()))

        def setupRandomCardButton(self):
                self.randomButton = QtWidgets.QPushButton(self.frameTop)
                self.randomButton.setGeometry(QtCore.QRect(380, 10, 75, 23))
                self.randomButton.setStyleSheet("background-color:rgb(105,105,105);\n"
                        "color: rgb(230,230,230);\n"
                        "font-weight:bold")
                self.randomButton.setObjectName("randomButton")
                self.randomButton.clicked.connect(lambda: self.search(self.getRandomCard()))

        def setupFramePages(self):
                self.framePages = QtWidgets.QFrame(self.centralwidget)
                self.framePages.setGeometry(QtCore.QRect(69, 219, 861, 1200))
                self.framePages.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.framePages.setFrameShadow(QtWidgets.QFrame.Raised)
                self.framePages.setObjectName("frame_pages")
                self.stackedWidget = QtWidgets.QStackedWidget(self.framePages)
                self.stackedWidget.setGeometry(QtCore.QRect(19, 19, 821, 651))
                self.stackedWidget.setObjectName("stackedWidget")

        def setupHomePage(self):
                self.homePage = QtWidgets.QWidget()
                self.homePage.setObjectName("homePage")
                self.homeDetailLabel = QtWidgets.QLabel(self.homePage)
                self.homeDetailLabel.setGeometry(QtCore.QRect(10, 10, 211, 71))
                self.homeDetailLabel.setObjectName("homeDetailLabel")
                self.stackedWidget.addWidget(self.homePage)

        def setupTop5Label(self):
                self.top5Label = QtWidgets.QLabel(self.homePage)
                self.top5Label.setGeometry(QtCore.QRect(300, 80, 200, 21))
                self.top5Label.setObjectName("top5Label")
                self.top5Table = QtWidgets.QTableWidget(self.homePage)
                self.top5Table.setGeometry(QtCore.QRect(10, 100, 800, 1000))
                self.top5Table.setObjectName("top5Table")

        def setupBrowsePage(self):
                self.browsePage = QtWidgets.QWidget()
                self.browsePage.setObjectName("browsePage")
                self.browseLabel = QtWidgets.QLabel(self.browsePage)
                self.browseLabel.setGeometry(QtCore.QRect(20, 50, 61, 21))
                self.browseLabel.setObjectName("browseLabel")
                self.stackedWidget.addWidget(self.browsePage)

        def setupAttributeLabel(self):
                self.attributeLabel = QtWidgets.QLabel(self.browsePage)
                self.attributeLabel.setGeometry(QtCore.QRect(20, 80, 61, 21))
                self.attributeLabel.setObjectName("attributeLabel")
                self.attributeLabel.setText("<b>Attributes:</b>")

        def setupBrowseDarkButton(self):
                self.browseDarkButton = QtWidgets.QPushButton(self.browsePage)
                self.browseDarkButton.setGeometry(QtCore.QRect(20, 100, 60, 20))
                self.browseDarkButton.setObjectName("browseDarkButton")
                self.browseDarkButton.setText("Dark")
                self.browseDarkButton.setStyleSheet("background-color:transparent; color:blue;")
                self.browseDarkButton.clicked.connect(lambda: self.populateBrowseTable('dark'))

               
        def setupBrowseDivineButton(self):
                self.browseDivineButton = QtWidgets.QPushButton(self.browsePage)
                self.browseDivineButton.setGeometry(QtCore.QRect(70, 100, 60, 20))
                self.browseDivineButton.setObjectName("browseDivineButton")
                self.browseDivineButton.setText("Divine")
                self.browseDivineButton.setStyleSheet("background-color:transparent; color:blue;")
                self.browseDivineButton.clicked.connect(lambda: self.populateBrowseTable('divine'))

        def setupBrowseEarthButton(self):
                self.browseEarthButton = QtWidgets.QPushButton(self.browsePage)
                self.browseEarthButton.setGeometry(QtCore.QRect(120, 100, 60, 20))
                self.browseEarthButton.setObjectName("browseEarthButton")
                self.browseEarthButton.setText("Earth")
                self.browseEarthButton.setStyleSheet("background-color:transparent; color:blue;")
                self.browseEarthButton.clicked.connect(lambda: self.populateBrowseTable('earth'))

        def setupBrowseFireButton(self):
                self.browseFireButton = QtWidgets.QPushButton(self.browsePage)
                self.browseFireButton.setGeometry(QtCore.QRect(170, 100, 60, 20))
                self.browseFireButton.setObjectName("browseFireButton")
                self.browseFireButton.setText("Fire")
                self.browseFireButton.setStyleSheet("background-color:transparent; color:blue;")
                self.browseFireButton.clicked.connect(lambda: self.populateBrowseTable('fire'))
        
        def setupBrowseLightButton(self):
                self.browseLightButton = QtWidgets.QPushButton(self.browsePage)
                self.browseLightButton.setGeometry(QtCore.QRect(220, 100, 60, 20))
                self.browseLightButton.setObjectName("browseLightButton")
                self.browseLightButton.setText("Light")
                self.browseLightButton.setStyleSheet("background-color:transparent; color:blue;")
                self.browseLightButton.clicked.connect(lambda: self.populateBrowseTable('light'))

        def setupBrowseWaterButton(self):
                self.browseWaterButton = QtWidgets.QPushButton(self.browsePage)
                self.browseWaterButton.setGeometry(QtCore.QRect(270, 100, 60, 20))
                self.browseWaterButton.setObjectName("browseWaterButton")
                self.browseWaterButton.setText("Water")
                self.browseWaterButton.setStyleSheet("background-color:transparent; color:blue;")
                self.browseWaterButton.clicked.connect(lambda: self.populateBrowseTable('water'))

        def setupBrowseWindButton(self):
                self.browseWindButton = QtWidgets.QPushButton(self.browsePage)
                self.browseWindButton.setGeometry(QtCore.QRect(320, 100, 60, 20))
                self.browseWindButton.setObjectName("browseWindButton")
                self.browseWindButton.setText("Wind")
                self.browseWindButton.setStyleSheet("background-color:transparent; color:blue;")
                self.browseWindButton.clicked.connect(lambda: self.populateBrowseTable('wind'))

        def setupBrowseTable(self):
                self.browseTable = QtWidgets.QTableWidget(self.browsePage)
                self.browseTable.setGeometry(QtCore.QRect(280, 130, 300, 600))
                self.browseTable.setObjectName("browseTable")

        def setupSearchPage(self):
                self.searchPage = QtWidgets.QWidget()
                self.searchPage.setObjectName("searchPage")
                self.searchLabel = QtWidgets.QLabel(self.searchPage)
                self.searchLabel.setGeometry(QtCore.QRect(390, 40, 51, 41))
                self.searchLabel.setObjectName("searchLabel")
                self.stackedWidget.addWidget(self.searchPage)

        def setupSearchPicLabel(self):
                self.searchPicLabel = QtWidgets.QLabel(self.searchPage)
                self.searchPicLabel.setGeometry(QtCore.QRect(0, 80, 300, 450))

        def setupSearchNameLabel(self):
                self.searchNameLabel = QtWidgets.QLabel(self.searchPage)
                self.searchNameLabel.setGeometry(QtCore.QRect(320, 70, 300, 40))

        def setupSearchDescriptionLabel(self):
                self.searchDescriptionLabel = QtWidgets.QLabel(self.searchPage)
                self.searchDescriptionLabel.setGeometry(QtCore.QRect(320, 20, 400, 400))
                self.searchDescriptionLabel.setWordWrap(True)

        def setupSearchPriceLabel(self):
                self.searchPriceLabel = QtWidgets.QLabel(self.searchPage)
                self.searchPriceLabel.setGeometry(QtCore.QRect(320, 500, 400, 40))
        
        def setupButtonAndInputText(self, _translate):
                button_texts = {
                        self.homeButton: "HOME",
                        self.browseButton: "BROWSE",
                        self.searchButton: "SEARCH",
                        self.randomButton: "RANDOMIZE"
                }
                for button, text in button_texts.items():
                        button.setText(_translate("mainWindow", text))

                input_placeholder = "Search Yu-Gi-Oh! Cards"
                self.searchInput.setPlaceholderText(_translate("mainWindow", input_placeholder))

                label_texts = {
                        self.homeDetailLabel: "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Free Yu-Gi-Oh! TCG Lookup Tool</span></p>"
                                                                  "<p><span style=\" font-size:10pt; font-weight:600;\"> Accurate card prices</span></p></body></html>",
                        self.browseLabel: "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">BROWSE</span></p></body></html>",
                        self.searchLabel: "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">SEARCH</span></p></body></html>",
                        self.top5Label: "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Top 5 Most Expensive Cards</span></p></body></html>"
                }
                for label, text in label_texts.items():
                        label.setText(_translate("mainWindow", text))
                
        def setupTop5Table(self):
                self.top5Table.setColumnCount(3)
                self.top5Table.setRowCount(5)
                self.top5Table.setColumnWidth(0, 300)
                self.top5Table.setColumnWidth(1, 400)
                self.top5Table.setColumnWidth(2, 85)
                for i in range(10):
                     self.top5Table.setRowHeight(i, 108)
                header_labels = ["", "Card", "Price"]
                self.top5Table.setHorizontalHeaderLabels(header_labels)

                for i in range(len(header_labels)):
                        header_item = self.top5Table.horizontalHeaderItem(i)
                        header_item.setTextAlignment(QtCore.Qt.AlignCenter)
        
        def populateBrowseCell(self, num_rows, data):
                buttonName = {}
                cardNames = {}
                for i in range(num_rows):
                        card = random.choice(data['data'])
                        while card['name'] in cardNames.values():
                                card = random.choice(data['data'])
                        cardNames[i] = card['name']
                        buttonName[i] = QtWidgets.QPushButton(self.browseTable)
                        buttonName[i].setText(card['name'])
                        buttonName[i].clicked.connect(lambda i=i, name=card['name']: self.search(name))
                        buttonName[i].setStyleSheet("background-color: transparent; color:blue;")
                        self.browseTable.setCellWidget(i, 0, buttonName[i])

        def populateBrowseTable(self, attribute):
                with open(f'{attribute}Attributes.json') as f:
                        data = json.load(f)
                        num_rows = 6 if attribute == 'divine' else 20
                        self.browseTable.setColumnCount(1)
                        self.browseTable.setRowCount(num_rows)
                        self.browseTable.setColumnWidth(0, 300)
                        for i in range(num_rows):
                                self.browseTable.setRowHeight(i, 25)
                        browse_headers = ["Card Name"]
                        self.browseTable.setHorizontalHeaderLabels(browse_headers)
                        self.populateBrowseCell(num_rows, data)
                        

        def setupLogo(self, mainWindow, _translate):
                mainWindow.setWindowTitle(_translate("mainWindow", "Yu-Gi-Oh! TCG Explorer"))
                self.logoTextLabel.setText(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \
                                                      \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                        "p, li { white-space: pre-wrap; }\n"
                        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:20pt; \
                                  font-weight:600; font-style:normal;\">\n"
                        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; \
                                -qt-block-indent:0; text-indent:0px;\">  Yu-Gi-Oh! </p>\n"
                        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; \
                                -qt-block-indent:0; text-indent:0px;\">TCG Explorer</p></body></html>"))
        
        def setPixmap(self, pixmap, label, link, row, item):
                label.setPixmap(pixmap)
                label.setScaledContents(True)
                label.setFixedSize(80, 105)
                label.setAlignment(QtCore.Qt.AlignCenter)
                self.top5Table.setCellWidget(row, 0, label)
                link.setText(item['name'])
                link.setFixedSize(400, 30)
                link.setStyleSheet("background-color: transparent; color:blue;")
                self.top5Table.setCellWidget(row, 1, link)

        def populateRow(self, row, item, names, label, link):
                picRequest = requests.get(f'http://yugiohprices.com/api/card_image/{item["name"]}')
                names[row] = item['name']
                if picRequest.status_code == 200:
                        with open('homepic1.jpg', 'wb') as f:
                                f.write(picRequest.content)
                else:
                        print('Error:', picRequest.status_code)
                pixmap = QPixmap('homepic1.jpg')
                self.setPixmap(pixmap, label, link, row, item)      
                link.clicked.connect(lambda: self.search(names[row]))
                self.top5Table.setItem(row, 2, QTableWidgetItem(str(item['price'])))
                self.top5Table.item(row, 2).setFlags(QtCore.Qt.ItemIsEnabled)

        def setupTop5PicLabel(self):
                self.picLabel0 = QtWidgets.QLabel(self.top5Table)
                self.picLabel1 = QtWidgets.QLabel(self.top5Table)       
                self.picLabel2 = QtWidgets.QLabel(self.top5Table)
                self.picLabel3 = QtWidgets.QLabel(self.top5Table)
                self.picLabel4 = QtWidgets.QLabel(self.top5Table)
                return self.picLabel0, self.picLabel1, self.picLabel2, self.picLabel3, self.picLabel4
        
        def setupTop5fCardLink(self):
                self.cardLink0 = QtWidgets.QPushButton(self.top5Label)     
                self.cardLink1 = QtWidgets.QPushButton(self.top5Label)   
                self.cardLink2 = QtWidgets.QPushButton(self.top5Label)
                self.cardLink3 = QtWidgets.QPushButton(self.top5Label)
                self.cardLink4 = QtWidgets.QPushButton(self.top5Label)
                return self.cardLink0, self.cardLink1, self.cardLink2, self.cardLink3, self.cardLink4
        
        def getTop5(self):
                response = requests.get('http://yugiohprices.com/api/top_100_cards')
                if response.status_code == 200:
                        data = response.json()
                        top_5_cards = data['data'][:5]
                else:
                        print('Error:', response.status_code)
                return top_5_cards

        def populateTop5Table(self):
                top_5_cards = self.getTop5()
                
                picLabel0, picLabel1, picLabel2, picLabel3, picLabel4 = self.setupTop5PicLabel()
                cardLink0, cardLink1, cardLink2, cardLink3,cardLink4 = self.setupTop5fCardLink()
                
                row = 0     
                names = [''] * 5
                for item in top_5_cards:
                        if item['name'] == 'Red Dragon Archfiend/Assault Mode':
                                item['name'] = 'Red Dragon Archfiend%2fAssault Mode'
                        if row == 0:
                                self.populateRow(row, item, names, picLabel0, cardLink0)
                        elif row == 1:
                                self.populateRow(row, item, names, picLabel1, cardLink1)
                        elif row == 2:
                                self.populateRow(row, item, names, picLabel2, cardLink2)
                        elif row == 3:
                                self.populateRow(row, item, names, picLabel3, cardLink3)
                        elif row == 4:
                                self.populateRow(row, item, names, picLabel4, cardLink4)
                        row += 1

        def getCardPic(self, name):
                try:
                        picRequest = requests.get(f'http://yugiohprices.com/api/card_image/{name}')
                        if picRequest.status_code == 200:
                                with open('searchpic.jpg', 'wb') as f:
                                        f.write(picRequest.content)
                                pixmap = QPixmap('searchpic.jpg')
                                self.searchPicLabel.setPixmap(pixmap)
                                self.searchPicLabel.setScaledContents(True)
                        else:
                                raise Exception(f'Error: {picRequest.status_code}')
                except Exception as e:
                        self.searchPicLabel.setText("Unavailable Image")
                        print(e)

        def getCardInfo(self, name):
                try:
                        cardRequest = requests.get(f'http://yugiohprices.com/api/card_data/{name}')
                        if cardRequest.status_code == 200:
                                data = cardRequest.json()
                                card_name = data['data']['name']
                                self.searchNameLabel.setText(f"<b>Name:</b>\n\n{card_name}")
                                card_description = data['data']['text']
                                self.searchDescriptionLabel.setText(card_description)
                        else:
                                raise Exception(f'Error: {cardRequest.status_code}')
                except Exception as e:
                        self.searchNameLabel.setText("Cannot find card")
                        self.searchDescriptionLabel.setText("Please search for a valid card name")
                        print(e)

        def getCardPrice(self, name):
                try:
                        priceRequest = requests.get(f'http://yugiohprices.com/api/get_card_prices/{name}')
                        if priceRequest.status_code == 200:
                                data = priceRequest.json()
                                card_price = data['data'][0]['price_data']['data']['prices']
                                self.searchPriceLabel.setText(f"<b>Price:</b> High:{card_price['high']}     Low:{card_price['low']}     Average:{card_price['average']}")
                        else:
                                raise Exception(f'Error: {priceRequest.status_code}')
                except Exception as e:
                        self.searchPriceLabel.setText("Cannot find card")
                        print(e)

        def search(self, name):
                self.stackedWidget.setCurrentIndex(2)
                self.getCardPic(name)
                self.getCardInfo(name)
                self.getCardPrice(name)

        def getRandomCard(self):
                response = requests.get("https://cs361-microservice.onrender.com/yugioh")
                if response.status_code == 200:
                        data = response.json()
                        name = data['name']
                        return name
                else:
                        print('Error:', response.status_code)


if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        mainWindow = QtWidgets.QMainWindow()
        ui = Ui_mainWindow()
        ui.setupUi(mainWindow)
        mainWindow.show()
        sys.exit(app.exec_())
