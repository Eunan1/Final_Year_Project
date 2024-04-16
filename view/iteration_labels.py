

from PyQt6.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QWidget, QSizePolicy, QFrame, QSpacerItem
from PyQt6.QtCore import Qt



class IterationLabels(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupIterationDetails()


    def setupIterationDetails(self):
        """ Set up the iteration details layout and add labels and stretches to it. """
        self.full_iteration_details_layout = QHBoxLayout(self)

        self.iteration_details_layout = QVBoxLayout()
        self.iteration_number = QLabel("k = 0")
        self.iteration_number.setObjectName("iteration_number")
        self.iteration_number.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        self.iteration_label = QLabel("Iteration Number")
        self.iteration_label.setObjectName("iteration_label")
        self.iteration_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.iteration_details_layout.addStretch(1)
        self.iteration_details_layout.addWidget(self.iteration_number)
        self.iteration_details_layout.addWidget(self.iteration_label)
        self.iteration_details_layout.addStretch(1)

        
        self.certainty_details_layout = QVBoxLayout()
        self.certainty_number = QLabel("1 - 2⁻ᵏ = 0.00")
        self.certainty_number.setObjectName("certainty_number")
        self.certainty_number.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.certainty_label = QLabel("Certainty")
        self.certainty_label.setObjectName("certainty_label")
        self.certainty_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.certainty_details_layout.addStretch(1)
        self.certainty_details_layout.addWidget(self.certainty_number)
        self.certainty_details_layout.addWidget(self.certainty_label)
        self.certainty_details_layout.addStretch(1)

        spacer = QSpacerItem(120, 40, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        self.full_iteration_details_layout.addLayout(self.iteration_details_layout)
        self.full_iteration_details_layout.addSpacerItem(spacer)
        self.full_iteration_details_layout.addLayout(self.certainty_details_layout)


    def updateCertaintyLabel(self, float):
        self.certainty_number.setText(f"1 - 2⁻ᵏ = {float}")


    def updateIterationLabel(self, count):
        self.iteration_number.setText(f"k = {count}")

