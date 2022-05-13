from lib2to3.pgen2.driver import Driver
from PySide6.QtCore                     import  Signal, QThread
from browserload                        import  browserLoad
from loginsite                          import  loginSite
from datetime                           import  datetime, timedelta
from time                               import  sleep, time as timetime
import random
import pause
from selenium.webdriver.common.action_chains   import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.select import Select

from myvar                              import  myVar       as  mv

class procThread(QThread):
    browserproc_signal = Signal(str)
    endofjob_signal = Signal(str)

    def __init__(self):
        super().__init__()

    def return_mesg(self,mesg):
        self.browserproc_signal.emit(mesg)

    def alert_check(self):
        # print(f'time7 : {datetime.now().strftime("%H:%M:%S:%f")}')

        try:
            # 예약하기(window handle을 갖었는지 혹은 alert인지 검토)
            rev_box = WebDriverWait(mv.DRIVER, 0.1).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/ul/li[1]/div/a'))
            )
            rev_box.click()

            # b = input("예약하기 1............")
            WebDriverWait(mv.DRIVER, 1).until(EC.alert_is_present())
            mesg = Alert(mv.DRIVER).text
            # Test
            Alert(mv.DRIVER).accept()
            # Alert(mv.DRIVER).dismiss()
            self.browserproc_signal.emit(mesg)
           
            if mesg.find("예약을") >= 0:
                
                # 예약이 정상적으로 처리되었습니다
                try:
                    WebDriverWait(mv.DRIVER, 0.2).until(EC.alert_is_present())
                    mesg = Alert(mv.DRIVER).text
                    Alert(mv.DRIVER).accept()
                    self.browserproc_signal.emit(mesg)
                    if mesg.find("정상적") >= 0 :
                        mv.isRUN = True
                        return mv.isRUN
                except Exception as e:
                    self.browserproc_signal.emit(str(e))
        except Exception as e:
            self.browserproc_signal.emit(str(e))
        mv.isRUN = False
        return mv.isRUN

    def browserload_n_login(self):
        #browser load
        try:
            before_time = datetime.now().strftime("%H%M%S%f")[:-3]
            self.bl = browserLoad()
            now_time = datetime.now().strftime("%H%M%S%f")[:-3]
            response_time = int((int(now_time) - int(before_time)) / 1000)
            self.browserproc_signal.emit(f'🌍 응답 시간 : {response_time} ms')
        except Exception as  e:
            self.browserproc_signal.emit(e.message)
        self.bl.site_signal.connect(self.return_mesg)
        self.lg = loginSite()
        self.lg.login_signal.connect(self.return_mesg)
        self.lg.login()


    def proc_tee(self):

        print(f'time1 : {datetime.now().strftime("%H:%M:%S:%f")}')

        # 예약하기 btn
        actions = ActionChains(mv.DRIVER)
        reserbtn = mv.DRIVER.find_element(By.XPATH, '//*[@id="main_quick"]/li[1]/a/img')
        actions.click(reserbtn)
        actions.perform()
        print(f'time2 : {datetime.now().strftime("%H:%M:%S:%f")}')

        # 새로 고침 및 예약 일자 click
        # Test
        # mv.AFTER_CNT = 8
        # print("date cnt ............", mv.TODAY_INDEX, mv.AFTER_CNT)
        query_str = mv.DATE_TABLE[mv.TODAY_INDEX + mv.AFTER_CNT]
        b_date = mv.DRIVER.find_element(By.XPATH, query_str).get_attribute('innerText')
        self.browserproc_signal.emit(f"{b_date}일 예약을 시도 합니다.....")
        
        # 새로고침 및 날자가 booking 가능한지
        # date_actions = ActionChains(mv.DRIVER)
        # reserbtn = mv.DRIVER.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/a/button')
        # date_actions.click(reserbtn)
        # day_btn = mv.DRIVER.find_element(By.XPATH, query_str)
        # date_actions.click(day_btn)
        # date_actions.perform()
        
        while True:
            try:

                # 새로 고침
                mv.DRIVER.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/a/button').click()
                # sleep(0.1)
                none_link =mv.DRIVER.find_element(By.XPATH, query_str).get_attribute('class')
                # print(f'time3 : {datetime.now().strftime("%H:%M:%S:%f")}')
                if none_link == 'book':
                    mv.DRIVER.find_element(By.XPATH, query_str).click()
                    break
                continue
            except Exception as e:
                print(f"새로 고침 loop error {str(e)}")
                mv.isRUN = False
                return


        # win_main_handle = mv.DRIVER.current_window_handle

        # b = input(f"{mv.TODAY_INDEX}, {mv.AFTER_CNT}-------------------------------------------")

        # select될때까지  반복
        select_cnt = 0
        
        while select_cnt < 21:
            # print(f'time4 : {datetime.now().strftime("%H:%M:%S:%f")}')
            select_cnt += 1
            # time choice
            if mv.TEE_FM_INDEX == mv.TEE_TO_INDEX:
                time_index = mv.TEE_FM_INDEX
            else:
                time_index = random.choice(range(mv.TEE_FM_INDEX, mv.TEE_TO_INDEX))
            # course choice
            if mv.USER_COURSE == 0:
                course_index = random.choice((1,2,3))
            else:
                course_index = mv.USER_COURSE

            try:
                # print(f'time5 : {datetime.now().strftime("%H:%M:%S:%f")}')
                # sleep(0.2)
                query_str = f'/html/body/div[1]/div/table/tbody/tr/td[{course_index}]/table/tbody/tr[{time_index}]/td[2]/button'
                none_link = mv.DRIVER.find_element(By.XPATH, query_str)
                link_attr = none_link.get_attribute('class')
                if link_attr.find('book2') >= 0:
                    mv.DRIVER.find_element(By.XPATH, query_str).click()
                    if self.alert_check() :
                        break
                # 새로 고침
                sleep(0.2)
                mv.DRIVER.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/a/button').click()
                # print(f'time6 : {datetime.now().strftime("%H:%M:%S:%f")}')
                self.browserproc_signal.emit(f"{select_cnt}번째 시도.......")
                continue
            except Exception as e:
                print(f"새로 고침 loop error {str(e)}")
                mv.isRUN = False
                return
       

    # use pause until
    def run(self):
        # time to seconds 3분전을 세팅함
        base_date = datetime.combine(datetime.today(), mv.BASE_TIME)
        start_time = base_date - timedelta(minutes=2)
        pause.until(start_time)
        self.browserload_n_login()

        start_time = base_date - timedelta(seconds=(2 + mv.DIFF_TIME))
        pause.until(start_time)
        self.proc_tee()
        mv.DRIVER.quit()
        self.endofjob_signal.emit("작업이 종료되었습니다.")
        self.stop()

    def stop(self):
        self.quit()
