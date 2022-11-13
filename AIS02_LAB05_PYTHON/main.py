#!/usr/bin/env python3
# coding=utf-8

import re
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

list_of_numbers = []


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('uis/main.ui', self)

        self.setWindowTitle('Работа с массивами и файлами в Python')
        self.setWindowIcon(QtGui.QIcon('image/logo.png'))

        self.btn_upload_data.clicked.connect(self.upload_data_from_file)
        self.btn_process_data.clicked.connect(self.process_data)
        self.btn_save_data.clicked.connect(self.save_data_in_file)
        self.btn_clear.clicked.connect(self.clear)

    def upload_data_from_file(self):
        """
        загружаем данные из файла
        :return: pass
        """
        global path_to_file
        path_to_file = QFileDialog.getOpenFileName(self, 'Открыть файл', '', "Text Files (*.txt)")[0]
        self.plainTextEdit.setPlainText("")
        if path_to_file:
            file = open(path_to_file, 'r')

            data = file.readlines()
            # выводим считанные данные на экран
            self.plainTextEdit.appendPlainText("Полученные данные: ")

            for lines in data:
                self.plainTextEdit.appendPlainText(lines.strip('\n'))

            global list_of_numbers
            list_of_numbers = []

            for lines in data:
                lineSplit = lines.split()
                list_of_numbers.append(lineSplit)

    def process_data(self):
        if validation_of_data():
            min_num, minj = find_min()

            # -*- выполнение задания -*-
            if minj == 1:
                for i in range(len(list_of_numbers)):
                    list_of_numbers[i][1] = 0

                self.plainTextEdit.appendPlainText("Данные обработаны! " + '\n')

                # выводим список на экран
                for lists in list_of_numbers:
                    for i in lists:
                        new_str = "{:5}".format(str(i))
                        self.plainTextEdit.insertPlainText(new_str)
                        # чтобы текст был в виде таблицы, делаем отступ после
                        # 6 элемента

                    self.plainTextEdit.appendPlainText("")
            else:
                self.plainTextEdit.appendPlainText(
                    "Минимальный элемент не стоит во втором столбце! \n")
        else:
            self.plainTextEdit.appendPlainText("Неправильно введены данные! "
                                               "Таблица должна быть размером "
                                               "5х5 и состоять из чисел! \n")

    def save_data_in_file(self):
        """
        сохраняем данные в выбранный нами файл
        :return:
        """

        if path_to_file:
            file = open(path_to_file.split(".")[0] + '-Output.txt', 'w')

            for lists in list_of_numbers:
                for i in lists:
                    new_str = "{:6}".format(str(i))
                    file.write(new_str)
                file.write("\n")

            file.close()

            self.plainTextEdit.appendPlainText("Файл был успешно загружен! \n")
        else:
            self.plainTextEdit.appendPlainText("Для начала загрузите файл!")

    def clear(self):
        self.plainTextEdit.clear()


def find_min():
    """
    находим минимальное число в списке
    :return: миниимальное число
    """
    min_num = list_of_numbers[0][0]
    minj = 0
    for i in range(len(list_of_numbers)):
        for j in range(len(list_of_numbers[i])):
            if min_num > list_of_numbers[i][j]:
                min_num = list_of_numbers[i][j]
                minj = j
    return min_num, minj


def validation_of_data():
    """
    проверяем данные на валидность: всего должно быть ровно 30 ЧИСЕЛ
    :return: True - данные корректны, False - нет
    """
    lenth_list = 0
    for lists in list_of_numbers:
        lenth_list += len(lists)
    if lenth_list == 25:
        for lists in list_of_numbers:
            for i in lists:
                try:
                    int(i)
                except Exception:
                    return False
        return True
    else:
        return False


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()