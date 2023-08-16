from PySide6.QtWidgets import QApplication
from PySide6 import QtCore
from myvar import myVar as mv
from intro import Intro
from probnopopup import ProbNo

mv.WAITCONDITION = QtCore.QWaitCondition()
mv.MUTEX = QtCore.QMutex()


def Main():
    '''
        argv에 의한 browser 선택
        argv[1] : C -->  Chrome
        argv[1] : F -->  Firefox
        Default : Chrome
    '''

    import sys
    import os
    app = QApplication(sys.argv)

    # resource 위치를 실행화일 위치 기준으로 바꿈(실행화일을 만들때 문제)
    if getattr(sys, 'frozen', False):
        pd = os.path.dirname(os.path.abspath(sys.executable))
    else:
        pd = os.path.dirname(os.path.abspath(__file__))

    # try:
    #   os.chdir(sys._MEIPASS)
    # except:
    #   os.chdir(os.getcwd())

    os.chdir(pd)

    if len(sys.argv) > 1:
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

    # Form 생성 및 실행
    form = Intro()
    form.show()
    # prob = ProbNo()
    # prob.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    Main()
