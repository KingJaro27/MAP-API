import sys
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
import requests
import io
from maps import get_map


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mega")

        # Виджеты для ввода координат и масштаба
        self.y_coord = QDoubleSpinBox(
            self, decimals=6, value=59.119467, singleStep=0.000001
        )
        self.x_coord = QDoubleSpinBox(
            self, decimals=6, value=37.904108, singleStep=0.000001
        )
        self.mas = QSpinBox(self, maximum=21, minimum=1, value=17)

        self.black = QCheckBox(self, checkStateChanged=self.africa)
        self.black.setText("Темная тема")
        self.color = "white"

        self.pixmap = QPixmap(500, 500)
        self.pixmap.fill()
        self.image = QLabel(pixmap=self.pixmap)

        self.btn = QPushButton(self, clicked=self.ok)
        self.btn.setText("ok")

        self.qvbox = QVBoxLayout()
        self.qvbox.addWidget(self.x_coord)
        self.qvbox.addWidget(self.y_coord)
        self.qvbox.addWidget(self.mas)
        self.qvbox.addWidget(self.btn)
        self.qvbox.addWidget(self.black)
        self.qvbox.addStretch()

        self.qhbox = QHBoxLayout(self)
        self.qhbox.addLayout(self.qvbox)
        self.qhbox.addWidget(self.image)

        self.setFocus()
        self.ok()

    def initUI(self):
        self.pixmap.loadFromData(self.map_file.getvalue())
        self.image.setPixmap(self.pixmap)

    def ok(self):
        self.x, self.y = self.x_coord.value(), self.y_coord.value()
        self.m = self.mas.value()
        self.map_file = get_map(self.x, self.y, self.m, self.color)
        print(self.color)
        self.initUI()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Z:
            self.mas.setValue(self.mas.value() + 1)
            self.ok()
        elif event.key() == Qt.Key.Key_X:
            self.mas.setValue(self.mas.value() - 1)
            self.ok()
        elif event.key() == Qt.Key.Key_D:
            self.x_coord.setValue(self.x_coord.value() + 0.000001)
            self.ok()
        elif event.key() == Qt.Key.Key_S:
            self.y_coord.setValue(self.y_coord.value() - 0.000001)
            self.ok()
        elif event.key() == Qt.Key.Key_A:
            self.x_coord.setValue(self.x_coord.value() - 0.000001)
            self.ok()
        elif event.key() == Qt.Key.Key_W:
            self.y_coord.setValue(self.y_coord.value() + 0.000001)
            self.ok()
        else:
            super().keyPressEvent(event)

    def africa(self):
        if self.black.isChecked():
            self.color = "black"
        else:
            self.color = "white"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
