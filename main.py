from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QWidget,QMessageBox
from card_layout import *
from data import *
from menu import *
from random import choice
from translates import *
q = choice(quest_list)
q.show_data(quest_lb, result_answ, rbtn_list)

timer = QTimer()
timer.setInterval(1000)

def ok_click():
    global q
    if ok_btn.text() == "Відповісти":
        if rbtn_group.checkedButton():
            q.chek_result(rbtn_list, result)
            show_result()
    else:
        q = choice(quest_list)
        q.show_data(quest_lb, result_answ, rbtn_list)
        show_question()

def start_test():
    menu_window.hide()
    window.show()
    translate_window.hide()

def show_menu():
    time_lb.setText('0')
    menu_window.show()
    window.hide()
    translate_window.hide()


def show_translates():
    timer.start()
    menu_window.hide()
    window.hide()
    translate_window.show()

    
    

def timer_handler():
    time_lb.setText(str(int(time_lb.text())+1))
    if int(time_lb.text()) >= 60:
        m = QMessageBox()
        m.setWindowTitle("Час вичерпано!")
        m.setText("Досить навчатись")
        if m.exec_() == 1024:
            timer.stop()
            show_menu()
timer.timeout.connect(timer_handler)
test_btn.clicked.connect(start_test)
ok_btn.clicked.connect(ok_click)
menu_btn.clicked.connect(show_menu)
new_btn.clicked.connect(show_translates)
menu_button2.clicked.connect(show_menu)
card_width, card_height = 600, 500

window = QWidget()
window.resize(card_width, card_height)
window.setWindowTitle("Memory Card")
window.move(0, 0)
# window.show()

window.setLayout(layout_card)

menu_window = QWidget()
menu_window.setWindowTitle("Memory Card Menu")
menu_window.resize(500, 300)

menu_window.setStyleSheet("background-color: lightgreen")

menu_window.setLayout(menu_line)

menu_window.show()

translate_window = QWidget()
translate_window.setWindowTitle("Memory Card Translates")
translate_window.resize(500, 300)
translate_window.setLayout(translate_line)



app.exec_()