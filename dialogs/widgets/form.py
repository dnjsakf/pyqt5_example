import utils.decorators.layouts as withLayout

from PyQt5.QtWidgets import *

# Main Dialog Widget
class FormDialogWidget(QWidget):
  def __init__(self, parent=None, *args, **kwargs):
    super(FormDialogWidget, self).__init__(parent, *args, **kwargs)
    
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
  @withLayout.addHBox
  def addTextInput(self, label=None, name=None, **kwargs):  
    w_label = QLabel(label)
    w_input = QLineEdit()
    
    if name is not None:
      self.form[name] = w_input
    
    return [ w_label, w_input ]
   
  # Button 위젯 추가
  @withLayout.addHBox
  def addButton(self, label=None, onClick=None, **kwargs):  
    w_button = QPushButton(label)
    w_button.clicked.connect( onClick(**kwargs) )
    
    return w_button
    
  # 이벤트 핸들러
  def handlePrintText(self, target=None, **kwargs):
    def handle( res ):
      w_target = self.form.get(target, None)
      
      print( w_target.text() )
    
      return res
    return handle
  
  # 취소
  def handleSubmit(self, *args, **kwargs):
    return self.parent.accept
  
  # 확인  
  def handleClose(self, *args, **kwargs):
    return self.parent.reject

    

  
