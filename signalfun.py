from datetime           import  datetime, timedelta, time
from PySide6.QtCore     import  QObject, Signal
from myvar              import  myVar  as mv

class signalFun(QObject):
    checkDisplay = Signal(str)

    def __init__(self):
         super().__init__()
   
    def check_date(self, tdate):
         # 요일 추출
         tdate = tdate.toPython()
         current_date = datetime.today()
         current_date = current_date.date()
         mv.REV_WEEK = datetime.isoweekday(tdate)    ##  요일을 1~7로 반환 weekday: 0~6반환
         if mv.REV_WEEK > 5:
            mv.AFTER_CNT = 5 + mv.REV_WEEK 
            cnt_date = tdate + timedelta(days = (-mv.AFTER_CNT))
            mv.BASE_TIME = time(14,0,0)
         else:
            mv.AFTER_CNT = 14
            cnt_date = tdate + timedelta(days = -mv.AFTER_CNT)
            mv.BASE_TIME = time(10,0,0)

         # 지정회원 정의(memver = True이면 지정회원)
         if mv.USER_MEMBER:
            if mv.REV_WEEK >= 6 :
               self.checkDisplay.emit("주말 예약은 불가합니다.")
               return
            else:
               mv.AFTER_CNT = 13
               cnt_date = tdate + timedelta(days = -mv.AFTER_CNT)

         mv.isRUN = False
         curr_time  =  datetime.today().time()
         if current_date > cnt_date:
            self.checkDisplay.emit("예약 날자가 지났습니다.")
            return
         elif current_date != cnt_date :  
            self.checkDisplay.emit("예약 날자가 아닙니다.")
            return
         elif curr_time > mv.BASE_TIME:
            self.checkDisplay.emit("예약 시간이 지났습니다.")
            return
         else:
            self.checkDisplay.emit(f"{tdate.strftime('%y-%m-%d')} 예약을 시작합니다.")

         mv.isRUN = True
