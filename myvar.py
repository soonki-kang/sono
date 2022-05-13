from datetime     import time
class myVar():
  USER_ID = ""
  USER_PASSWORD = ""
  USER_MEMBER = False
  USER_REVDATE = None
  USER_FMTIME = 0
  USER_TOTIME = 0
  USER_COURSE = 0
  USER_SITE = "아시아드컨트리클럽"
  USER_BROWSER = None
  # pc url
  # USER_URL = 'https://www.asiadcc.co.kr/html/member/login.asp'
  # mobile url
  USER_URL = 'https://www.asiadcc.co.kr/mobile/login.asp'
  # USER_URL = 'http://google.com'
  # USER_URL = 'http://abctdef1s.com'
  DRIVER = None
  isRUN  = True
  BASE_TIME = time(10,0,0)
  REV_WEEK = 0
  AFTER_CNT = 0
  DIFF_TIME = 0
  myweb = None
  DATE_TABLE = []
  TEE_TABLE  = []
  TODAY_INDEX = 0
  TEE_FM_INDEX = 0
  TEE_TO_INDEX = 0
  