from PySide6.QtWidgets  import QApplication, QWidget
from asiadform          import AsiadForm
from myvar              import myVar   as mv
def Main():
    '''
        argv에 의한 browser 선택
        argv[1] : C -->  Chrome
        argv[1] : F -->  Firefox
        Default : Chrome
    '''
    
    import sys, os
    app = QApplication(sys.argv)

    ## resource 위치를 실행화일 위치 기준으로 바꿈(실행화일을 만들때 문제)
    try:
      os.chdir(sys._MEIPASS)
    except:
      os.chdir(os.getcwd())


    if len(sys.argv) > 1 :
        pick = str(sys.argv[1])
        if pick.upper() == "C":
            mv.USER_BROWSER = "Chrome"
        elif pick.upper() == "F":
            mv.USER_BROWSER = "Firefox"
        else:
            print("unknown browser")
            quit()
    else:
        mv.USER_BROWSER = "Chrome"
    
    form = AsiadForm()
    form.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    Main()


