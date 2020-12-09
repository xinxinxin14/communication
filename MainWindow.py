# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\program\Anaconda3\Lib\site-packages\pyqt5_tools\Qt\bin\MainWindow_communication.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(570, 581)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.client_button = QtWidgets.QPushButton(self.centralwidget)
        self.client_button.setObjectName("client_button")
        self.verticalLayout_6.addWidget(self.client_button)
        self.server_button = QtWidgets.QPushButton(self.centralwidget)
        self.server_button.setObjectName("server_button")
        self.verticalLayout_6.addWidget(self.server_button)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.main_stacked_widget = QtWidgets.QStackedWidget(self.centralwidget)
        self.main_stacked_widget.setObjectName("main_stacked_widget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.server_frame = QtWidgets.QFrame(self.page)
        self.server_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.server_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.server_frame.setObjectName("server_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.server_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.server_text_edit = QtWidgets.QTextEdit(self.server_frame)
        self.server_text_edit.setReadOnly(True)
        self.server_text_edit.setObjectName("server_text_edit")
        self.verticalLayout.addWidget(self.server_text_edit)
        self.server_config_groupbox = QtWidgets.QGroupBox(self.server_frame)
        self.server_config_groupbox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.server_config_groupbox.sizePolicy().hasHeightForWidth())
        self.server_config_groupbox.setSizePolicy(sizePolicy)
        self.server_config_groupbox.setCheckable(True)
        self.server_config_groupbox.setChecked(False)
        self.server_config_groupbox.setObjectName("server_config_groupbox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.server_config_groupbox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.server_port_label = QtWidgets.QLabel(self.server_config_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.server_port_label.sizePolicy().hasHeightForWidth())
        self.server_port_label.setSizePolicy(sizePolicy)
        self.server_port_label.setObjectName("server_port_label")
        self.gridLayout_2.addWidget(self.server_port_label, 1, 0, 1, 1)
        self.server_ip_combobox = QtWidgets.QComboBox(self.server_config_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.server_ip_combobox.sizePolicy().hasHeightForWidth())
        self.server_ip_combobox.setSizePolicy(sizePolicy)
        self.server_ip_combobox.setObjectName("server_ip_combobox")
        self.gridLayout_2.addWidget(self.server_ip_combobox, 0, 1, 1, 1)
        self.server_port_line_edit = QtWidgets.QLineEdit(self.server_config_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.server_port_line_edit.sizePolicy().hasHeightForWidth())
        self.server_port_line_edit.setSizePolicy(sizePolicy)
        self.server_port_line_edit.setObjectName("server_port_line_edit")
        self.gridLayout_2.addWidget(self.server_port_line_edit, 1, 1, 1, 1)
        self.server_ip_label = QtWidgets.QLabel(self.server_config_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.server_ip_label.sizePolicy().hasHeightForWidth())
        self.server_ip_label.setSizePolicy(sizePolicy)
        self.server_ip_label.setObjectName("server_ip_label")
        self.gridLayout_2.addWidget(self.server_ip_label, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 3, 1, 1)
        self.verticalLayout.addWidget(self.server_config_groupbox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.start_bind_button = QtWidgets.QPushButton(self.server_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_bind_button.sizePolicy().hasHeightForWidth())
        self.start_bind_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(16)
        self.start_bind_button.setFont(font)
        self.start_bind_button.setObjectName("start_bind_button")
        self.horizontalLayout.addWidget(self.start_bind_button)
        self.stop_bind_button = QtWidgets.QPushButton(self.server_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stop_bind_button.sizePolicy().hasHeightForWidth())
        self.stop_bind_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(16)
        self.stop_bind_button.setFont(font)
        self.stop_bind_button.setObjectName("stop_bind_button")
        self.horizontalLayout.addWidget(self.stop_bind_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 10)
        self.verticalLayout.setStretch(1, 3)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout_3.addWidget(self.server_frame)
        self.main_stacked_widget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.client_frame = QtWidgets.QFrame(self.page_2)
        self.client_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.client_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.client_frame.setObjectName("client_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.client_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.client_text_edit = QtWidgets.QTextEdit(self.client_frame)
        self.client_text_edit.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.client_text_edit.setReadOnly(True)
        self.client_text_edit.setObjectName("client_text_edit")
        self.verticalLayout_2.addWidget(self.client_text_edit)
        self.client_config_groupbox = QtWidgets.QGroupBox(self.client_frame)
        self.client_config_groupbox.setEnabled(True)
        self.client_config_groupbox.setCheckable(True)
        self.client_config_groupbox.setChecked(False)
        self.client_config_groupbox.setObjectName("client_config_groupbox")
        self.gridLayout = QtWidgets.QGridLayout(self.client_config_groupbox)
        self.gridLayout.setObjectName("gridLayout")
        self.server_port_line_edit_in_client = QtWidgets.QLineEdit(self.client_config_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.server_port_line_edit_in_client.sizePolicy().hasHeightForWidth())
        self.server_port_line_edit_in_client.setSizePolicy(sizePolicy)
        self.server_port_line_edit_in_client.setObjectName("server_port_line_edit_in_client")
        self.gridLayout.addWidget(self.server_port_line_edit_in_client, 1, 1, 1, 1)
        self.server_ip_line_edit_in_client = QtWidgets.QLineEdit(self.client_config_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.server_ip_line_edit_in_client.sizePolicy().hasHeightForWidth())
        self.server_ip_line_edit_in_client.setSizePolicy(sizePolicy)
        self.server_ip_line_edit_in_client.setObjectName("server_ip_line_edit_in_client")
        self.gridLayout.addWidget(self.server_ip_line_edit_in_client, 0, 1, 1, 1)
        self.server_port_label_in_client = QtWidgets.QLabel(self.client_config_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.server_port_label_in_client.sizePolicy().hasHeightForWidth())
        self.server_port_label_in_client.setSizePolicy(sizePolicy)
        self.server_port_label_in_client.setObjectName("server_port_label_in_client")
        self.gridLayout.addWidget(self.server_port_label_in_client, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 3, 1, 1)
        self.server_ip_label_in_client = QtWidgets.QLabel(self.client_config_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.server_ip_label_in_client.sizePolicy().hasHeightForWidth())
        self.server_ip_label_in_client.setSizePolicy(sizePolicy)
        self.server_ip_label_in_client.setObjectName("server_ip_label_in_client")
        self.gridLayout.addWidget(self.server_ip_label_in_client, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.client_config_groupbox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ready_button = QtWidgets.QPushButton(self.client_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ready_button.sizePolicy().hasHeightForWidth())
        self.ready_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(16)
        self.ready_button.setFont(font)
        self.ready_button.setObjectName("ready_button")
        self.horizontalLayout_2.addWidget(self.ready_button)
        self.finish_button = QtWidgets.QPushButton(self.client_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.finish_button.sizePolicy().hasHeightForWidth())
        self.finish_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(16)
        self.finish_button.setFont(font)
        self.finish_button.setObjectName("finish_button")
        self.horizontalLayout_2.addWidget(self.finish_button)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.setStretch(0, 10)
        self.verticalLayout_2.setStretch(1, 3)
        self.verticalLayout_2.setStretch(2, 2)
        self.verticalLayout_5.addWidget(self.client_frame)
        self.main_stacked_widget.addWidget(self.page_2)
        self.horizontalLayout_3.addWidget(self.main_stacked_widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 570, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.main_stacked_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.client_button.setText(_translate("MainWindow", "远端"))
        self.server_button.setText(_translate("MainWindow", "近端"))
        self.server_config_groupbox.setTitle(_translate("MainWindow", "配置"))
        self.server_port_label.setText(_translate("MainWindow", "端口:"))
        self.server_port_line_edit.setText(_translate("MainWindow", "12345"))
        self.server_ip_label.setText(_translate("MainWindow", "近端ip:"))
        self.start_bind_button.setText(_translate("MainWindow", "开始连接"))
        self.stop_bind_button.setText(_translate("MainWindow", "断开连接"))
        self.client_config_groupbox.setTitle(_translate("MainWindow", "配置"))
        self.server_port_line_edit_in_client.setText(_translate("MainWindow", "12345"))
        self.server_ip_line_edit_in_client.setText(_translate("MainWindow", "192.168.1.1"))
        self.server_port_label_in_client.setText(_translate("MainWindow", "端口:"))
        self.server_ip_label_in_client.setText(_translate("MainWindow", "近端ip:"))
        self.ready_button.setText(_translate("MainWindow", "已准备"))
        self.finish_button.setText(_translate("MainWindow", "测试完成"))