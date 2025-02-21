import sys
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import requests
import io
from maps import get_map

SCREEN_SIZE = [750, 500]


class Example(QWidget):
    def __init__(self):
        super().__init__(windowTitle="Mega")
        self.setGeometry(100, 100, SCREEN_SIZE[0] - 250, SCREEN_SIZE[-1])
        self.adress = QLineEdit(self, placeholderText="Введите координаты")
        self.mas = QLineEdit(self, placeholderText="Введиет масштаб")
        self.qhbox = QHBoxLayout(self)
        self.qvbox = QVBoxLayout()
        self.adress.setFixedSize(100, 30)
        self.mas.setFixedSize(100, 30)
        self.btn = QPushButton(self, clicked=self.ok)
        self.btn.setFixedSize(100, 30)
        self.adress.move(0, 100)
        self.mas.move(0, 150)
        self.btn.move(0, 200)
        self.qvbox.addWidget(self.adress)
        self.qvbox.addWidget(self.mas)
        self.qvbox.addWidget(self.btn)
        self.btn.setText("ok")

    def initUI(self):
        ## Изображение
        self.pixmap = QPixmap()
        self.pixmap.loadFromData(self.map_file.getvalue())
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(450, 450)
        self.image.setPixmap(self.pixmap)
        self.qhbox.addWidget(self.image)
        self.qhbox.addLayout(self.qvbox)

    def ok(self):
        text = self.adress.text().split()
        self.x, self.y = float(text[0]), float(text[-1])
        self.m = float(self.mas.text())
        self.map_file = get_map(self.x, self.y, self.m)
        self.initUI()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
