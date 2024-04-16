from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QFrame, QSizePolicy
from PyQt6.QtCore import Qt


class CalcField2(QWidget):
    def __init__(self):
        super().__init__()
        self.setupStartLabel()
        self.setupBracketLabels()
        self.setupFraction()
        self.setupLayouts()

        # Conntect to QLineEdits to change its width based on extra inputs
        self.input_numerator.textChanged.connect(self.updateLineEditWidth)
        self.input_denominator.textChanged.connect(self.updateLineEditWidth)

        # Connecto to QLineEdits to ensure both are always centred according to largest input
        self.input_numerator.textChanged.connect(self.recenterLayout)
        self.input_denominator.textChanged.connect(self.recenterLayout)


    def updateLineEditWidth(self):
        # Assuming self.input_numerator and self.input_denominator are your two QLineEdit widgets
        max_width = max(
            26 * len(self.input_numerator.text()), 
            26 * len(self.input_denominator.text())
        )
        max_width = max(26, max_width)  # Ensure minimum width remains

        # Update the widths of both LineEdits
        self.input_numerator.setFixedWidth(max_width)
        self.input_denominator.setFixedWidth(max_width)


    def recenterLayout(self):
        # This is a simplified example. You would need to adapt it to your specific layout.
        # Assuming self.calculation_layout is your main QHBoxLayout:
        self.calculation_layout.setStretchFactor(self.input_numerator, 1)
        self.calculation_layout.setStretchFactor(self.input_denominator, 1)
        # Ensure other elements in the layout are adjusted as needed to maintain centering


    def setupLayouts(self):
        self.fraction_layout.addStretch(1)
        self.fraction_layout.addWidget(self.input_numerator)
        self.fraction_layout.addWidget(self.fraction_line)
        self.fraction_layout.addWidget(self.input_denominator)
        self.fraction_layout.addStretch(1)

        self.calculation_layout = QHBoxLayout(self)
        self.calculation_layout.setSpacing(0)
        #self.fraction_layout.setSpacing(0)

        # Adding widgets to the layout
        self.calculation_layout.addStretch(1)
        self.calculation_layout.addWidget(self.formula_label1)
        self.calculation_layout.addWidget(self.formula_label2)
        self.calculation_layout.addLayout(self.fraction_layout)
        self.calculation_layout.addWidget(self.formula_label3)
        self.calculation_layout.addStretch(1)

       

        
    def setupStartLabel(self):
        # Create QLabel for 'x = '
        self.formula_label1 = QLabel("x = ")
        self.formula_label1.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.formula_label1.setObjectName("formulaLabel1")

    
    def setupBracketLabels(self):
        self.formula_label2 = QLabel("(")
        self.formula_label2.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.formula_label2.setObjectName("bracket1")

        # Create QLabel for ')'
        self.formula_label3 = QLabel(")")
        self.formula_label3.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.formula_label3.setObjectName("bracket2")


    def setupFraction(self):
        # Create QVBoxLayout with a QLineEdit, a straight line/QFrame and another QLineEdit for
        self.fraction_layout = QVBoxLayout()
        self.fraction_layout.setSpacing(0)
        
        # Create QLineEdit for the numerator 'a'
        self.input_numerator = QLineEdit()
        self.input_numerator.setPlaceholderText("ɑ")
        self.input_numerator.setFixedWidth(26)
        self.input_numerator.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_numerator.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        

        # Create QFrame for the fraction symbol '-'
        self.fraction_line = QFrame()
        self.fraction_line.setFrameShape(QFrame.Shape.HLine)  # Horizontal line
        self.fraction_line.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.fraction_line.setObjectName("fractionLine")


        # Create QLineEdit for the denominator 'b'
        self.input_denominator = QLineEdit()
        self.input_denominator.setPlaceholderText("N")
        self.input_denominator.setFixedWidth(26)
        self.input_denominator.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_denominator.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

    


        # Add these methods inside the CalcField2 class

    def get_a_value(self):
        try:
            return int(self.input_numerator.text())
        except ValueError:
            return None  # None indicates invalid input

    def get_N_value(self):
        try:
            return int(self.input_denominator.text())
        except ValueError:
            return None  # None indicates invalid input
