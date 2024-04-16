from PyQt6.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QSpacerItem, QSizePolicy, QFrame, QHBoxLayout, QTabWidget, QLabel
from PyQt6.QtCore import Qt
from fyp.view.calculation_frame import CalculationFrame  # Update this import as necessary
from fyp.view.calc_field1 import CalcField1
from fyp.view.calc_field2 import CalcField2
from fyp.view.calc_field3 import CalcField3
from fyp.view.zero_knowledge import ZeroKnowledge

from fyp.utils import load_config 

# Load the global configuration file for the entire package
CONFIG = load_config()

class OverallStructure(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setupLayout()
        self.addLeftFrame()
        self.addSpacer()
        self.addRightFrame()

        # Initialize the main grid layout

    def setupLayout(self):
        self.setWindowTitle("Quadratic Residues GUI Calculator Tool")
        self.setWindowState(Qt.WindowState.WindowMaximized)
        self.setContentsMargins(200, 75, 200, 75)

        self.main_horizontal_layout = QHBoxLayout(self)


    def addLeftFrame(self):
        self.frame_left = QFrame()
        self.frame_left.setFrameShape(QFrame.Shape.Box)
        self.frame_left.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        self.frame_left.setObjectName("frame_left")

        self.main_horizontal_layout.addWidget(self.frame_left)
        self.main_horizontal_layout.setSpacing(0)

        self.frame_left_layout = QVBoxLayout(self.frame_left)
        self.frame_left_layout.setSpacing(0)
        
        
        # Create a QTabWidget
        self.tabWidget = QTabWidget()
        self.tabWidget.tabBar().setExpanding(True)
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)  # Set tab position
        self.tabWidget.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)


        self.addTab1Contents()
        self.addTab2Contents()
        self.addTab3Contents()

        self.frame_left_layout.addWidget(self.tabWidget)  # Add the tab widget to the frame layout


    
    def addTab1Contents(self):
        calcField1 = CalcField1()
        calcBox1 = CalculationFrame(calcField1)

        # Create first tab
        self.tab1 = QWidget()
        self.tab1_layout = QVBoxLayout(self.tab1)
        self.tab1_layout.setContentsMargins(100, 50, 100, 50)
        self.tab1_layout.addWidget(calcBox1)
        self.tabWidget.addTab(self.tab1, "Quadratic Residues")

    
    def addTab2Contents(self):
        calcField2 = CalcField2()
        calcBox2 = CalculationFrame(calcField2)

        # Create second tab
        self.tab2 = QWidget()
        self.tab2_layout = QVBoxLayout(self.tab2)
        self.tab2_layout.setContentsMargins(100, 50, 100, 50)
        self.tab2_layout.addWidget(calcBox2)
        self.tabWidget.addTab(self.tab2, "Legendre Symbol")

    
    def addTab3Contents(self):
        calcField3 = CalcField3()
        calcBox3 = CalculationFrame(calcField3)

        # Create third tab
        tab3 = QWidget()
        tab3_layout = QVBoxLayout(tab3)
        tab3_layout.setContentsMargins(100, 50, 100, 50)
        tab3_layout.addWidget(calcBox3)
        self.tabWidget.addTab(tab3, "Proof Calculation")


    def addSpacer(self):
        """ Adds spacer to the main QHBoxLayout. """
        self.new_spacer = QSpacerItem(60, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        self.main_horizontal_layout.addSpacerItem(self.new_spacer)
        


    def addRightFrame(self):

        self.frame_right = QFrame()
        self.frame_right.setFrameShape(QFrame.Shape.Box)
        self.frame_right.setObjectName("frame_right")
        self.main_horizontal_layout.addWidget(self.frame_right)

        self.frame_right_layout = QVBoxLayout(self.frame_right)
        self.frame_right_layout.setContentsMargins(50, 50, 50, 50)
        
        self.zero_knowledge = ZeroKnowledge()
        self.frame_right_layout.addWidget(self.zero_knowledge)




