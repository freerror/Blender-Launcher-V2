# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window_design.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.HeaderLayout = QtWidgets.QHBoxLayout()
        self.HeaderLayout.setSpacing(0)
        self.HeaderLayout.setObjectName("HeaderLayout")
        self.SettingsButton = QtWidgets.QPushButton(self.centralwidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/icons/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.SettingsButton.setIcon(icon)
        self.SettingsButton.setIconSize(QtCore.QSize(32, 32))
        self.SettingsButton.setObjectName("SettingsButton")
        self.HeaderLayout.addWidget(self.SettingsButton, 0, QtCore.Qt.AlignLeft)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.HeaderLayout.addItem(spacerItem)
        self.TitleLabel = QtWidgets.QLabel(self.centralwidget)
        self.TitleLabel.setObjectName("TitleLabel")
        self.HeaderLayout.addWidget(self.TitleLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.HeaderLayout.addItem(spacerItem1)
        self.MinimizeButton = QtWidgets.QPushButton(self.centralwidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/resources/icons/minimize.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.MinimizeButton.setIcon(icon1)
        self.MinimizeButton.setIconSize(QtCore.QSize(32, 32))
        self.MinimizeButton.setObjectName("MinimizeButton")
        self.HeaderLayout.addWidget(self.MinimizeButton)
        self.CloseButton = QtWidgets.QPushButton(self.centralwidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/resources/icons/close.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.CloseButton.setIcon(icon2)
        self.CloseButton.setIconSize(QtCore.QSize(32, 32))
        self.CloseButton.setObjectName("CloseButton")
        self.HeaderLayout.addWidget(self.CloseButton)
        self.verticalLayout_2.addLayout(self.HeaderLayout)
        self.TabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.TabWidget.setObjectName("TabWidget")
        self.LibraryTab = QtWidgets.QWidget()
        self.LibraryTab.setObjectName("LibraryTab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.LibraryTab)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.LibraryToolBox = QtWidgets.QToolBox(self.LibraryTab)
        self.LibraryToolBox.setObjectName("LibraryToolBox")
        self.LibraryStablePage = QtWidgets.QWidget()
        self.LibraryStablePage.setGeometry(QtCore.QRect(0, 0, 634, 293))
        self.LibraryStablePage.setObjectName("LibraryStablePage")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.LibraryStablePage)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.LibraryStableListWidget = QtWidgets.QListWidget(self.LibraryStablePage)
        self.LibraryStableListWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.LibraryStableListWidget.setObjectName("LibraryStableListWidget")
        self.verticalLayout_7.addWidget(self.LibraryStableListWidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/resources/icons/page_opened.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.LibraryToolBox.addItem(self.LibraryStablePage, icon3, "")
        self.LibraryDailyPage = QtWidgets.QWidget()
        self.LibraryDailyPage.setGeometry(QtCore.QRect(0, 0, 634, 293))
        self.LibraryDailyPage.setObjectName("LibraryDailyPage")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.LibraryDailyPage)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.LibraryDailyListWidget = QtWidgets.QListWidget(self.LibraryDailyPage)
        self.LibraryDailyListWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.LibraryDailyListWidget.setObjectName("LibraryDailyListWidget")
        self.verticalLayout_9.addWidget(self.LibraryDailyListWidget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/resources/icons/page_closed.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.LibraryToolBox.addItem(self.LibraryDailyPage, icon4, "")
        self.LibraryExperimentalPage = QtWidgets.QWidget()
        self.LibraryExperimentalPage.setGeometry(QtCore.QRect(0, 0, 634, 293))
        self.LibraryExperimentalPage.setObjectName("LibraryExperimentalPage")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.LibraryExperimentalPage)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.LibraryExperimentalListWidget = QtWidgets.QListWidget(self.LibraryExperimentalPage)
        self.LibraryExperimentalListWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.LibraryExperimentalListWidget.setObjectName("LibraryExperimentalListWidget")
        self.verticalLayout_8.addWidget(self.LibraryExperimentalListWidget)
        self.LibraryToolBox.addItem(self.LibraryExperimentalPage, icon4, "")
        self.verticalLayout.addWidget(self.LibraryToolBox)
        self.TabWidget.addTab(self.LibraryTab, "")
        self.DownloadsTab = QtWidgets.QWidget()
        self.DownloadsTab.setObjectName("DownloadsTab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.DownloadsTab)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.DownloadsToolBox = QtWidgets.QToolBox(self.DownloadsTab)
        self.DownloadsToolBox.setObjectName("DownloadsToolBox")
        self.DownloadsStablePage = QtWidgets.QWidget()
        self.DownloadsStablePage.setGeometry(QtCore.QRect(0, 0, 634, 293))
        self.DownloadsStablePage.setObjectName("DownloadsStablePage")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.DownloadsStablePage)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.DownloadsStableListWidget = QtWidgets.QListWidget(self.DownloadsStablePage)
        self.DownloadsStableListWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.DownloadsStableListWidget.setObjectName("DownloadsStableListWidget")
        self.verticalLayout_4.addWidget(self.DownloadsStableListWidget)
        self.DownloadsToolBox.addItem(self.DownloadsStablePage, icon3, "")
        self.DownloadsDailyPage = QtWidgets.QWidget()
        self.DownloadsDailyPage.setGeometry(QtCore.QRect(0, 0, 98, 69))
        self.DownloadsDailyPage.setObjectName("DownloadsDailyPage")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.DownloadsDailyPage)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.DownloadsDailyListWidget = QtWidgets.QListWidget(self.DownloadsDailyPage)
        self.DownloadsDailyListWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.DownloadsDailyListWidget.setObjectName("DownloadsDailyListWidget")
        self.verticalLayout_5.addWidget(self.DownloadsDailyListWidget)
        self.DownloadsToolBox.addItem(self.DownloadsDailyPage, icon4, "")
        self.DownloadsExperimentalPage = QtWidgets.QWidget()
        self.DownloadsExperimentalPage.setGeometry(QtCore.QRect(0, 0, 98, 69))
        self.DownloadsExperimentalPage.setObjectName("DownloadsExperimentalPage")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.DownloadsExperimentalPage)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.DownloadsExperimentalListWidget = QtWidgets.QListWidget(self.DownloadsExperimentalPage)
        self.DownloadsExperimentalListWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.DownloadsExperimentalListWidget.setObjectName("DownloadsExperimentalListWidget")
        self.verticalLayout_6.addWidget(self.DownloadsExperimentalListWidget)
        self.DownloadsToolBox.addItem(self.DownloadsExperimentalPage, icon4, "")
        self.verticalLayout_3.addWidget(self.DownloadsToolBox)
        self.TabWidget.addTab(self.DownloadsTab, "")
        self.verticalLayout_2.addWidget(self.TabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.TabWidget.setCurrentIndex(0)
        self.LibraryToolBox.setCurrentIndex(0)
        self.LibraryToolBox.layout().setSpacing(0)
        self.DownloadsToolBox.setCurrentIndex(0)
        self.DownloadsToolBox.layout().setSpacing(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.TitleLabel.setText(_translate("MainWindow", "Blender Launcher"))
        self.LibraryToolBox.setItemText(self.LibraryToolBox.indexOf(self.LibraryStablePage), _translate("MainWindow", "Stable Releases"))
        self.LibraryToolBox.setItemText(self.LibraryToolBox.indexOf(self.LibraryDailyPage), _translate("MainWindow", "Daily Builds"))
        self.LibraryToolBox.setItemText(self.LibraryToolBox.indexOf(self.LibraryExperimentalPage), _translate("MainWindow", "Experimental Branches"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.LibraryTab), _translate("MainWindow", "Library"))
        self.DownloadsToolBox.setItemText(self.DownloadsToolBox.indexOf(self.DownloadsStablePage), _translate("MainWindow", "Stable Releases"))
        self.DownloadsToolBox.setItemText(self.DownloadsToolBox.indexOf(self.DownloadsDailyPage), _translate("MainWindow", "Daily Builds"))
        self.DownloadsToolBox.setItemText(self.DownloadsToolBox.indexOf(self.DownloadsExperimentalPage), _translate("MainWindow", "Experimental Branches"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.DownloadsTab), _translate("MainWindow", "Downloads"))

import resources.resources_rc
