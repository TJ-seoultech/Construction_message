from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
from bs4 import BeautifulSoup
import urllib.request
import re
import Construction_message_functions_t as cmfunc
from twilio.rest import Client
import os

def CCP_2(relative_path):
    base_path = getattr(sys, "_MIEPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

ui_file = CCP_2("./gui_section1_test_2_weather.ui")


# 웹 크롤링
webpage = urllib.request.urlopen(
    'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EA%B3%B5%EB%A6%89%EB%8F%99+%EB%82%A0%EC%94%A8&oquery=%EB%8F%84%EB%8B%B4%EB%8F%99+%EB%82%A0%EC%94%A8&tqi=hiLhCsp0JXVssdi3iGossssssuR-100634/')
soup = BeautifulSoup(webpage, 'html.parser')
temps = soup.find('div', "temperature_text")
humidity = soup.select('dd.desc')
# 변수지정
temperature = int(re.sub(r"[^a-zA-Z0-9]", "", temps.get_text()))
hum = int(re.sub(r"[^a-zA-Z0-9]", "", humidity[1].get_text()))
rain = int(re.sub(r"[^a-zA-Z0-9]", "", humidity[0].get_text()))


class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(ui_file,self)
        self.message_to_send_preface = []
        self.message_to_send = [] # 문자로 보낼 메시지 리스트
        self.weather_info = [temperature, hum, rain]
        self.label_4.setText('--> 날씨: {} \u2103 \n--> 습도: {}%\n--> 강수확률: {}%'.format(self.weather_info[0],self.weather_info[1], self.weather_info[2]))

        self.pushButton.clicked.connect(self.buttonclick)
        self.pushButton_2.clicked.connect(self.removing_message)
        self.pushButton_3.clicked.connect(self.sending_message)

        self.checkBox_2.clicked.connect(lambda: cmfunc.making_text(self.weather_info[0], self.weather_info[1], self.weather_info[2],self.message_to_send, self.checkBox_2, 1))
        self.checkBox_3.clicked.connect(lambda: cmfunc.making_text(self.weather_info[0], self.weather_info[1], self.weather_info[2],self.message_to_send, self.checkBox_3, 2))
        self.checkBox_4.clicked.connect(lambda: cmfunc.making_text(self.weather_info[0], self.weather_info[1], self.weather_info[2],self.message_to_send, self.checkBox_4, 3))
        self.checkBox_5.clicked.connect(lambda: cmfunc.making_text(self.weather_info[0], self.weather_info[1], self.weather_info[2],self.message_to_send, self.checkBox_5, 4))
        self.checkBox_6.clicked.connect(lambda: cmfunc.making_text(self.weather_info[0], self.weather_info[1], self.weather_info[2],self.message_to_send, self.checkBox_6, 5))
        self.checkBox_7.clicked.connect(lambda: cmfunc.making_text(self.weather_info[0], self.weather_info[1], self.weather_info[2],self.message_to_send, self.checkBox_7, 6))
        self.checkBox_8.clicked.connect(lambda: cmfunc.making_text(self.weather_info[0], self.weather_info[1], self.weather_info[2],self.message_to_send, self.checkBox_8, 7))
        self.checkBox_9.clicked.connect(lambda: cmfunc.making_text(self.weather_info[0], self.weather_info[1], self.weather_info[2],self.message_to_send, self.checkBox_9, 8))
        self.checkBox_10.clicked.connect(lambda: cmfunc.making_text(self.weather_info[0], self.weather_info[1], self.weather_info[2],self.message_to_send, self.checkBox_10, 9))
        self.checkBox_11.clicked.connect(lambda: cmfunc.making_text(self.weather_info[0], self.weather_info[1], self.weather_info[2],self.message_to_send, self.checkBox_11, 10))
        self.checkBox_12.clicked.connect(lambda: cmfunc.making_text(self.weather_info[0], self.weather_info[1], self.weather_info[2],self.message_to_send, self.checkBox_12, 11))

    def removing_message(self):
        self.message_1.clear()

    def buttonclick(self):
        self.message_1.clear()
        for message in self.message_to_send:
            for instructions in message:
                self.message_1.append(instructions)
        self.message_to_send_twilio = self.message_to_send
        self.message_to_send = []

    def sending_message(self):
        account_sid = 'AC227cc2085426b7dc96e32220a2982396'
        auth_token = 'a29beb3c74c41f5f58080d1850587279'
        client = Client(account_sid, auth_token)
        message_body = ''
        # [[방수공사 주의사항, , , ],[미장공사 주의사항, , , ],[토공사 주의사항, , ]]
        for work_instructions in self.message_to_send_twilio:
            for instruction in work_instructions:
                message_body = message_body + instruction + '\n'
        print(message_body)
        message = client.messages \
            .create(
            body=message_body,
            from_='+12283007335',
            to='+8201025414136'
        )


QApplication.setStyle("fusion")
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
sys.exit(app.exec_())
input()