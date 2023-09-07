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
        self.b_smn_lang.clicked.connect(self.smn_lang)
        self.b_sl_pod.clicked.connect(self.sl_pod)
        self.b_vyp.clicked.connect(self.comply)

    def smn_lang(self):
        lang = self.vibor_lang.currentText()
        if lang == "Русский":
            self.txt_vvod.setText("Ввод:")
            self.b_vyp.setText("Выполнить")
            self.text_otvet.setText("Ответ:")
            self.text_toch.setText("Точность:")
            self.b_sl_pod.setText("Служба поддержки")
            self.txt_lang.setText("Язык:")
        elif lang == "English":
            self.txt_vvod.setText("Input:")
            self.b_vyp.setText("Comply")
            self.text_otvet.setText("Result:")
            self.text_toch.setText("Accuracy:")
            self.b_sl_pod.setText("Support service")
            self.txt_lang.setText("Language:")
        elif lang == "中文":
            self.txt_vvod.setText("输入:")
            self.b_vyp.setText("表演/表演")
            self.text_otvet.setText("回答:")
            self.text_toch.setText("准确度:")
            self.b_sl_pod.setText("支援服务")
            self.txt_lang.setText("语言:")
        elif lang == "Español":
            self.txt_vvod.setText("Entrada:")
            self.b_vyp.setText("Ejecutar")
            self.text_otvet.setText("Resultado:")
            self.text_toch.setText("Precisión:")
            self.b_sl_pod.setText("Servicio al cliente")
            self.txt_lang.setText("Idioma:")

    def test_number(self, vvod):
        true = "0123456789"
        count_vern = 0
        for el in vvod:
            if el in true:
                count_vern += 1
        return count_vern == len(vvod)


    def sl_pod(self):
        url = QUrl("https://www.hse.ru/org/persons/4200771")
        QDesktopServices.openUrl(url)

    def comply(self):
        vvod1 = self.vvod_otvet.toPlainText()
        vvod2 = self.vvod_toch.toPlainText()
        if (self.test_number(vvod1)) and (self.test_number(vvod2)):
            if vvod2 == "":
                self.vivid_otvet.setText(str(sqrt(int(vvod1))))
            else:
                self.vivid_otvet.setText(str(round(sqrt(int(vvod1)), int(vvod2))))
        else:
            self.vivid_otvet.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    screen_1 = Screen_1()
    widget.addWidget(screen_1)
    widget.setFixedHeight(576)
    widget.setFixedWidth(1024)
    widget.show()
    sys.exit(app.exec_())


