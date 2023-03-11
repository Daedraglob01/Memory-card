from PyQt5.Qt import Qt
from PyQt5.QtWidgets import (QApplication, QRadioButton, QVBoxLayout, 
                            QHBoxLayout, QLabel, QPushButton, QSpinBox, 
                            QGroupBox, QButtonGroup)

def show_result():
    group_box.hide()
    group_box2.show()
    ok_btn.setText("Наступне питання")

def show_question():
    rbtn_group.setExclusive(False)
    for rb in rbtn_list:
        rb.setChecked(False)
    rbtn_group.setExclusive(True)
    group_box2.hide()
    group_box.show()
    ok_btn.setText("Відповісти")

app = QApplication([])

# Елементи першої лінії
menu_btn = QPushButton("Меню")
rest_btn = QPushButton("Відпочити")
rest_spin = QSpinBox()
rest_spin.setValue(30)
# Питання
quest_lb = QLabel("запитання")

# Блок з варіантами
# рамка для вріантів з написом
group_box = QGroupBox("Варіанти відповіді")
# група кнопок
rbtn_group = QButtonGroup()
rbtn_list = []
for i in range(4):
    rbtn = QRadioButton("варіант1")
    rbtn_list.append(rbtn)
    rbtn_group.addButton(rbtn)

# розташуємо варіанти в групі
layout_group = QHBoxLayout()
line1_group = QVBoxLayout()
line2_group = QVBoxLayout()

line1_group.addWidget(rbtn_list[0])
line1_group.addWidget(rbtn_list[1])
line2_group.addWidget(rbtn_list[2])
line2_group.addWidget(rbtn_list[3])

layout_group.addLayout(line1_group)
layout_group.addLayout(line2_group)

group_box.setLayout(layout_group)

# приховані елементи - результати
group_box2 = QGroupBox("Результат теста")
result = QLabel("вірно/невірно")
result_answ = QLabel("відповідь")

layout_group2 = QVBoxLayout()
layout_group2.addWidget(result, alignment=Qt.AlignTop | Qt.AlignLeft)
layout_group2.addStretch(1)
layout_group2.addWidget(result_answ, alignment=Qt.AlignHCenter)
layout_group2.addStretch(1)
group_box2.setLayout(layout_group2)

# group_box.hide()
group_box2.hide()

# кнопка на останній лінії
ok_btn = QPushButton("Відповісти")

# напрямні лінії
layout_card = QVBoxLayout()
line1 = QHBoxLayout()
line2 = QHBoxLayout()

line1.addWidget(menu_btn)
line1.addStretch()
line1.addWidget(rest_btn)
line1.addWidget(rest_spin)
line1.addWidget(QLabel("хвилин"))

line2.addStretch(1)
line2.addWidget(ok_btn, stretch=2)
line2.addStretch(1)

# додаємо все на основний лайаут
layout_card.addLayout(line1)
layout_card.addStretch(1)
layout_card.addWidget(quest_lb, alignment=Qt.AlignHCenter)
layout_card.addStretch(1)
layout_card.addWidget(group_box, stretch=8)
layout_card.addWidget(group_box2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(line2)
layout_card.addStretch(1)