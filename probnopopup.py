import PySide6.QtGui
from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget, QDialog, QPushButton, QApplication, QLineEdit, QVBoxLayout
from PySide6.QtCore import QTimer, Qt, Signal, QObject
from myvar import myVar as mv


class ProbNo(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('승인번호')
        self.edit = MyLineEdit()
        self.edit.setText('승인 번호를 입력하세요!!!')
        self.edit.selectAll()
        self.button = QPushButton('O K !')
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        # self.showEvent()
        self.setLayout(layout)
        self.button.clicked.connect(self.sendProbNo)

    def sendProbNo(self):
        try:
            mv.PROBNO = int(self.edit.text())
            print(f'prob no는 {mv.PROBNO}')
            mv.WAITCONDITION.wakeAll()
            # self.close()
            self.done(0)
            # self.reject()
        except:
            mv.PROBNO = 0

    def showEvent(self, event):
        super().showEvent(event)
        self.setFocus()

    def setFocus(self):
        self.activateWindow()
        self.raise_()
        self.show()


class MyLineEdit(QLineEdit):
    inputcharary = ''

    def __init__(self, parent=None):
        super(MyLineEdit, self).__init__(parent)
        # self.setStyleSheet('color: rgb(255,0,0)')
        self.setStyleSheet(
            'selection-background-color: red;')
        self._timer = QTimer(self)
        self._timer.timeout.connect(self.toggle_text_visibility)
        self._is_visible = True

        self.start_blinking()
        # self.setStyleSheet('blink')

    # def focusInEvent(self, e):
    #     self.selectAll()

    def start_blinking(self, interval_ms=500):
        self._timer.start(interval_ms)

    def stop_blinking(self):
        self._timer.stop()
        self._is_visible = True
        self.repaint()

    def toggle_text_visibility(self):
        self._is_visible = not self._is_visible
        self.repaint()

    def paintEvent(self, event):
        if self._is_visible:
            super().paintEvent(event)

    # def keyReleaseEvent(self, event):
    #     self.stop_blinking()

    def keyPressEvent(self, event):
        self.stop_blinking()
        if 47 < event.key() < 58:
            self.inputcharary += chr(event.key())
        self.setText(self.inputcharary)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = ProbNo()
    win.show()
    sys.exit(app.exec())
