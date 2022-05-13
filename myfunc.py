from os                 import  environ
import socket, struct
from datetime           import  datetime

# 해상도별 글자 크기 강제하는 함수
def suppress_qt_warnings():
    '''
    os의 environ를 import하여야 함
    해상도와 상관없이 일정한 크기로 글자 유지
    '''
    environ["QT_DIVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"   # True 모니터의 픽셀 밀도에 따라 자동 크기 조정을 활성화
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"       # True 각 화면에 대한 축척 계수를 지정,포인트 크기 글꼴의 크기는 변경되지 않음
    environ["QT_SCALE_FACTOR"] = "1"               #      포인트 크기 글꼴을 포함하여 전체 응용 프로그램에 대한 전역 배율을 정의


def time_check(local_zone):
    mesg = ""
    current_ntp_time = get_ntp_time(local_zone)
    current_svr_time = datetime.now().timestamp()
    time_interval = current_ntp_time - current_svr_time
    time_interval = current_svr_time - current_ntp_time
    # print("ntp time : ", current_ntp_time)
    # print("svr time : ", current_svr_time)
    # print("inter time : ", abs(time_interval))
    if abs(time_interval) > 2 :
      print("시간 차이 : ", time_interval)
      mesg = "표준시와 PC의 시간 차이가 2초 이상입니다.\nPC 시간을 동기화 하세요! (" + str(int(time_interval)) + ")"
    else:
      mesg = ""
    return mesg
def get_ntp_time(addr):
    TIME1970 = 2208988800      # Reference time
    client = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
    data = b'\x1b' + 47 * b'\0'
    client.sendto( data, (addr, 123))  #time.windows.com에서 서울 표준시를 가져옴
    data, address = client.recvfrom( 1024 )
    if data:
        t = struct.unpack( '!12I', data )[10]
        if t == 0 :
            raise 'invalid response'
        t -= TIME1970
        diff_time = t
        # ninehour = 9*60*60
        # seoultime = time.gmtime(t - TIME1970 + ninehour)
        # ninehour = t + 9*60*60
        # windows의 date setting시 super user권한 획득 필요
        # seoultime = time.gmtime(t)
        # date_str = time.strftime('%Y-%m-%d',seoultime)
        # time_str = time.strftime('%H:%M:%S',seoultime)
        # date_command = ['powershell.exe','Start-Process','date %s'%date_str,'${env:ProgramFiles(x86)}\test\setting.ini','-Verb','runAs']
        # time_command = ['powershell.exe','Start-Process','time %s'%time_str,'${env:ProgramFiles(x86)}\test\setting.ini','-Verb','runAs']
        # subprocess.run(date_command, shell=True)
        # subprocess.run(time_command, shell=True)
        # subprocess.call(['runas','user:Administrator', 'date %s'%date_str])
        # date_command = 'cmd /c date %s'%date_str
        # time_command = 'cmd /c time %s'%time_str
        # os.system(date_command)
        # os.system(time_command)
    else:
        raise 'no data returned'
    return t
