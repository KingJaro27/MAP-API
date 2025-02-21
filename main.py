import sys
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import requests
import io
from maps import get_map


class Example(QWidget):
    def __init__(self):
        super().__init__(windowTitle="Mega")
        self.y_coord = QDoubleSpinBox(
            self, decimals=6, value=59.119467, singleStep=0.000001
        )
        self.x_coord = QDoubleSpinBox(
            self, decimals=6, value=37.904108, singleStep=0.000001
        )
        self.mas = QSpinBox(self, maximum=21, minimum=1, value=17)

        self.pixmap = QPixmap(500, 500)
        self.pixmap.fill()
        self.image = QLabel(pixmap=self.pixmap)

        self.qvbox = QVBoxLayout()
        self.btn = QPushButton(self, clicked=self.ok)
        self.qvbox.addWidget(self.x_coord)
        self.qvbox.addWidget(self.y_coord)
        self.qvbox.addWidget(self.mas)
        self.qvbox.addWidget(self.btn)
        self.qvbox.addStretch()
        self.btn.setText("ok")

        self.qhbox = QHBoxLayout(self)
        self.qhbox.addLayout(self.qvbox)
        self.qhbox.addWidget(self.image)
        self.ok()

    def initUI(self):
        ## Изображение

        self.pixmap.loadFromData(self.map_file.getvalue())
        self.image.move(0, 0)
        self.image.resize(500, 500)
        self.image.setPixmap(self.pixmap)

    def ok(self):
        self.x, self.y = self.x_coord.value(), self.y_coord.value()
        self.m = self.mas.value()
        self.map_file = get_map(self.x, self.y, self.m)
        self.initUI()

    def keyPressEvent(self, keyPress):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
