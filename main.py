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
    
    def display_content(self):
        """
        Display the color in grid systm on the main window.
        """
        # Create grid layout:
        grid_layout = QGridLayout()
        # Create the container:
        container = QWidget()
        # Create color && add it to the grid layout:
        grid_layout.addWidget(Color("Magenta"),0,0,1,3)
        grid_layout.addWidget(Color("Yellow"),1,0,1,2)
        grid_layout.addWidget(Color("Orange"),1,2,1,1)
        grid_layout.addWidget(Color("Magenta"),2,0,1,3)
        grid_layout.addWidget(Color("Teal"),3,0,1,1)
        grid_layout.addWidget(Color("Pink"),3,1,1,2)
        # Set the grid layout to the container:
        container.setLayout(grid_layout)
        # Set the container to be the central widget of the main window:
        self.setCentralWidget(container)

# Run the program:
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())


