# MyWidget.py
import utils.decorators.layouts as withLayout

from PyQt5.QtWidgets import *
from dialogs.form import FormDialog

# 메인 위젯
class FormWidget(QWidget):
  def __init__(self, parent=None, *args, **kwargs):
    super(FormWidget, self).__init__(parent, *args, **kwargs)
    
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
  @withLayout.addHBoxWithGrid
  def addTextInput(self, label=None, name=None, **kwargs):  
    w_label = QLabel(label)
    w_input = QLineEdit()
    
    if name is not None:
      self.form[name] = w_input
    
    return [ w_label, w_input ]
   
  # Button 위젯 추가
  @withLayout.addHBoxWithGrid
  def addButton(self, label=None, onClick=None, **kwargs):  
    w_button = QPushButton(label)
    w_button.clicked.connect( onClick(**kwargs) )
    
    return w_button
  
  # Button 위젯 추가
  @withLayout.addHBoxWithGrid
  def addModalButton(self, label=None, onClick=None, **kwargs):  
    w_button = QPushButton(label)
    w_button.clicked.connect( onClick(**kwargs) )
    
    return w_button

    
  # Console Print 이벤트 핸들러
  def handlePrintText(self, target=None, **kwargs):
    def handle( flag ):
      w_target = self.form.get(target, None)
      
      print( w_target.text() )
      
      w_target.setText("")
    
      return flag
    return handle
    
  # Modal 이벤트 핸들러
  def handleOpenModal(self, form=None, **kwargs):
    def handle( flag ):
      width = kwargs.get("width", 300)
      height = kwargs.get("height", 100)
    
      dialog = FormDialog(self, width=width, height=height)
      modal = dialog.exec_()
      
      print( modal )
    
      return flag
    return handle
