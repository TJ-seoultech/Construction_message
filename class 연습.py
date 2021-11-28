from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
from PyQt5.QtCore import Qt

weather = [4, 17, 8]

def earthwork(tem_p, hum_p, rain_p, message_list):   #토공사
    if tem_p > -12:
        message_list.append(["토공사를 진행하기 적합한 기온입니다!", "1. 발파는 인근 지역의 인부,장비 작업시간을 배제 후 실시하며 발파 후 5분 이내는 춤입 금지해야 됩니다!", "2. 전색 시 정전기 방지 복장을 착용하여 안전사고를 예방해야 합니다!", "3. 각 공정간 간섭공정에 대한 검토사항에 따라 시공순서 및 공법변경 사항을 검토해야 합니다!"])
    else:
        message_list.append(["토공사 하기 적합하지 않은 환경입니다."])
    return message_list

# class gui(QDialog):
#     def __init__(self):
#         QDialog.__init__(self, None)
#         uic.loadUi(ui_file,self)

class gui(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.message_to_send=[]

    def initUI(self):
        cb = QCheckBox('Show title', self)
        cb.move(20, 20)
        cb.stateChanged.connect(self.creating_message)

        self.setWindowTitle('My First Application')
        self.move(300, 300)
        self.resize(400, 200)

        if cb.isChecked():
            self.creating_message()
    def creating_message(self, state):
        if state == Qt.Checked:
            earthwork(weather[0], weather[1], weather[2], self.message_to_send)
            print(self.message_to_send)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_gui_program = gui()
    my_gui_program.show()
    sys.exit(app.exec_())
