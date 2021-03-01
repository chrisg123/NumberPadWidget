import sys
import signal
import time
import inspect
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt, QSize, QTimer
from typing import Callable, Any
from NumberPadWidget import NumberPadWidget

def main():
    signal.signal(signal.SIGINT, sigint)

    app = QApplication(['_'])

    window = QWidget()
    layout = QGridLayout(window)
    layout.setSpacing(0)
    layout.setContentsMargins(0,0,0,0)
    window.setLayout(layout)
    window.setFixedSize(QSize(640, 480))

    numpad = NumberPadWidget(QSize(65,65), 24, 5)
    numpad.set_on_click(lambda x: print(x))
    layout.addWidget(numpad, 0,0, Qt.AlignCenter)

    window.show()

    timer = QTimer()
    timer.timeout.connect(lambda:None)
    timer.start(100)

    exit_code = app.exec_()

    return exit_code

def sigint(*_):
    sys.stdout.write("\nexit\n")
    sys.exit(0)

if __name__ == '__main__':
    sys.exit(main())
