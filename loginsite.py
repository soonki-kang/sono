from selenium.webdriver.common.action_chains    import ActionChains
from selenium.webdriver.common.by               import By
from selenium.webdriver.support.ui              import WebDriverWait 
from selenium.webdriver.common.alert            import Alert
from selenium.webdriver.support                 import expected_conditions as EC 
from PySide6.QtCore                             import  Signal, QObject
from time                                       import  sleep
from myvar                                      import  myVar   as mv

class loginSite(QObject):
    login_signal    =   Signal(str)
    
    def __init__(self):
        super().__init__()


    def login(self):
        # mv.DRIVER.find_element(By.XPATH, '/html/body/table/tbody/tr[1]/td/table[1]/tbody/tr[1]/td[2]/table/tbody/tr/td[7]/a').click()
        # content = mv.DRIVER.find_element(By.NAME, 'iframe')
        # mv.DRIVER.switch_to.frame(content)

        loginid = mv.DRIVER.find_element(By.XPATH, '//*[@id="cyberId"]')
        loginpassword = mv.DRIVER.find_element(By.XPATH, '//*[@id="cyberPass"]' )
        loginbtn = mv.DRIVER.find_element(By.XPATH, '//*[@id="loginBtn"]/a/img')
        
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
                mv.DRIVER.switch_to.default_content()
                return
            except Exception  as e:
                self.login_signal.emit("정상적으로 login되었습니다.")
                mv.isRUN = True
                mv.DRIVER.switch_to.default_content()
                return



    def logout(self):
        # date select '/html/body/div/nav/div/div[3]/img'
        # tee select  '/html/body/div[1]/nav/div/div[3]/img'
        # logoutbtn = mv.DRIVER.find_element(By.XPATH, '//*[@id="mainBody"]/div/div[2]/div/fieldset/div/a[2]/img')
        logoutbtn = mv.DRIVER.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/ul[2]/li[1]/a')

        actions = ActionChains(mv.DRIVER)
        actions.click(logoutbtn)
        actions.perform()
        # Alert(mv.DRIVER).accept()

        ###  //*[@id="mainBody"]/div/div[2]/ul/li[1]/a  골프예약
