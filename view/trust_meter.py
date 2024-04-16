from PyQt6.QtWidgets import QProgressBar, QVBoxLayout, QWidget, QSizePolicy
from PyQt6.QtCore import QPropertyAnimation, pyqtProperty


class TrustMeter(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        self.progress_bar = QProgressBar()
        self.progress_bar.setFixedHeight(50)
        self.progress_bar.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.progress_bar.setValue(0)
        self.progress_bar.setObjectName("progress_bar")
        layout.addWidget(self.progress_bar)
        self.progress_bar.setMaximum(100)  # Max value is 100%

        self.animation = QPropertyAnimation(self, b"progressValue", self)
        self.animation.setDuration(1000)


    @pyqtProperty(int)
    def progressValue(self):
        return self.progress_bar.value()

    @progressValue.setter
    def progressValue(self, value):
        self.progress_bar.setValue(value)

    def updateTrustLevel(self, trustPercentage):
        # Start animation from current value to new value
        inverted_trust_percentage = 100 - trustPercentage
        self.animation.setStartValue(self.progress_bar.value())
        self.animation.setEndValue(inverted_trust_percentage)
        self.animation.start()

