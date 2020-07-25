from functools import wraps
from PyQt5.QtWidgets import *

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