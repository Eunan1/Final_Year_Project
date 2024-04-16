from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QLineEdit
from PyQt6.QtCore import Qt


class CalcField3(QWidget):
    def __init__(self):
        super().__init__()
        self.setupContents()
        self.setupLayout()
        # Connect textChanged signals to the method that will update widths
        self.input_r.textChanged.connect(self.updateLineEditWidthR)
        self.input_N.textChanged.connect(self.updateLineEditWidthN)

    def setupLayout(self):
        self.calc_field1_layout = QHBoxLayout(self)
        self.calc_field1_layout.setSpacing(0)
        self.calc_field1_layout.addStretch(1)
        self.calc_field1_layout.addWidget(self.formula_label1)
        self.calc_field1_layout.addWidget(self.input_r)
        self.calc_field1_layout.addWidget(self.formula_label2)
        self.calc_field1_layout.addWidget(self.input_N)
        self.calc_field1_layout.addStretch(1)
        self.setLayout(self.calc_field1_layout)

    def setupContents(self):
        # Create QLabel for the formula piece "s = "
        self.formula_label1 = QLabel("s = ")
        self.formula_label1.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        
        # Create QLineEdit for "r"
        self.input_r = QLineEdit()
        self.input_r.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_r.setPlaceholderText("r")
        self.input_r.setFixedWidth(26)  # Set initial width

        # Create QLabel for "² mod "
        self.formula_label2 = QLabel("² mod ")
        self.formula_label2.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        # Create QLineEdit for "N"
        self.input_N = QLineEdit()
        self.input_N.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_N.setPlaceholderText("N")
        self.input_N.setFixedWidth(26)  # Set initial width

    def updateLineEditWidthN(self):
        # Adjust the width based on the text length
        sender = self.sender()
        new_width = max(26, 26 * len(sender.text()))  # Assume each character takes about 25px
        sender.setFixedWidth(new_width)
        # Since the width of inputs might have changed, adjust the layout to re-center

    def updateLineEditWidthR(self):
        sender = self.sender()
        new_width = max(26, 26 * len(sender.text()))
        sender.setFixedWidth(new_width)


    # Inside CalcField3 class

    def get_r_value(self):
        try:
            return int(self.input_r.text())
        except ValueError:
            return 0  # or handle invalid input differently

    def get_N_value(self):
        try:
            return int(self.input_N.text())
        except ValueError:
            return 0  # or handle invalid input differently


