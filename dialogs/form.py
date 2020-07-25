import utils.decorators.layouts as withLayout

from PyQt5.QtWidgets import *
from .widgets.form import FormDialogWidget

# Main Dialog
class FormDialog(QDialog):
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
    self.main_widget = FormDialogWidget(self)
    self.main_layout.addWidget(self.main_widget)    
    self.setLayout(self.main_layout)