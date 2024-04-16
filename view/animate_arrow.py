from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtGui import QPainter, QPen, QColor, QLinearGradient
from PyQt6.QtCore import Qt, QTimer
from fyp.view.base_animation import BaseAnimation
from fyp.view.arrow_widget import ArrowWidget


class AnimateArrow(ArrowWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Initialize animation states
        self._topArrowAnimating = False
        self._bottomArrowAnimating = False
        self._glowPositionTop = 0.0
        self._glowPositionBottom = 1.0  # Start from the opposite end
        self._timer = QTimer(self)
        self._timer.timeout.connect(self._animate)
        self._timer.start(40)  # Adjust the timing for smoother or slower animation
        self._animationDuration = 2000  # Adjust the animation duration as needed
        self._delayBeforeStart = 400  # Adjust the delay before starting the animation

    def _animate(self):
        self.increment = 1 / 62.5
        if self._topArrowAnimating:
            self._glowPositionTop += self.increment
            if self._glowPositionTop > 1.0:
                self._glowPositionTop = 0.0
                self._topArrowAnimating = False  # Stop the animation
                self.startTopArrowAnimation()  # Delay before restart

        if self._bottomArrowAnimating:
            self._glowPositionBottom -= self.increment
            if self._glowPositionBottom < 0.0:
                self._glowPositionBottom = 1.0
                self._bottomArrowAnimating = False  # Stop the animation
                self.startBottomArrowAnimation()  # Delay before restart

        self.update()

    def startTopArrowAnimation(self):
        self._glowPositionTop = 0.0
        self._topArrowAnimating = True

    def stopTopArrowAnimation(self):
        self._topArrowAnimating = False
        self.update()
        

    def startBottomArrowAnimation(self):
        self._glowPositionBottom = 1.0
        self._bottomArrowAnimating = True

    def stopBottomArrowAnimation(self):
        self._bottomArrowAnimating = False
        
    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        if self._topArrowAnimating:
            self._drawAnimatedLineWithArrow(painter, True)
        if self._bottomArrowAnimating:
            self._drawAnimatedLineWithArrow(painter, False)

    def _drawAnimatedLineWithArrow(self, painter, isTopLine):
        line_length = self.width() - 20
        arrow_size = 10
        line_y = self.height() // 3 if isTopLine else 2 * self.height() // 3
        glowPosition = self._glowPositionTop if isTopLine else self._glowPositionBottom

        # Setup for animated glow effect
        gradient = QLinearGradient(0, 0, self.width(), 0)
        if isTopLine:
            gradient.setColorAt(max(0, glowPosition - 0.2), QColor(60, 107, 133))
            gradient.setColorAt(glowPosition, QColor(Qt.GlobalColor.cyan))
            gradient.setColorAt(min(1, glowPosition + 0.2), QColor(60, 107, 133))
        else:
            gradient.setColorAt(max(0, glowPosition - 0.2), QColor(60, 107, 133))
            gradient.setColorAt(glowPosition, QColor(Qt.GlobalColor.cyan))
            gradient.setColorAt(min(1, glowPosition + 0.2), QColor(60, 107, 133))


        painter.setPen(QPen(gradient, 3))
        painter.drawLine(10, line_y, line_length + 10, line_y)

        # Arrow direction adjustments
        arrow_start = line_length + 10 if isTopLine else 10
        arrow_direction = 1 if isTopLine else -1
        painter.drawLine(arrow_start, line_y, arrow_start - arrow_size * arrow_direction, line_y - arrow_size)
        painter.drawLine(arrow_start, line_y, arrow_start - arrow_size * arrow_direction, line_y + arrow_size)
        



