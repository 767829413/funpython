from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton

app = QApplication([])
main_window = QMainWindow()
main_window.resize(480, 360)


def show_msg():
    QMessageBox.information(main_window, "信息提示框", "ok,弹出测试信息")


btn = QPushButton("测试点击按钮", main_window)
btn.clicked.connect(show_msg)

main_window.show()
app.exec_()
