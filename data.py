from random import shuffle

# class Test:
#     def __init__(self, quest_list, quantity = 5):

#         # self.current_quest = 0

class Questions:
    def __init__(self, question, right, wrong1, wrong2, wrong3, img=None):
        self.question = question
        self.right = right
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
        self.img = img
    
    def show_data(self, quest_lb, result_answ, rbtn_list):
        quest_lb.setText(self.question + "<br>" + f"<img src={self.img} height=100>")
        result_answ.setText(self.right)
        shuffle(rbtn_list)
        rbtn_list[0].setText(self.right)
        rbtn_list[1].setText(self.wrong1)
        rbtn_list[2].setText(self.wrong2)
        rbtn_list[3].setText(self.wrong3)

    def chek_result(self, rbtn_list, result):
        if rbtn_list[0].isChecked():
            result.setText("вірно!")
        else:
            result.setText("не вірно!")

q1 = Questions("Яблуко", "apple", "caterpillar", "jamm", "cloud", "D:/memory_card/img/yabloko.jpg")
q2 = Questions("Дерево", "tree", "three", "root", "groot", "D:/memory_card/img/tree.jpg")
q3 = Questions("Кішка", "cat", "cow", "dog", "frog", "D:/memory_card/img/cat.jpg")
q4 = Questions("Червоний", "red", "green", "blue", "black", "D:/memory_card/img/red.png")
q5 = Questions("Небо", "sky", "fly", "cry", "bue", "D:/memory_card/img/sky.jpg")
q6 = Questions('Апельсин','orange','red','bue','cherry','D:/memory_card/img/orange.jpg' )
q7 = Questions('Банан','banana','banan','banane','banano','D:/memory_card/img/banana.jpg')
q8 = Questions('Манго','mango','manga','mange','mangu','D:/memory_card/img/mango.jfif')
q9 = Questions('Вишня','cherry','cherro','cherra','cherri','D:/memory_card/img/cherry.png')
q10 = Questions('Мандарин','mandarin','mandarine','mandarina','mandarino','D:/memory_card/img/mandarin.jpg')


quest_list = [q1, q2, q3, q4, q5,q6,q7,q8,q9,q10]