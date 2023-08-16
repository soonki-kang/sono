from datetime           import  datetime, timedelta, time
from PySide6.QtCore     import  QObject, Signal
from myvar              import  myVar  as mv

class signalFun(QObject):
    checkDisplay = Signal(str)

    def __init__(self):
         super().__init__()
   
    def check_date(self, tdate):
         # 요일 추출
         mv.isRUN = False
         tdate = tdate.toPython()
         current_date = datetime.today()
         current_date = current_date.date()
         curr_week    = datetime.isoweekday(current_date)
         curr_time    = datetime.today().time()
         mv.REV_WEEK = datetime.isoweekday(tdate)    ##  요일을 1~7로 반환: weekday: 0~6반환
         
         
         # 월요일부터 주말까지 월요일에 일괄 예약함.
         if curr_week != 1 :
             self.checkDisplay.emit('월요일이 아닙니다.')
             return
         
         if curr_time > mv.BASE_TIME :
             self.checkDisplay.emit('예약 시간이 지났습니다.')
             return
         
         # 예약 일자가  현재일 부터 4주 후 날자에 해당하는가?
         # 예약 가능 시작일(avail_fm_date) 및
         # 예약 가능 종료일(avail_to_date) 계산(4주 후 월요일과 일요일)
         avail_fm_date = current_date + timedelta( days = 29 - curr_week)
         avail_to_date = avail_fm_date + timedelta(days =  6)

         if avail_fm_date > tdate  or tdate > avail_to_date :
             self.checkDisplay.emit("4주 후 주간만 예약 가능합니다.")
             return 

         self.checkDisplay.emit(f"{tdate.strftime('%y-%m-%d')}일이 지정되었습니다.")

         mv.isRUN = True
