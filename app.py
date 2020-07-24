# app.py
import sys

from PyQt5.QtWidgets import QApplication
from MyWindow import MainWindow

if __name__ == '__main__':  
  app = QApplication( sys.argv )
  win = MainWindow(
    title="메인 윈도우", 
    posX=100, posY=400, 
    width=300, height=200
  )
  win.show()
  
  sys.exit( app.exec() )