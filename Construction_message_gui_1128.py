from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
from bs4 import BeautifulSoup
import urllib.request
import re
# import Construction_message_functions as cmfunc

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

print(temperature, hum, rain)

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(ui_file,self)
        self.message_to_send = [] # 문자로 보낼 메시지 리스트
        self.weather_info = [temperature, hum, rain]
        # self.weather_box = QLabel(str("\n".join(self.weather_info)))
        self.pushButton.clicked.connect(self.buttonclick)

        self.checkBox_2.clicked.connect(lambda: self.message_writing(self.weather_info[0], self.weather_info[1], self.weather_info[2],self.message_to_send, self.checkBox_2))
        self.checkBox_3.clicked.connect(lambda: self.message_writing(self.weather_info[0], self.weather_info[1], self.weather_info[2],self.message_to_send, self.checkBox_3))
        self.checkBox_4.clicked.connect(lambda: self.message_writing(self.weather_info[0], self.weather_info[1], self.weather_info[2],self.message_to_send, self.checkBox_4))
        self.checkBox_5.clicked.connect(lambda: self.message_writing(self.weather_info[0], self.weather_info[1], self.weather_info[2],self.message_to_send, self.checkBox_5))
        self.checkBox_6.clicked.connect(lambda: self.message_writing(self.weather_info[0], self.weather_info[1], self.weather_info[2],self.message_to_send, self.checkBox_6))
        self.checkBox_7.clicked.connect(lambda: self.message_writing(self.weather_info[0], self.weather_info[1], self.weather_info[2],self.message_to_send, self.checkBox_7))
        self.checkBox_8.clicked.connect(lambda: self.message_writing(self.weather_info[0], self.weather_info[1], self.weather_info[2],self.message_to_send, self.checkBox_8))
        self.checkBox_9.clicked.connect(lambda: self.message_writing(self.weather_info[0], self.weather_info[1], self.weather_info[2],self.message_to_send, self.checkBox_9))
        self.checkBox_10.clicked.connect(lambda: self.message_writing(self.weather_info[0], self.weather_info[1], self.weather_info[2],self.message_to_send, self.checkBox_10))
        self.checkBox_11.clicked.connect(lambda: self.message_writing(self.weather_info[0], self.weather_info[1], self.weather_info[2],self.message_to_send, self.checkBox_11))
        self.checkBox_12.clicked.connect(lambda: self.message_writing(self.weather_info[0], self.weather_info[1], self.weather_info[2],self.message_to_send, self.checkBox_12))

    def buttonclick(self):
        self.message_1.clear()
        for message in self.message_to_send:
            for instructions in message:
                self.message_1.append(instructions)
        self.message_to_send = []

    def message_writing(tem_p, hum_p, rain_p, message_list, checkBox_object):
        if tem_p > 30:
            message_list.append = ("실외 공사는 가급적이면 쉬어주세요!\n")
        else:
            pass
        if hum_p > 0:
            message_list.append = ("비가 예상됩니다.비가 온다면 바로 실외 공사를 중단해주세요!\n")
        else:
            pass

        if checkBox_object == MainDialog.checkBox_2:  # 토공사
            if checkBox_object.isChecked() == True:
                if tem_p > -12:
                    message_list.append(["토공사를 진행하기 적합한 기온입니다!",
                                         "1. 발파는 인근 지역의 인부,장비 작업시간을 배제 후 실시하며 발파 후 5분 이내는 춤입 금지해야 됩니다!",
                                         "2. 전색 시 정전기 방지 복장을 착용하여 안전사고를 예방해야 합니다!",
                                         "3. 각 공정간 간섭공정에 대한 검토사항에 따라 시공순서 및 공법변경 사항을 검토해야 합니다!"])
                else:
                    message_list.append(["토공사 하기 적합하지 않은 환경입니다."])
            return message_list

        if checkBox_object == MainDialog.checkBox_3:  # 거푸집공사
            if checkBox_object.isChecked() == True:
                message_list.append(["1. 강풍,큰 비,눈이 내릴 때에는 작업을 중지 해주세요!",
                                     "2. 해체된 거푸집을 높은 곳에서 떨어트리지 않도록 철저히 지시 해주세요!",
                                     "3. 형상, 치수가 정확하고 처짐, 배부름, 뒤틀림등의 변형이 없도록 해주세요!"])
            return message_list

        if checkBox_object == MainDialog.checkBox_4:  # 하수도공사
            if checkBox_object.isChecked() == True:
                message_list.append(["1. 개구부에는 난간, 조명설비 등을 설치. 관계자 이외의 출입금지 등의 조치를 해야 합니다!",
                                     "2. 높은 곳 작업을 할 때에는 비계 또는 안전그물을 깔고 젼고한 작업대, 가설통로를 설치해야 합니다!",
                                     "3. 도로를 깊이 굴착할 경우 굴착 주변의 건물의 영향을 받을 수 있으므로 흙막이를 설치하여 지반의 활동을 막아 건물의 안전을 유지해야 합니다!"])
            return message_list

        if checkBox_object == MainDialog.checkBox_5:  # 철근공사
            if checkBox_object.isChecked() == True:
                message_list.append(["1. 철근은 도면에 따라 바르게 배근하고 콘크리트 타설 완료시까지 움직이지 않도록 견고하게 조립해야 됩니다!",
                                     "2. 슬래브 배근시 작업통로 및 발판 설치로 철근 변형이나 유효높이 미확보 사례를 방지 해주세요!",
                                     "3. 고임대 및 간격재는 콘크리트제 및 플라스틱제를 사용하며 사용 전 KS인증을 받은 규격품 확인이 필요합니다!"])
            return message_list

        if checkBox_object == MainDialog.checkBox_6:  # 콘크리트공사
            if checkBox_object.isChecked() == True:
                if tem_p <= 4:
                    message_list.append(["한중콘크리트로 시공을 해주세요."])
                if tem_p > 25:
                    message_list.append(["서중콘크리트로 시공을 해주세요.", "1. 방수 및 고정처리가 절실히 필요한 부위는 타설 전 반드시 확인해야 합니다!",
                                         "2. 지하 외벽으로부터 내부로 관통하는 각종 슬리브는 누수방지용 설치여부를 반드시 확인해야 합니다!",
                                         "3. 콘크리트 타설 시 철근 및 매설물의 배치나 거푸집이 변형 손상되지 않도록 주의해야 합니다!"])
                if tem_p < 5:
                    message_list.append(["모르타르 작업을 할 수 없는 환경입니다.", "1. 방수 및 고정처리가 절실히 필요한 부위는 타설 전 반드시 확인해야 합니다!",
                                         "2. 지하 외벽으로부터 내부로 관통하는 각종 슬리브는 누수방지용 설치여부를 반드시 확인해야 합니다!",
                                         "3. 콘크리트 타설 시 철근 및 매설물의 배치나 거푸집이 변형 손상되지 않도록 주의해야 합니다!"])
                if tem_p < -10:
                    message_list.append(["콘크리트 치기 작업을 할 수 없는 환경입니다."])
            return message_list

        if checkBox_object == MainDialog.checkBox_7:  # 방수공사
            if checkBox_object.isChecked() == True:
                if 5 < tem_p < 25:
                    message_list.append(["방수공사 하기 적합한 환경입니다.",
                                         "1. 시작 전 요철면, 레이턴스 및 시멘트 등 불순물을 그라인더로 면고르기를 실시하고 균열부위를 보수한 이후 물청소를 실시해주세요!",
                                         "2. 작업 후 누수테스트를 꼭 해주세요!",
                                         "3. 건조, 습윤상태(표면함수율 10%이하, 프라이머 사용시 30%이하)를 확인 해주세요!"])
                else:
                    message_list.append(["방수공사 하기 적합하지 않은 환경입니다."])
            return message_list

        if checkBox_object == MainDialog.checkBox_8:  # 도장공사
            if checkBox_object.isChecked() == True:
                if 15 < tem_p < 32 and hum_p < 85:
                    message_list.append(["도장공사 하기 적합한 환경입니다.",
                                         "1. 휘발성 용제 사용할 경우 화재, 폭발 주의해주세요!",
                                         "2. 도장 후 직사광선 노출은 피해주시고 바탕에 녹물 등 유해물을 제거해주세요!",
                                         "3. 도료를 선택하고 솔질이 뭉치거나 거품이 일지 않도록 천천히 발라주세요!"])
                else:
                    message_list.append(["도장공사 하기 적합하지 않은 환경입니다."])
            return message_list

        if checkBox_object == MainDialog.checkBox_9:  # 미장공사
            if checkBox_object.isChecked() == True:
                if 3 < tem_p and hum_p > 10:
                    message_list.append(["미장공사 하기 적합한 환경입니다.",
                                         "1. 재료는 균일해 질 때까지 충분히 비벼주세요!",
                                         "2. 시멘트 쌓기 단수는 13포대 이하로 해주세요!",
                                         "3. 콘크리트, 블록 등 초벌바름이 건조한 것은 미리 적당히 물축임을 해주세요!"])
                else:
                    message_list.append(["미장공사 하기 적합하지 않은 환경입니다."])
            return message_list

        if checkBox_object == MainDialog.checkBox_10:  # 조적공사
            if checkBox_object.isChecked() == True:
                if 4 < tem_p and hum_p < 80:
                    message_list.append(["조적공사 하기 적합한 환경입니다.",
                                         "1. 1일 쌓기량, 쌓기법을 준수해주세요!",
                                         "2. 벽돌은 횡력이 약하기 때문에 진동, 충격 등 하중을 필히 방지해주세요!",
                                         "3. 도면, 시방서에 정한바가 없을 경우 영식 또는 화란식 쌓기로 진행해주세요!"])
                else:
                    message_list.append(["조적공사 하기 적합하지 않은 환경입니다."])
            return message_list

        if checkBox_object == MainDialog.checkBox_11:  # 타일공사
            if checkBox_object.isChecked() == True:
                message_list.append(["1. Open time을 준수해주세요!(15분)",
                                     "2. 들뜸 현상이 일어나지 않게 타일 뒷면 채움을 철저하게 해주세요!",
                                     "3. 균열, 탈락 등의 현상이 일어나지 않게 보양, 바탕처리를 철저하게 해주세요!"])
            return message_list

        if checkBox_object == MainDialog.checkBox_12:  # 창호공사
            if checkBox_object.isChecked() == True:
                message_list.append(["1. 창, 문틀 수직 수평 철저하게 해주세요!",
                                     "2. 창, 문틀 고정방법 준수해주세요!",
                                     "3. 문짝 경첩부위 홈파기는 필히 기계 홈파기로 하되, 옆면 3mm 정도는 홈파지 말 것!"])
            return message_list

    # def sending_message(self):
    #     for message in self.message_to_send:
    #         for instructions in message:
    #

if __name__ == '__main__':
    QApplication.setStyle("fusion")
    app = QApplication(sys.argv)
    main_dialog = MainDialog()
    main_dialog.show()
    sys.exit(app.exec_())