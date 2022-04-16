# Import necessary classes and modules:
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QGridLayout,QWidget)
from custom_widget_placeholder import Color

# Class of our GUI:
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initialize_ui()
        self.show()
    
    def initialize_ui(self):
        """
        Initialize the main window and display its contents of the widgets.
        """
        self.setGeometry(40, 40, 800, 900)
        self.setWindowTitle("Grid Sytem Layout PyQt5")
        self.display_content()
    
    