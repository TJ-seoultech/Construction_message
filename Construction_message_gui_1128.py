from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
from bs4 import BeautifulSoup
import urllib.request
import re
import Construction_message_functions as cmfunc
from PyQt5.QtCore import Qt

ui_file = "gui_section1_test_2_weather.ui"
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
        self.message_to_send = [] # 문자로 보낼 메시지 리스트
        self.weather_info = [temperature, hum, rain]
        # self.weather_box = QLabel(self.weather_info)
        self.pushButton.clicked.connect(self.buttonclick)

        self.checkBox_2.clicked.connect(lambda: cmfunc.earthwork(self.weather_info[0], self.weather_info[1], self.weather_info[2],self.message_to_send))
        self.checkBox_3.clicked.connect(lambda: cmfunc.form_work(self.weather_info[0], self.weather_info[1], self.weather_info[2],self.message_to_send))
        self.checkBox_4.clicked.connect(lambda: cmfunc.drain_page_works(self.weather_info[0], self.weather_info[1]   , self.weather_info[2],self.message_to_send))
        self.checkBox_5.clicked.connect(lambda: cmfunc.reinforcing_bar_work(self.weather_info[0], self.weather_info[1] , self.weather_info[2],self.message_to_send))
        self.checkBox_6.clicked.connect(lambda: cmfunc.concrete_work(self.weather_info[0], self.weather_info[1], self.weather_info[2],self.message_to_send))
        self.checkBox_7.clicked.connect(lambda: cmfunc.water_proof(self.weather_info[0], self.weather_info[1]  , self.weather_info[2],self.message_to_send))
        self.checkBox_8.clicked.connect(lambda: cmfunc.painters_work(self.weather_info[0], self.weather_info[1], self.weather_info[2],self.message_to_send))
        self.checkBox_9.clicked.connect(lambda: cmfunc.plaster_work(self.weather_info[0], self.weather_info[1] , self.weather_info[2],self.message_to_send))
        self.checkBox_10.clicked.connect(lambda: cmfunc.masonry(self.weather_info[0], self.weather_info[1]  , self.weather_info[2],self.message_to_send))
        self.checkBox_11.clicked.connect(lambda: cmfunc.tiling(self.weather_info[0], self.weather_info[1]   , self.weather_info[2],self.message_to_send))
        self.checkBox_12.clicked.connect(lambda: cmfunc.joiners_work(self.weather_info[0], self.weather_info[1] , self.weather_info[2],self.message_to_send))

    def buttonclick(self):
        for message in self.message_to_send:
            for instructions in message:
                self.message_1.append(instructions)


QApplication.setStyle("fusion")
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
sys.exit(app.exec_())