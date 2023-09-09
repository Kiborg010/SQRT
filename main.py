import sys
from math import sqrt
from PyQt5.Qt import QUrl, QDesktopServices
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets, QtGui
from window import Ui_MainWindow
import numexpr as ne


class Screen_1(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_change_lang.clicked.connect(self.change_lang)
        self.btn_sup_serv.clicked.connect(self.sup_serv)
        self.btn_comply.clicked.connect(self.comply)
        self.btn_clear.clicked.connect(self.clear)

    def change_lang_base(self, tx_input, comply, result, detail, sup_serv, lang, clear, error_act, error):
        self.text_input.setText(tx_input)
        self.btn_comply.setText(comply)
        self.text_result.setText(result)
        self.text_detail.setText(detail)
        self.btn_sup_serv.setText(sup_serv)
        self.text_lang.setText(lang)
        self.btn_clear.setText(clear)
        if not (error_act):
            self.text_error.setText(error)

    def change_lang(self):
        lang = self.choice_lang.currentText()
        if lang == "Русский":
            self.change_lang_base("Ввод:", "Выполнить", "Ответ:", "Точность:", "Служба поддержки", "Язык:", "Очистить",
                                  self.text_error.toPlainText() == "", "Ошибка ввода")
        elif lang == "English":
            self.change_lang_base("Input:", "Comply", "Result:", "Accuracy:", "Support service", "Language:", "Clear",
                                  self.text_error.toPlainText() == "", "Input error")
        elif lang == "中文":
            self.change_lang_base("输入:", "表演/表演", "回答:", "准确度:", "支援服务", "语言:", "擦除",
                                  self.text_error.toPlainText() == "", "输入错误")
        elif lang == "Español":
            self.change_lang_base("Entrada:", "Ejecutar", "Resultado:", "Precisión:", "Servicio al cliente", "Idioma:",
                                  "Barrer",
                                  self.text_error.toPlainText() == "", "Error de entrada")

    def sup_serv(self):
        url = QUrl("https://www.hse.ru/org/persons/4200771")
        QDesktopServices.openUrl(url)

    def give_error(self):
        dict_lang_error = {"Русский": "Ошибка ввода", "English": "Input error", "Español": "Error de entrada",
                           "中文": "输入错误"}
        key_lang = self.choice_lang.currentText()
        self.text_error.setText(dict_lang_error[key_lang])

    def comply(self):
        try:
            if self.input_detail.toPlainText() == "":
                input_detail = 0
            else:
                input_detail = int(ne.evaluate(self.input_detail.toPlainText()))
            if input_detail == 0:
                res = sqrt(ne.evaluate(self.input_data.toPlainText()))
            else:
                res = round(sqrt(ne.evaluate(self.input_data.toPlainText())), input_detail)
            self.result.setText(str(res))
            self.text_error.setText("")
        except KeyError:
            self.give_error()
        except SyntaxError:
            self.give_error()
        except TypeError:
            self.give_error()
        except ValueError:
            self.give_error()

    def clear(self):
        self.input_data.setText("")
        self.result.setText("")
        self.text_error.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    screen_1 = Screen_1()
    widget.addWidget(screen_1)
    widget.setWindowTitle("Square")
    widget.setWindowIcon(QtGui.QIcon("data/icon.png"))
    widget.setFixedHeight(576)
    widget.setFixedWidth(1024)
    widget.show()
    sys.exit(app.exec_())
