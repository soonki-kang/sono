from ast import Pass
from selenium.webdriver.common.keys             import  Keys
from selenium.webdriver.common.action_chains    import ActionChains
from selenium.webdriver.common.by               import By
from selenium.webdriver.support.ui              import WebDriverWait 
from selenium.webdriver.common.alert            import Alert
from selenium.webdriver.support                 import expected_conditions as EC 
from PySide6.QtCore                             import  Signal, QObject
from time                                       import  sleep
from datetime                                   import  timedelta, datetime
from myvar                                      import  myVar   as mv

class loginSite(QObject):
    login_signal    =   Signal(str)
    
    def __init__(self):
        super().__init__()


    def login(self):
        loginid = mv.DRIVER.find_element(By.XPATH, '//*[@id="userId1"]')
        loginpassword = mv.DRIVER.find_element(By.XPATH, '//*[@id="userPw1"]' )
        loginbtn = mv.DRIVER.find_element(By.XPATH, '//*[@id="loginForm"]/button')
        
        actions = ActionChains(mv.DRIVER)
        actions.click(loginid)
        actions.send_keys(mv.USER_ID)
        actions.click(loginpassword)
        actions.send_keys(mv.USER_PASSWORD)
        # actions.move_to_element(loginbtn)
        actions.click(loginbtn)
        actions.perform()
        sleep(1)
        # actions.reset_actions()
        n = 0

        while True:
            try: 
                WebDriverWait(mv.DRIVER, 1).until(EC.alert_is_present())
                mesg = Alert(mv.DRIVER).text
                mv.isRUN = False
                self.login_signal.emit(mesg)
                Alert(mv.DRIVER).accept()
                return
            except Exception  as e:
                self.login_signal.emit("정상적으로 login되었습니다.")
                mv.isRUN = True
                return



    def logout(self):
        # date select '/html/body/div/nav/div/div[3]/img'
        # tee select  '/html/body/div[1]/nav/div/div[3]/img'
        logoutbtn = mv.DRIVER.find_element(By.XPATH, '/html/body/div/nav/div/div[3]/img')
        actions = ActionChains(mv.DRIVER)
        actions.click(logoutbtn)
        actions.perform()
        Alert(mv.DRIVER).accept()

    def get_basic_tee(self):
        actions = ActionChains(mv.DRIVER)
        reserbtn = mv.DRIVER.find_element(By.XPATH, '//*[@id="main_quick"]/li[1]/a/img')
        actions.click(reserbtn)
        actions.perform()

        # 하루 전 날자 선택하여 기준으로 함(javascript 실행)
        # cal_date = datetime.today() + timedelta(1)
        # year = format(cal_date.year,"4")
        # month = format(cal_date.month, "02")
        # day   = format(cal_date.day, "02")
        # print(year, month,day)
        # script_str = 'Date_Click(' + year + ',' + month + ',' + day + ');'
        # mv.DRIVER.execute_script(script_str)
        # # mv.DRIVER.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/table/tbody/tr[3]/td[6]/a').click()
        # print("script : ", script_str)
        # sleep(2)

        # new  
        # table = mv.DRIVER.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/table/tbody')
        rows =mv.DRIVER.find_elements(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/table/tbody/tr' )
        cols = mv.DRIVER.find_elements(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/table/tbody/tr[2]/td' )
        numofrow = len(rows) + 1
        numofcol = len(cols) + 1
        table_index = 0
        
        for i in range(2, numofrow):
            for j in range(1, numofcol):
                # pc xpath
                # //*[@id="sub_contents"]/div[3]/div/div/div[1]/div/table/tbody/tr[2]/td[4]/a
                # mobile xpath
                ele_xpath = '/html/body/div[1]/div/div[3]/div/div/table/tbody/tr[' + str(i) + ']/td[' + str(j) + ']'
                table_text  = mv.DRIVER.find_element(By.XPATH, ele_xpath).text
                mv.DATE_TABLE.append(ele_xpath)
                if not table_text.find("오늘") < 0 :
                    mv.TODAY_INDEX = table_index
                
                table_index += 1

        if mv.REV_WEEK == 1 :
            add_index = 11
        else:
            add_index = 13



        # print(mv.TODAY_INDEX, mv.DATE_TABLE[mv.TODAY_INDEX + add_index])
        b_date = mv.DRIVER.find_element(By.XPATH, mv.DATE_TABLE[mv.TODAY_INDEX + add_index]).get_attribute('innerText')
        print(f"Tee time 기준 날자 : {b_date[:2]} 일 입니다.")
        self.login_signal.emit(f"Tee time 기준 날자 : {b_date[:2]} 일 입니다.")

        # 시간 table를 갖기 위한 예약 하루 뒤(월요일이면 전주 금요일) 날자 선택
        try:
            mv.DRIVER.find_element(By.XPATH, mv.DATE_TABLE[mv.TODAY_INDEX + add_index]).click()
        except Exception as e:
            self.login_signal.emit(str(e))
            mv.isRUN = False
            return
        
        #  하루 전 tee 시간을 기준하기 위한 tee time 가져 오기
        #  시작 및 종료 시간 string 변환
        fm_str = "00:00" if mv.USER_FMTIME == 0 else format(mv.USER_FMTIME + 4, "02") + ":00"
        to_str = "24:00" if mv.USER_TOTIME == 0 else format(mv.USER_TOTIME + 5, "02") + ":00"  
        tbody = mv.DRIVER.find_element(By.XPATH, '/html/body/div[1]/div/table/tbody/tr/td[1]/table/tbody')
        rows = tbody.find_elements(By.TAG_NAME, 'tr')
        
        for i, value in enumerate(rows):
            body = value.find_elements(By.TAG_NAME, 'td')[0]
            mv.TEE_TABLE.append(body.text)
            if body.text <= fm_str:
                mv.TEE_FM_INDEX = i 
            if body.text < to_str:
                mv.TEE_TO_INDEX = i
        # print(mv.TEE_TABLE, fm_str, to_str)
        # print("time index", mv.TEE_FM_INDEX, mv.TEE_TO_INDEX)
        ##  tee_table은 필요 없을것 같음        
        
        # print(fm_str, mv.TEE_FM_INDEX, to_str, mv.TEE_TO_INDEX, "\n", mv.TEE_TABLE)
