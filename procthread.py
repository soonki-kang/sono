from PySide6.QtCore import Signal, QThread, QMutex, QWaitCondition
from browserload import browserLoad
from loginsite import loginSite
from datetime import datetime, timedelta
from time import time
import pause
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from turtle import textinput

# import threading
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
# from jointhread import joinThread
from probnopopup import ProbNo

from myvar import myVar as mv

waitCondition = QWaitCondition()
mutex = QMutex()


class procThread(QThread):
    browserproc_signal = Signal(str)
    endofjob_signal = Signal(str)
    probno_signal = Signal(str)

    def __init__(self):
        super().__init__()

    def return_mesg(self, mesg):
        self.browserproc_signal.emit(mesg)

    def browserload_n_login(self):
        # browser load
        # site 응답시간 계산
        try:
            before_time = datetime.now().strftime("%H%M%S%f")[:-3]
            self.bl = browserLoad()
            now_time = datetime.now().strftime("%H%M%S%f")[:-3]
            response_time = int((int(now_time) - int(before_time)) / 1000)
            self.browserproc_signal.emit(f'🌍 응답 시간 : {response_time} ms')
        except Exception as e:
            self.browserproc_signal.emit(str(e))

        self.bl.site_signal.connect(self.return_mesg)
        self.lg = loginSite()
        self.lg.login_signal.connect(self.return_mesg)
        self.lg.login()

    def moveToRes(self):
        # 예약 버튼 클릭
        mv.DRIVER.get('https://www.sonofelicecc.com/rsv.cal.dp/dmparse.dm')

        # couse selelct
        if mv.USER_COURSE == 0:
            mv.DRIVER.find_element(
                By.XPATH, '//*[@id="fJiyukSel"]/option[1]').click()
        elif mv.USER_COURSE == 1:
            mv.DRIVER.find_element(
                By.XPATH, '//*[@id="fJiyukSel"]/option[2]').click()
        elif mv.USER_COURSE == 2:
            mv.DRIVER.find_element(
                By.XPATH, '//*[@id="fJiyukSel"]/option[3]').click()
        elif mv.USER_COURSE == 3:
            mv.DRIVER.find_element(
                By.XPATH, '//*[@id="fJiyukSel"]/option[4]').click()
        self.refresh()

    def refresh(self):

        # 새로고침
        #
        mv.DRIVER.find_element(
            By.XPATH, '//*[@id="startCal"]/span[1]/a/img').click()

    # def callthread(self, e, selectTime):
    #     self.locals()['jt{}'.format(selectTime)] = joinThread(e, parent=self)
    #     self.locals()['jt{}'.format(selectTime)
    #                   ].joinsignal.connect(self.return_mesg)
    #     self.locals()['jt{}'.format(selectTime)].start()

    def choiceTee(self, tee):

        # 해당 tee 선택
        tee.click()

        # check alert
        # alert이 있으면 종료될때 까지 실행
        while True:
            try:
                WebDriverWait(mv.DRIVER, 2).until(
                    EC.alert_is_present()
                )
                # if EC.alert_is_present():
                alert_pannel = mv.DRIVER.switch_to.alert
                self.browserproc_signal.emit(alert_pannel.text)
                alert_pannel.accept()
            except:
                break

        # 인증 번호 요구하기
        mv.DRIVER.find_element(
            By.XPATH, '//*[@id="rsvForm"]/div/fieldset/table/tbody/tr[8]/th/a/input').click()

        # 인증번호 발송

        # mv.DRIVER.find_element(
        #     By.XPATH, '//*[@id="popContainer"]/div[2]/div[2]/a').click()

        mv.DRIVER.execute_script('doSmsAuthSend();')

        # if EC.alert_is_present():
        # 인증번호 전송했다는 alert 처리
        try:
            WebDriverWait(mv.DRIVER, 3).until(
                EC.alert_is_present()
            )
        except:
            print('not exist alert..............')

        alert_pannel = mv.DRIVER.switch_to.alert
        self.browserproc_signal.emit(alert_pannel.text)
        alert_pannel.accept()

        # 인증 번호가  입력될때까지 대기
        self.probno_signal.emit('OK')

        mv.MUTEX.lock()
        mv.WAITCONDITION.wait(mutex)
        mv.MUTEX.unlock()

        # yield '인증번호 입력 대기'clear

        # print('인증 번호 입력 완료.............................')

        # prob_no = textinput("인증번호", "인증번호를 입력하세요!!")
        # print(f'...........prob no  {mv.PROBNO}')

        # 인증 번호 전송
        prob_input = mv.DRIVER.find_element(By.XPATH, '//*[@id="answer"]')
        prob_input.click()
        prob_input.send_keys(mv.PROBNO)

        # 최종 예약 버튼 클릭
        mv.DRIVER.find_element(
            By.XPATH, '//*[@id="container"]/div[3]/div[3]/a[1]').click()

        alert_pannel = mv.DRIVER.switch_to.alert
        self.browserproc_signal.emit(alert_pannel.text)
        alert_pannel.accept()

    # 날자가 open될때까지 20초 동안 기다림..........

    def peekDate(self):
        setTimeOut = time() + 20
        # 시간 정규 표현식 정의
        # expr_time = re.compile("\d{2}[:]\d{2}")
        rev_date = mv.USER_REVDATE.strftime('%Y%m%d')
        tableXpath = '//*[@id="container"]/div[3]/div[5]'
        dateXpath = f"//a[contains(@href, " + \
            f'"doReserv(' + f"'{rev_date}'" + '")]'
        findText = tableXpath + dateXpath

        # print(f'----------- here1  {findText} -----------')

        while True:
            self.refresh()
            try:
                mv.DRIVER.find_element(By.XPATH, findText).click()
                return True
            except:
                # get_attribute(rev_date)
                if setTimeOut < time():
                    self.browserproc_signal.emit("Open Time Out .......")
                    mv.isRUN = False
                    return False
                else:
                    continue

    #  날자 진입후 처리

    def proc_tee(self):

        # teeElements = mv.DRIVER.find_elements(By.XPATH, '//*[@id="rsvTableBody"]//a[@class=button]')

        try:
            teeElements = WebDriverWait(mv.DRIVER, 2).until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, '//*[@id="rsvTableBody"]//a[contains(@class, "button")]'))
            )
        except:
            self.browserproc_signal.emit("제공된 tee가 없습니다.")
            mv.isRUN = False
            return

        random.shuffle(teeElements)

        for i, tee in enumerate(teeElements):
            linkText = tee.get_attribute('href')
            # linkText = tee.get_attribute('href')[37:41]
            startString = linkText.find('(')
            endString = linkText.find(')')
            selectTime = linkText[startString:endString].split(',')[2][1:5]
            if (mv.STRREVFMTIME <= selectTime <= mv.STRREVTOTIME):
                self.choiceTee(tee)
                break

    # use pause until

    def run(self):

        # set time to minutes 2분전까지 대기
        base_date = datetime.combine(datetime.today(), mv.BASE_TIME)

        start_time = base_date - timedelta(minutes=2)
        pause.until(start_time)

        # 1 두번째 login
        self.browserload_n_login()

        # 2 login후 골프 예약 page로 이동 및 course setting
        self.moveToRes()

        # 10초전까지 대기
        # start_time = base_date - timedelta(seconds=(2 + mv.DIFF_TIME))
        start_time = base_date - timedelta(seconds=10)
        pause.until(start_time)

        # 3 날자 open 대기 후 open이 되면  실행
        if self.peekDate():
            self.proc_tee()
        else:
            self.endofjob_signal.emit("날자를 선택하지 못했습니다.")

        self.endofjob_signal.emit("작업이 종료되었습니다.")
        self.stop()

    def stop(self):
        self.lg.logout()
        # time.sleep(1)
        mv.DRIVER.quit()
        self.quit()
