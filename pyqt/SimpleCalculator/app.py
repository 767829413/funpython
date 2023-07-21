from PyQt5.QtWidgets import *
from untitled import Ui_MainWindow
from logic import CalLogic


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MyMainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.cal = CalLogic(self.lcdNumber)
        self.do_signal_slot()

        self.cal.init_cal()

    def do_signal_slot(self):
        """给数字0~9建立click信号和槽函数"""
        self.pushButton_0.clicked.connect(lambda: self.cal.number_slot(0))
        self.pushButton_1.clicked.connect(lambda: self.cal.number_slot(1))
        self.pushButton_2.clicked.connect(lambda: self.cal.number_slot(2))
        self.pushButton_3.clicked.connect(lambda: self.cal.number_slot(3))
        self.pushButton_4.clicked.connect(lambda: self.cal.number_slot(4))
        self.pushButton_5.clicked.connect(lambda: self.cal.number_slot(5))
        self.pushButton_6.clicked.connect(lambda: self.cal.number_slot(6))
        self.pushButton_7.clicked.connect(lambda: self.cal.number_slot(7))
        self.pushButton_8.clicked.connect(lambda: self.cal.number_slot(8))
        self.pushButton_9.clicked.connect(lambda: self.cal.number_slot(9))

        """给+-*/建立click信号和槽函数"""
        self.pushButton_add.clicked.connect(lambda: self.cal.operation_slot("+"))
        self.pushButton_sub.clicked.connect(lambda: self.cal.operation_slot("-"))
        self.pushButton_mul.clicked.connect(lambda: self.cal.operation_slot("*"))
        self.pushButton_div.clicked.connect(lambda: self.cal.operation_slot("/"))

        """给/100建立click信号和槽函数"""
        self.pushButton_perc.clicked.connect(self.cal.perc_slot)

        """给RE M MR建立click信号和槽函数"""
        self.pushButton_RE.clicked.connect(self.cal.re_slot)
        self.pushButton_M.clicked.connect(self.cal.m_slot)
        self.pushButton_MR.clicked.connect(self.cal.mr_slot)

        """给=建立click信号和槽函数"""
        self.pushButton_eq.clicked.connect(self.cal.eq_slot)


if __name__ == "__main__":
    app = QApplication([])

    window = MyMainWindow()
    window.setWindowTitle("旺财")
    window.show()
    app.exec_()
