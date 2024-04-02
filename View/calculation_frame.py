from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFrame, QSpacerItem, QSizePolicy
from fyp.utils import load_config

# Load the global configuration file for the entire package
CONFIG = load_config() 


class CalculationFrame(QWidget):
    def __init__(self, calc_field):
        super().__init__()
        self._config = CONFIG['calculationFrame']  # Load configs from JSON calculationFrame
        config_spacer1 = self._config['spacer1'] 
        config_spacer2 = self._config['spacer2']

        self.setupLayout()
        self.setupFrame1(calc_field)  # Adds the main calculation frame to the layout
        self.setupSpacer(config_spacer1['width'], config_spacer1['height'])
        self.setupFrame2()  # Adds the answer box frame to the layout
        self.setupSpacer(config_spacer2['width'], config_spacer2['height'])
        self.setupButton()  # Add the button below the frame

    def setupLayout(self):
        """Initializes the layout of the calculation frame widgets."""
        self.calculation_frame_layout = QVBoxLayout(self)  # Create a QGridLayout for the container frame

    def setupOuterFrame(self):
        """Initializes the outer frame and its layout."""
        self.container_frame = QFrame(self)  # Create the main frame
        self.container_frame.setFrameShape(QFrame.Shape.Box)  # Set the shape of the frame
        self.container_frame_layout = QVBoxLayout(self.container_frame)  # Create a QVBoxLayout within the main frame
        self.container_frame.setLayout(self.container_frame_layout)  # Set the layout for the main frame
        self.container_frame_layout.setContentsMargins(30, 30, 30, 30)  # Set even margins
        self.container_frame.setObjectName("outerFrame")


    def setupFrame1(self, calc_field):
        """Adds frame1 to the vertical layout and arranges formula components."""
        config = self._config['frame1']
        self.frame1 = QFrame()  # Creates the outside frame 1
        self.frame1.setFrameShape(QFrame.Shape.Box) 
        self.frame1.setFixedHeight(config['height'])
        self.frame1.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.frame1.setObjectName("frame1")

        # Create and add CalculationField to frame1 directly
        # Create dummy layout to hold calc_field while it is undefined 
        # Prevents Segmentation because .layout() in calc_field.layout() doesn't work on an undefined variable
        calc_field_layout = QVBoxLayout()
        calc_field_layout.addWidget(calc_field)

        self.frame1.setLayout(calc_field_layout)  # Using the layout from CalcField1
        self.calculation_frame_layout.addWidget(self.frame1)
        
        
    def setupFrame2(self):
        """Adds frame2 to the vertical layout"""
        config = self._config['frame2']
        self.frame2 = QFrame()
        self.frame2.setFrameShape(QFrame.Shape.Box)
        self.frame2.setFixedHeight(config['height'])
        self.frame2.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.frame2.setObjectName("frame2")
        self.calculation_frame_layout.addWidget(self.frame2)
        
    def setupSpacer(self, width, height):
        """Adds a spacer to the QVBoxLayout."""
        
        self.spacer = QSpacerItem(width, height, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.calculation_frame_layout.addSpacerItem(self.spacer)

    def setupButton(self):
        """Adds a calculation button below the frame."""
        config = self._config['button']
        self.button = QPushButton("Calculate")
        self.button.setFixedHeight(config['height'])
        self.button.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.calculation_frame_layout.addWidget(self.button)

