from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFrame, QLabel, QSpacerItem, QSizePolicy
from PyQt6.QtCore import Qt
from fyp.utils import load_config
from fyp.view.calc_field2 import CalcField2
from fyp.view.calc_field3 import CalcField3

# Load the global configuration file for the entire package
CONFIG = load_config()

class CalculationFrame(QWidget):
    def __init__(self, calc_field):
        super().__init__()
        self._config = CONFIG['calculationFrame']  # Load configs from JSON calculationFrame
        self.calc_field = calc_field  # Store the calc_field for later use in calculations

        self.setupLayout()
        self.setupFrame1(self.calc_field)  # Adds the main calculation frame to the layout
        self.setupSpacer(self._config['spacer1']['width'], self._config['spacer1']['height'])
        self.setupFrame2()  # Adds the answer box frame to the layout
        self.setupSpacer(self._config['spacer2']['width'], self._config['spacer2']['height'])
        self.setupButton()  # Add the button below the frame
        self.frame2.setLayout(QVBoxLayout())  # Ensure frame2 has a layout

    def setupLayout(self):
        """Initializes the layout of the calculation frame widgets."""
        self.calculation_frame_layout = QVBoxLayout(self)

    def setupFrame1(self, calc_field):
        """Adds frame1 to the vertical layout and arranges formula components."""
        config = self._config['frame1']
        self.frame1 = QFrame()
        self.frame1.setFrameShape(QFrame.Shape.Box)
        self.frame1.setFixedHeight(config['height'])
        self.frame1.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.frame1.setObjectName("frame1")

        calc_field_layout = QVBoxLayout()
        calc_field_layout.addWidget(calc_field)
        self.frame1.setLayout(calc_field_layout)
        self.calculation_frame_layout.addWidget(self.frame1)

    def setupFrame2(self):
        """Adds frame2 to the vertical layout."""
        config = self._config['frame2']
        self.frame2 = QFrame()
        self.frame2.setFrameShape(QFrame.Shape.Box)
        self.frame2.setFixedHeight(config['height'])
        self.frame2.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.frame2.setObjectName("frame2")
        self.calculation_frame_layout.addWidget(self.frame2)

    def setupSpacer(self, width, height):
        """Adds a spacer to the QVBoxLayout."""
        spacer = QSpacerItem(width, height, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.calculation_frame_layout.addSpacerItem(spacer)

    def setupButton(self):
        """Adds a calculation button below the frame."""
        config = self._config['button']
        self.button = QPushButton("Calculate")
        self.button.setFixedHeight(config['height'])
        self.button.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.calculation_frame_layout.addWidget(self.button)
        self.button.clicked.connect(self.calculate)


    def displayResult(self, result):
        # Clear the layout first to remove previous result
        for i in reversed(range(self.frame2.layout().count())): 
            widget_to_remove = self.frame2.layout().itemAt(i).widget()
            self.frame2.layout().removeWidget(widget_to_remove)
            widget_to_remove.deleteLater()
        
        # Create a QLabel to display the result and add it to frame2's layout
        result_label = QLabel(str(result))
        result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        result_label.setStyleSheet("font-size: 20px; font-weight: bold; color :white")
        self.frame2.layout().addWidget(result_label)




        # Modify the calculate method in CalculationFrame
    def calculate(self):
        if isinstance(self.calc_field, CalcField3):  # Assuming CalcField1 for the r^2 mod N calculation
            r = self.calc_field.get_r_value()
            N = self.calc_field.get_N_value()
            if r is not None and N is not None and N != 0:
                result = (r ** 2) % N
                self.displayResult(f"The result is: {result}")
            else:
                self.displayResult("Invalid input for r or N.")
        elif isinstance(self.calc_field, CalcField2):  # Checking if the current calc_field is CalcField2
            a = self.calc_field.get_a_value()
            N = self.calc_field.get_N_value()
            if a is not None and N is not None and N != 0:
                # Check if a is a quadratic residue modulo N using Euler's criterion
                if pow(a, (N - 1) // 2, N) == 1:
                    self.displayResult("Yes: \n a is a quadratic residue mod N")
                else:
                    self.displayResult("No: a is not a quadratic residue mod N")
            else:
                self.displayResult("Invalid input for a or N.")
        else:
            # Handle other fields or default case
            self.displayResult("Please provide valid input values.")

