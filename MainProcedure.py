# -*- coding: utf-8 -*-
import socket
from PyQt5 import QtCore, QtGui, QtWidgets
from MainWindow import Ui_MainWindow
import sys
import time

class MainWindowImproved(QtWidgets.QMainWindow):
    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self,
                                               '确认退出',
                                               "是否退出程序？",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.Yes)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
            
        else:
            event.ignore()

class MainWindow_UI(MainWindowImproved, Ui_MainWindow):
    def __init__(self, MainWindow):
        super(MainWindow_UI,self).__init__()
        self.setupUi(MainWindow)
        settings = self.read_config()
        server_port = settings.value("ServerPort")
        server_ip_in_client = settings.value("ServerIPInClient")
        server_port_in_client = settings.value("ServerPortInClient")
        stacked_widget_index = settings.value("StackedWidgetIndex")
        if server_port:
            self.server_port_line_edit.setText(server_port)
        if server_ip_in_client:
            self.server_ip_line_edit_in_client.setText(server_ip_in_client)
        if server_port_in_client:
            self.server_port_line_edit_in_client.setText(server_port_in_client)
        if stacked_widget_index:
            self.main_stacked_widget.setCurrentIndex(int(stacked_widget_index))
        ip_list = self.get_ip_list()
        self.server_ip_combobox.addItems(ip_list)
        self.server_button.clicked.connect(self.show_frame)
        self.client_button.clicked.connect(self.show_frame)
        self.ready_button.clicked.connect(self.send_ready)
        self.finish_button.clicked.connect(self.send_finish)
        self.start_bind_button.clicked.connect(self.start_listen)
        self.stop_bind_button.clicked.connect(self.stop_listen)
        self.stop_bind_button.setDisabled(True)
        self.start_bind_button.setEnabled(True)
        self.server_port_line_edit_in_client.editingFinished.connect(self.save_config)
        self.server_ip_line_edit_in_client.editingFinished.connect(self.save_config)
        self.server_port_line_edit.editingFinished.connect(self.save_config)
        self.main_stacked_widget.currentChanged.connect(self.save_config)


    def print_server_data(self, data):
        self.server_text_edit.append("<font color=\"#00FF00\">{}</font> ".format(data))

    def print_server_warn(self, warn_msg):
        self.server_text_edit.append("<font color=\"#0000FF\">{}</font> ".format(warn_msg))

    def print_server_error(self, error_msg):
        self.server_text_edit.append("<font color=\"#FF0000\">{}</font>".format(error_msg))

    def print_client_data(self, data):
        self.client_text_edit.append("<font color=\"#00FF00\">{}</font> ".format(data))

    def print_client_error(self, error_msg):
        self.client_text_edit.append("<font color=\"#FF0000\">{}</font>".format(error_msg))

    @staticmethod
    def get_ip_list():
        addrs = socket.getaddrinfo(socket.gethostname(), None)
        ip_list = [item[4][0] for item in addrs if ":" not in item[4][0]]
        return ip_list
    def show_frame(self):
        frame_dict = {
            "server_button":0,
            "client_button":1
        }
        index = frame_dict[self.sender().objectName()]
        self.main_stacked_widget.setCurrentIndex(index)

    def start_listen(self):
        self.start_bind_button.setDisabled(True)
        self.stop_bind_button.setEnabled(True)
        self.server_ip = self.server_ip_combobox.currentText()
        self.server_port = int(self.server_port_line_edit.text())
        self.server_thread = ServerThread((self.server_ip, self.server_port))
        self.server_thread.start()
        self.server_thread._data.connect(self.print_server_data)
        self.server_thread._error.connect(self.print_server_error)
        self.server_thread._warn.connect(self.print_server_warn)

    def stop_listen(self):
        self.server_thread.stop()
        self.stop_bind_button.setDisabled(True)
        self.start_bind_button.setEnabled(True)

    def send_ready(self):
        self.server_ip_in_client = self.server_ip_line_edit_in_client.text()
        self.server_port_in_client = int(self.server_port_line_edit_in_client.text())
        addr = (self.server_ip_in_client, self.server_port_in_client)
        data = "对方已准备"
        self.client_thread = ClientThread(addr, data)
        self.client_thread.start()
        self.client_thread._data.connect(self.print_client_data)
        self.client_thread._error.connect(self.print_client_error)

    def send_finish(self):
        self.server_ip_in_client = self.server_ip_line_edit_in_client.text()
        self.server_port_in_client = int(self.server_port_line_edit_in_client.text())
        addr = (self.server_ip_in_client, self.server_port_in_client)
        data = "对方测试完成"
        self.client_thread = ClientThread(addr, data)
        self.client_thread.start()
        self.client_thread._data.connect(self.print_client_data)
        self.client_thread._error.connect(self.print_client_error)
    
    def save_config(self):
        setting = QtCore.QSettings("config.ini", QtCore.QSettings.IniFormat)
        setting.setValue("ServerIPInClient", self.server_ip_line_edit_in_client.text())
        setting.setValue("ServerPortInClient", self.server_port_line_edit_in_client.text())
        setting.setValue("ServerPort", self.server_port_line_edit.text())
        setting.setValue("StackedWidgetIndex", self.main_stacked_widget.currentIndex())

    def read_config(self):
        settings = QtCore.QSettings("config.ini", QtCore.QSettings.IniFormat)
        return settings


class ServerThread(QtCore.QThread):
    _data = QtCore.pyqtSignal(str)
    _error = QtCore.pyqtSignal(str)
    _warn = QtCore.pyqtSignal(str)
    def __init__(self, addr):
        QtCore.QThread.__init__(self)
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(addr)
        self.server.listen(2)
        self.server.settimeout(1)

    def run(self):
        bufsize = 1024
        warn_start_msg = "正在等待对方确认..."
        self._warn.emit(warn_start_msg)
        latest_connected_time = time.time()
        while 1:
            try:
                data = ""
                client, _addr = self.server.accept()
                data = client.recv(bufsize)
            except Exception as e:
                if type(e) == socket.timeout:
                    pass
                else:
                    self._error.emit(str(e))
            if data:
                self._data.emit(data.decode())
                client.sendall("对方已接收".encode())
                latest_connected_time = time.time()
            else:
                if time.time() - latest_connected_time > 20:
                    data = "正在等待对方重新确认..."
                    self._warn.emit(data)
                    latest_connected_time = time.time()
                # else:
                #     self._warn.emit(str(time.time() - latest_connected_time))
  
    def stop(self):
        print("close thread")
        self.terminate()
        self.server.close()

class ClientThread(QtCore.QThread):
    _data = QtCore.pyqtSignal(str)
    _error = QtCore.pyqtSignal(str)
    def __init__(self, addr, data):
        QtCore.QThread.__init__(self)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.settimeout(1)
        self.addr = addr
        self.data = data

    def run(self):
        try:
            self.client.connect(self.addr)
            self.client.sendall(self.data.encode())
            bufsize = 1024
            # timeout = 1
            data = self.client.recv(bufsize)
            if data:
                print(data.decode())
                self._data.emit(data.decode())
            self.client.close()
        except Exception as e:
            if type(e) == socket.timeout:
                pass
            else:
                self._error.emit(str(e))
            self.client.close()
  
    def stop(self):
        print("close thread")
        self.client.close()
        self.terminate()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindowImproved()
    app.setStyle("Fusion")
    ui = MainWindow_UI(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())