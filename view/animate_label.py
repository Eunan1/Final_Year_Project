from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import QTimer, QObject

from PyQt6.QtWidgets import QLabel, QWidget
from PyQt6.QtCore import QPropertyAnimation, Qt, QPoint

class LabelAnimator(QObject):
    def __init__(self, parent: QWidget, labelText: str, start_x: int, start_y: int, end_x: int, end_y: int):
        super().__init__(parent)
        self.label = QLabel(labelText, parent)
        self.label.setFixedSize(110, 35)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("border: 3px solid #444444; border-radius: 10px; background-color: #222222; color: white; font-size: 20px; font-weight: bold; font-family: Consolas; padding: 2px;")
        
        self.start_pos = QPoint(start_x, start_y)
        self.end_pos = QPoint(end_x, end_y)
        
        self.label.move(self.start_pos)
        self.label.hide()

        self.animation = QPropertyAnimation(self.label, b"pos")
        self.animation.setDuration(2000)
        self.animation.setStartValue(self.start_pos)
        self.animation.setEndValue(self.end_pos)
        
        self.animation.finished.connect(self.prepareRestart)
        self.delayBeforeRestart = 258
        self.shouldRestart = False  # Controls whether the animation restarts after finishing

    def start(self):
        """Start or restart the animation with initial delay."""
        self.shouldRestart = True
        self.prepareAnimation()

    def prepareAnimation(self):
        """Prepares the label and starts the animation after a delay."""
        if self.shouldRestart:  # Only proceed if restart is allowed
            self.label.show()
            self.label.move(self.start_pos.x(), self.start_pos.y())
            QTimer.singleShot(self.delayBeforeRestart, self.animation.start)

    def prepareRestart(self):
        """Prepares to restart the animation once it finishes."""
        # Keep the label visible at the end of its journey
        if self.shouldRestart:
            # The label remains visible, no need to hide it here
            QTimer.singleShot(self.delayBeforeRestart, self.restartAnimation)
        else:
            # If not restarting, then hide the label after the delay
            QTimer.singleShot(self.delayBeforeRestart, self.label.hide)

    def restartAnimation(self):
        """Restarts the animation if allowed."""
        if self.shouldRestart:
            self.prepareAnimation()

    def stop(self):
        """Stops the animation and prevents it from restarting."""
        self.shouldRestart = False
        self.animation.stop()
        # Delay the hiding to simulate the waiting period
        QTimer.singleShot(self.delayBeforeRestart, self.label.hide)

    def setText(self, newText: str):
        """Sets or updates the label's text."""
        self.label.setText(newText)