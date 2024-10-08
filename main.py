import sys # 시스템 제어 관련 모듈

# 위젯이란? GUI 프로그램에서 구성요소를 뜻하는 용어
from ui import View # QMessageBox : 메시지박스 위젯
from ctrl import Control                                                              # Icon을 추가하기 위한 라이브러리
from PyQt5.QtWidgets import QApplication
# 나는 계산기 유형을 직접 정의한다! 이때 Qwidget에 기반을 둔다
'''class Calculator(QWidget) :

    def __init__(self) :
        super().__init__()                                                                 # 뭔가에 기반을 둘 경우 써줘야 하는 코드
        self.initUI()

    def initUI(self) :


        self.te1 = QPlainTextEdit()
        self.te1.setReadOnly(True)

        self.btn1 = QPushButton('Message', self)                                           # 버튼추가
        self.btn1.clicked.connect(self.activateMessage)                                    # 이벤트 핸들링 : 클릭했을 때, 뭐를 할거다! 라고 정하는 것
        
        self.btn2 = QPushButton('Clear', self)
        self.btn2.clicked.connect(self.clearMessage)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)

       
        vbox = QVBoxLayout()
        vbox.addWidget(self.te1)                                                               # 수직 레이아웃 위젯 생성
        vbox.addLayout(hbox)                                                                 # 빈 공간
        vbox.addStretch(1)
        vbox.addWidget(self.btn1)                                                          # 버튼 위치
        vbox.addStretch(1)
                                                                         # 빈 공간

        self.setLayout(vbox)                                                               # 설정 적용

        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))                                              # 윈도 아이콘 추가
        self.resize(256, 256)
        self.show()
    
    def clearMessage(self) :
        self.te1.clear()

    def activateMessage(self) :
        self.te1.appendPlainText("Hello, PyQt App!")                                                            # 버튼을 클릭할 때 동작하는 함수 : 메세지 박스 출력
        #QMessageBox.information(self, "information", "Button Clicked!")

# 클래스를 정의했으나, 여기에서 실행하겠다..라는 실행부
# if __name__ == '__main__' : 이 모듈이 직접 실행되는 경우라는 뜻
if __name__ == '__main__' :
    app = QApplication(sys.argv)      # Qt 프로그램 실행코드
    view = Calculator()               # 내가 만든 계산기 GUI 생성코드
    sys.exit(app.exec_())             # 계산기 종료 시 시스템 종료 명령'''
def main() :
    calc = QApplication(sys.argv)
    app = QApplication(sys.argv)
    view = View()
    Control(view = view)
    sys.exit(app.exec_())

if __name__ == '__main__' :
    main()