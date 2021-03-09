import inspect
from typing import Callable, Any
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton
from PyQt5.QtCore import Qt, QSize

class NumberPadWidget(QWidget):
    def __init__(self, btn_size: QSize, font_size: float = 16, border_size: int=1):
        super().__init__()

        layout = QGridLayout(self)
        layout.setSpacing(0)
        layout.setContentsMargins(0,0,0,0)
        width = (btn_size.width() * 3)
        height = (btn_size.height() * 4)
        size = QSize(width, height)
        self.setFixedSize(size)
        self.setStyleSheet(inspect.cleandoc(
        """\
        QPushButton {
        font:Segoe UI;
        background-color:white;
        border: %dpx solid black;
        font-size: %dpx;
        padding:5px;
        font-weight:bold;
        }
        QPushButton:pressed {background-color: red }
        """ % (border_size,font_size)))

        self._on_click = lambda _: None

        def f(txt: str, r: int, c: int):
            btn = QPushButton(txt)
            btn.clicked.connect(lambda: self._on_click(btn.text()))
            btn.setFixedSize(btn_size)
            layout.addWidget(btn, r, c, Qt.AlignCenter)
            return btn

        button1 = f("1", 0, 0)
        button2 = f("2", 0, 1)
        button3 = f("3", 0, 2)
        button4 = f("4", 1, 0)
        button5 = f("5", 1, 1)
        button6 = f("6", 1, 2)
        button7 = f("7", 2, 0)
        button8 = f("8", 2, 1)
        button9 = f("9", 2, 2)
        button10 = f("*", 3, 0)
        button11 = f("0", 3, 1)
        button12 = f("#", 3, 2)

    def set_on_click(self, fn: Callable[[str], Any]):
        self._on_click = fn
