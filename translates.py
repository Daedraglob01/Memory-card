from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QVBoxLayout, QHBoxLayout,QLabel,QPushButton)
from time import sleep
translate_line2 = QHBoxLayout()
translate_line1 = QVBoxLayout()
time_lb = QLabel("0")
translate_line2.addStretch(2)
translate_line2.addWidget(QLabel("час навчання"))
translate_line2.addWidget(time_lb)
t1 = QLabel("Apple-яблуко")
t2 = QLabel("Tree-дерево")
t3 = QLabel("Cat-кішка")
t4 = QLabel("Red-червоний")
t5 = QLabel("Sky-небо")
t6 = QLabel("Banana-банан")
t7 = QLabel("Orange-апельсин")
t8 = QLabel("Mango-манго")
t9 = QLabel("Cherry-вишня")
t10 = QLabel("Mandarin-мандарин")
menu_button2 = QPushButton('Меню')
translate_line1.addWidget(menu_button2, alignment=Qt.AlignLeft)
translate_line1.addWidget(t1,alignment=Qt.AlignHCenter)
translate_line1.addWidget(t2,alignment=Qt.AlignHCenter)
translate_line1.addWidget(t3,alignment=Qt.AlignHCenter)
translate_line1.addWidget(t4,alignment=Qt.AlignHCenter)
translate_line1.addWidget(t5,alignment=Qt.AlignHCenter)
translate_line1.addWidget(t6,alignment=Qt.AlignHCenter)
translate_line1.addWidget(t7,alignment=Qt.AlignHCenter)
translate_line1.addWidget(t8,alignment=Qt.AlignHCenter)
translate_line1.addWidget(t9,alignment=Qt.AlignHCenter)
translate_line1.addWidget(t10,alignment=Qt.AlignHCenter)
translate_line = QVBoxLayout()
translate_line.addLayout(translate_line1)
translate_line.addLayout(translate_line2)