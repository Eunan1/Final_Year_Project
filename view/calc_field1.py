from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QLineEdit
from PyQt6.QtCore import Qt


class CalcField1(QWidget):
    def __init__(self):
        super().__init__()
        self.setupContents()
        self.setupLayout()
        self.input_N.textChanged.connect(self.updateLineEditWidth)

    def setupLayout(self):
        self.calculation_layout = QHBoxLayout(self)  # Create a horizontal layout associated with this widget
        self.calculation_layout.setSpacing(0)  # Set the spacing between widgets in the layout to 0

        # Adding widgets to the layout
        self.calculation_layout.addStretch(1)  # Add stretch before widgets to push them to the center
        self.calculation_layout.addWidget(self.formula_label)  # Add the label to the layout
        self.calculation_layout.addWidget(self.input_N)  # Add the QLineEdit to the layout
        self.calculation_layout.addStretch(1)  # Add stretch after widgets to ensure centering

        # Set the layout to the widget
        self.setLayout(self.calculation_layout)

    def setupContents(self):
        # Create QLabel for the formula "y² = a mod "
        self.formula_label = QLabel("y² = ɑ mod ")
        self.formula_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create QLineEdit for 'N'
        self.input_N = QLineEdit()
        self.input_N.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Keep text aligned left to flow into the equation
        self.input_N.setPlaceholderText("N")
        self.input_N.setFixedWidth(26)

        
    def updateLineEditWidth(self):
        # Adjust the width based on the text length
        sender = self.sender()
        new_width = max(26, 26 * len(sender.text()))  # Assume each character takes about 25px
        sender.setFixedWidth(new_width)
        # Since the width of inputs might have changed, adjust the layout to re-center



    # Existing methods remain unchanged

    def get_N_value(self):
        """Return the integer value of N, or None if the input is invalid."""
        try:
            return int(self.input_N.text())
        except ValueError:
            return None
