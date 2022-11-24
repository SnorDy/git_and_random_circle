from random import randint
import sys
from PyQt5.QtWidgets import QWidget, QPushButton,QApplication
from PyQt5.QtGui import QPainter,QColor


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter(self)
            qp.setBrush(QColor(randint(1, 255), randint(1, 255), randint(1, 255), randint(1, 255)))
            for i in range(4):
                qp.drawEllipse(randint(1, 300), randint(1, 300), randint(1, 100), randint(1, 100))
            qp.end()

    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Git и случайные окружности')
        self.setStyleSheet('background-color: rgb(30,30,50)')
        self.btn = QPushButton(self)
        self.btn.resize(175,50)
        self.btn.move(120,20)
        self.btn.clicked.connect(self.paint)
        self.btn.setText("Нарисовать окружности")
        self.btn.setStyleSheet('background-color: rgb(50,190,200);border-radius:2px; font: 11pt Yu Gothic UI Semilight ')
if __name__=='__main__':
    app=QApplication([])
    ex= Example()
    ex.show()
    sys.exit(app.exec())