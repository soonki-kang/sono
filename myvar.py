from datetime import time


class myVar():
    USER_ID = ""
    USER_PASSWORD = ""
    USER_MEMBER = 1
    USER_REVDATE = None
    USER_FMTIME = 0
    USER_TOTIME = 0
    USER_COURSE = 0
    USER_SITE = "소노펠리체 컨트리클럽"
    USER_BROWSER = None
    USER_URL = 'https://www.sonofelicecc.com/main.dp/dmparse.dm'
    # USER_URL = 'http://golf.edenvalley.co.kr/Member/view.asp?location=01/'
    # USER_URL = 'http://google.com'
    # USER_URL = 'http://abctdef1s.com'
    DRIVER = None
    isRUN = True
    isThreadRun = True
    BASE_TIME = time(9, 0, 0)
    REV_WEEK = 0
    AFTER_CNT = 0
    DIFF_TIME = 0
    myweb = None
    DATE_TABLE = []
    TEE_TABLE = []
    TODAY_INDEX = 0
    TEE_FM_INDEX = 0
    TEE_TO_INDEX = 0
    STRREVFMTIME = ''
    STRREVTOTIME = ''
    PROBNO = 0
    WAITCONDITION = ''
    MUTEX = ''
