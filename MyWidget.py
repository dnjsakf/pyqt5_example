# MyWidget.py
from functools import wraps
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QDialog
    

# 데코레이터
def addHBox(func):
  @wraps(func)
  def wrapper(self, *args, **kwargs):
    hbox = QHBoxLayout()
    
    widgets = func(self, *args, **kwargs)
    if isinstance( widgets, list ):
      for widget in widgets:
        hbox.addWidget(widget)
    else:
      hbox.addWidget(widgets)
  
    self.main_layout.addLayout(hbox)
  return wrapper

def addHBoxWithGrid(func):
  @wraps(func)
  def wrapper(self, *args, **kwargs):
    row = kwargs.get("row", 0)
    col = kwargs.get("col", 0)
    rowspan = kwargs.get("rowspan", 1)
    colspan = kwargs.get("colspan", 1)
    
    # Sub Layout 생성
    # QHBoxLayout: Widget을 가로방향으로 나열
    hbox = QHBoxLayout()
    
    # hbox에 위젯 추가
    widgets = func(self, *args, **kwargs)
    if isinstance( widgets, list ):
      for widget in widgets:
        hbox.addWidget(widget)
    else:
      hbox.addWidget(widgets)
    
    # Sub Layout을 Main Layout에 추가
    self.main_layout.addLayout(hbox, row, col, rowspan, colspan)
    
  return wrapper

  
# Main Dialog Widget
class MainDialogWidget(QWidget):
  def __init__(self, parent=None, *args, **kwargs):
    super(MainDialogWidget, self).__init__(parent, *args, **kwargs)
    
    # 설정값
    self.parent = parent
    self.args = args
    self.kwargs = kwargs
    
    # 입력 Widget 저장소
    self.form = {}
    
    # UI 렌더링
    self.render()
  
  # UI 렌더링
  def render(self):
    # Main Layout 생성
    # QGridLayout: Layout, Widget을 지정된 위치(row, col)에 나열.
    self.main_layout = QVBoxLayout(self)
    
    # Main Layout에 Sub Layout, Widget 추가
    self.addTextInput(
      label="이름",
      name="username",
    )
    self.addButton(
      label="취소",
      onClick=self.handleClose
    )
    self.addButton(
      label="확인",
      onClick=self.handleSubmit
    )
    
    # Main Layout 설정
    self.setLayout(self.main_layout)
  
  # Text Input 위젯 추가
  @addHBox
  def addTextInput(self, label=None, name=None, **kwargs):  
    w_label = QLabel(label)
    w_input = QLineEdit()
    
    if name is not None:
      self.form[name] = w_input
    
    return [ w_label, w_input ]
   
  # Button 위젯 추가
  @addHBox
  def addButton(self, label=None, onClick=None, **kwargs):  
    w_button = QPushButton(label)
    w_button.clicked.connect( onClick(**kwargs) )
    
    return w_button
    
  def addButtonGroup(self, label=None, 
  
  # 이벤트 핸들러
  def handlePrintText(self, target=None, **kwargs):
    def handle( res ):
      w_target = self.form.get(target, None)
      
      print( w_target.text() );
    
      return res
    return handle
  
  # 취소
  def handleSubmit(self, *args, **kwargs):
    return self.parent.accept
  
  # 확인  
  def handleClose(self, *args, **kwargs):
    return self.parent.reject

    
# Main Dialog
class MainDialog(QDialog):
  def __init__(self, parent=None, *args, **kwargs):
    super(QDialog, self).__init__(parent, *args, **kwargs)
    
    # 설정값
    self.parent = parent
    self.args = args
    self.kwargs = kwargs
        
    # UI 렌더링
    self.render()
    
  # UI 렌더링
  def render(self):
    self.init_window()
    self.init_widget()
    
  # Window 렌더링
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
    
  # 메인 위젯 설정
  def init_widget(self):
    self.main_layout = QVBoxLayout()    
    self.main_widget = MainDialogWidget(self)
    self.main_layout.addWidget(self.main_widget)    
    self.setLayout(self.main_layout)
  

# 메인 위젯
class MainWidget(QWidget):
  def __init__(self, parent=None, *args, **kwargs):
    super(MainWidget, self).__init__(parent, *args, **kwargs)
    
    # 설정값
    self.parent = parent
    self.args = args
    self.kwargs = kwargs
    
    # 입력 Widget 저장소
    self.form = {}
    
    # UI 렌더링
    self.render()
  
  # UI 렌더링
  def render(self):
    # Main Layout 생성
    # QGridLayout: Layout, Widget을 지정된 위치(row, col)에 나열.
    self.main_layout = QGridLayout(self)
    
    # Main Layout에 Sub Layout, Widget 추가
    self.addTextInput(
      label="이름:", 
      name="username", 
      row=0,
      col=0
    )
    self.addButton(
      label="이름 출력",
      row=0,
      col=1,
      target="username",
      onClick=self.handlePrintText
    )
    self.addModalButton(
      label="팝업",
      row=1,
      col=0,
      colspan=2,
      target="username",
      onClick=self.handleOpenModal
    )
    
    # Main Layout 설정
    self.setLayout(self.main_layout)
  
  
  # Text Input 위젯 추가
  @addHBoxWithGrid
  def addTextInput(self, label=None, name=None, **kwargs):  
    w_label = QLabel(label)
    w_input = QLineEdit()
    
    if name is not None:
      self.form[name] = w_input
    
    return [ w_label, w_input ]
   
  # Button 위젯 추가
  @addHBoxWithGrid
  def addButton(self, label=None, onClick=None, **kwargs):  
    w_button = QPushButton(label)
    w_button.clicked.connect( onClick(**kwargs) )
    
    return w_button
  
  # Button 위젯 추가
  @addHBoxWithGrid
  def addModalButton(self, label=None, onClick=None, **kwargs):  
    w_button = QPushButton(label)
    w_button.clicked.connect( onClick(**kwargs) )
    
    return w_button

    
  # Console Print 이벤트 핸들러
  def handlePrintText(self, target=None, **kwargs):
    def handle( flag ):
      w_target = self.form.get(target, None)
      
      print( w_target.text() );
      
      w_target.setText("")
    
      return flag
    return handle
    
  # Modal 이벤트 핸들러
  def handleOpenModal(self, form=None, **kwargs):
    def handle( flag ):
      width = kwargs.get("width", 300)
      height = kwargs.get("height", 100)
    
      dialog = MainDialog(self, width=width, height=height)
      modal = dialog.exec_()
      
      print( modal )
    
      return flag
    return handle
