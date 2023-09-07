import sys
from math import sqrt
from PyQt5.Qt import QUrl, QDesktopServices
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
from window import Ui_MainWindow


class Screen_1(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_change_lang.clicked.connect(self.change_lang)
        self.btn_sup_serv.clicked.connect(self.sup_serv)
        self.btn_comply.clicked.connect(self.comply)
        self.btn_clear.clicked.connect(self.clear)

    def change_lang(self):
        lang = self.choice_lang.currentText()
        if lang == "Русский":
            self.text_input.setText("Ввод:")
            self.btn_comply.setText("Выполнить")
            self.text_result.setText("Ответ:")
            self.text_detail.setText("Точность:")
            self.btn_sup_serv.setText("Служба поддержки")
            self.text_lang.setText("Язык:")
            self.btn_clear.setText("Очистить")
        elif lang == "English":
            self.text_input.setText("Input:")
            self.btn_comply.setText("Comply")
            self.text_result.setText("Result:")
            self.text_detail.setText("Accuracy:")
            self.btn_sup_serv.setText("Support service")
            self.text_lang.setText("Language:")
            self.btn_clear.setText("Clear")
        elif lang == "中文":
            self.text_input.setText("输入:")
            self.btn_comply.setText("表演/表演")
            self.text_result.setText("回答:")
            self.text_detail.setText("准确度:")
            self.btn_sup_serv.setText("支援服务")
            self.text_lang.setText("语言:")
            self.btn_clear.setText("擦除")
        elif lang == "Español":
            self.text_input.setText("Entrada:")
            self.btn_comply.setText("Ejecutar")
            self.text_result.setText("Resultado:")
            self.text_detail.setText("Precisión:")
            self.btn_sup_serv.setText("Servicio al cliente")
            self.text_lang.setText("Idioma:")
            self.btn_clear.setText("Barrer")

    def test_number(self, input):
        true = "0123456789"
        count_true = 0
        for el in input:
            if el in true:
                count_true += 1
        return count_true == len(input)

    def sup_serv(self):
        url = QUrl("https://www.hse.ru/org/persons/4200771")
        QDesktopServices.openUrl(url)

    def comply(self):
        input_data = self.input_data.toPlainText()
        input_detail = self.input_detail.toPlainText()
        if (self.test_number(input_data)) and (self.test_number(input_detail)):
            if input_detail == "":
                self.result.setText(str(sqrt(int(input_data))))
            else:
                self.result.setText(str(round(sqrt(int(input_data)), int(input_detail))))
        else:
            self.result.setText("")

    def clear(self):
        self.input_data.setText("")
        self.result.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    screen_1 = Screen_1()
    widget.addWidget(screen_1)
    widget.setFixedHeight(576)
    widget.setFixedWidth(1024)
    widget.show()
    sys.exit(app.exec_())
