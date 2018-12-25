#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Python界面模板 """

__author__ = 'Shu Xu'

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
from mainwindow import Ui_MainWindow
from dialog import Ui_Dialog


class NewMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    # 初始化主窗口
    def __init__(self):
        self.App = QtWidgets.QApplication(sys.argv)
        super(NewMainWindow, self).__init__()
        self.setupUi(self)
        self._load_wel_image()
        self.widget1.hide()
        self.widget2.hide()
        self.function()
        self.show()
        self.quit()

    # 加载欢迎图片
    def _load_wel_image(self):
        if os.path.exists(".\\welcome.jpg"):
            image = QtGui.QPixmap(".\\welcome.jpg")
            self.welcome.setPixmap(image)
            self.welcome.setScaledContents(True)

    # 定义功能项
    def function(self):
        self.quit_button.clicked.connect(self.close)
        self.calculate_button.clicked.connect(self._plus)
        self.form1_button.clicked.connect(self._display_form1)
        self.form2_button.clicked.connect(self._display_form2)
        self.open_button.clicked.connect(self._open_dialog)

    # 退出主窗口
    def quit(self):
        if self.App.exec_():
            sys.exit()
        else:
            pass

    # 关闭主窗口时的动作
    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, '提示', '确定要退出吗?', QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    # 界面1功能：加法计算器
    def _plus(self):
        text1 = self.value_1.text()
        text2 = self.value_2.text()
        if text1 == '' or text2 == '':
            QtWidgets.QMessageBox.warning(self, "警告", '请正确输入。', QtWidgets.QMessageBox.Yes)
        else:
            sum = int(text1) + int(text2)
            self.value_sum.setText(str(sum))

    # 进入界面1
    def _display_form1(self):
        self.wel_widget.hide()
        self.widget2.hide()
        self.widget1.show()

    # 进入界面2
    def _display_form2(self):
        self._sync()
        self.wel_widget.hide()
        self.widget1.hide()
        self.widget2.show()

    # 主窗口功能：打开对话框
    def _open_dialog(self):
        dialog = NewDialog(self.display1.text(), self.display2.value())
        dialog.Signal1.connect(self._get_dialog_text)
        dialog.Signal2.connect(self._get_dialog_value)
        dialog.exec_()

    # 主窗口功能：显示对话框字符
    def _get_dialog_text(self, connect):
        self.display1.setText(connect)

    # 主窗口功能：显示对话框数值
    def _get_dialog_value(self, connect):
        self.display2.setValue(connect)

    # 同步界面1的内容至界面2
    def _sync(self):
        num = self.value_sum.text()
        if num != '':
            self.sum_display.display(int(num))


class NewDialog(QtWidgets.QDialog, Ui_Dialog):
    # 设置数据传递通道
    Signal1 = QtCore.pyqtSignal(str)
    Signal2 = QtCore.pyqtSignal(int)

    # 初始化对话框
    def __init__(self, info_pre, value_pre):
        super(NewDialog, self).__init__()
        self.setupUi(self)
        self.info.setText(info_pre)
        self.value.setValue(value_pre)
        self.function()

    # 定义功能项
    def function(self):
        self.cancel_button.clicked.connect(self.close)
        self.confirm_button.clicked.connect(self._confirm)

    # 对话框功能：传递数据
    def _confirm(self):
        self.Signal1.emit(self.info.text())
        self.Signal2.emit(self.value.value())
        self.close()


if __name__ == '__main__':
    NewMainWindow()
