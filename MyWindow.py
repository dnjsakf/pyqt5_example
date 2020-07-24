# MyWindow.py
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
from MyWidget import MainWidget
   
# 메인 윈도우
class MainWindow(QMainWindow):
  def __init__(self, *args, **kwargs):
    super(QMainWindow, self).__init__()
    
    # 상태값 설정
    self.args = args
    self.kwargs = kwargs
    
    # UI 렌더링
    self.render()
    
  # UI 렌더링
  def render(self):
    self.init_window()
    self.init_widget()
    
  # 윈도우 설정
  def init_window(self):
    # 설정값
    title = self.kwargs.get("title", "Main Window")
    posX = self.kwargs.get("posX", 0)
    posY = self.kwargs.get("posY", 0)
    width = self.kwargs.get("width", 300)
    height = self.kwargs.get("height", 200)
    
    # 제목 설정
    self.setWindowTitle(title)
    
    # 크기 및 위치 설정
    self.setGeometry(posX, posY, width, height)
    
    # 화면 가운데 정렬
    frame_geo = self.frameGeometry()
    desktop_center = QDesktopWidget().availableGeometry().center()
    frame_geo.moveCenter(desktop_center)
    self.move(frame_geo.topLeft())

  # 메인 위젯 설정
  def init_widget(self):
    self.main_widget = MainWidget(self)
    self.setCentralWidget(self.main_widget)
