
class old:
    def showEvent(self, event):
        super().showEvent(event)
        self.startAnimation()  # Start the animation once the widget is displayed

    def startAnimation(self):
        self.path_pos = 0.0  # Position along the path
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateAnimation)
        self.timer.start(60)  # Animation update interval

        self.updateAnimationPath()  # Set up the animation path based on current widget positions

    def updateAnimationPath(self):
        # Calculate center points of prover and verifier relative to ZeroKnowledge widget
        prover_center = QPointF(self.prover_label.pos() + self.prover_label.rect().center())
        verifier_center = QPointF(self.verifier_label.pos() + self.verifier_label.rect().center())

        # Artificially extend the arc's width by adding an extra distance
        extra_distance = 350  # Increase this value to extend the arc further
        actual_distance = verifier_center.x() - prover_center.x()
        extended_distance = actual_distance + extra_distance

        # Create the arc path with the extended width
        self.arc_path = QPainterPath()
        self.arc_path.moveTo(prover_center)  # Start from the prover
        arc_height = 75  # Adjust the arc's height if needed
        # The bounding rectangle for the arc is now based on the extended distance
        arc_rect = QRectF(prover_center.x(), prover_center.y() - arc_height,
                        extended_distance, arc_height * 2)
        self.arc_path.arcTo(arc_rect, 180, -180)


    def updateAnimation(self):
        self.path_pos += 0.01  # Speed of the animation
        if self.path_pos > 1.0:
            self.path_pos = 0.0  # Loop the animation

        # Calculate new position on the arc
        point = self.arc_path.pointAtPercent(self.path_pos)
        
        # Update animated label position
        self.animated_label.move(int(point.x() - self.animated_label.width() / 2), 
                                 int(point.y() - self.animated_label.height() / 2))
        














from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPainter, QPen, QColor

class ArrowWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumHeight(40)  # Adjust height to fit two arrows
        self._glowIntensity = 0  # Intensity of the glow effect
        self._timer = QTimer(self)  # Timer for updating the glow effect
        self._timer.timeout.connect(self._updateGlow)
        self._glowEnabled = False  # Controls whether the glow effect is applied

    def _updateGlow(self):
        if self._glowEnabled:
            self._glowIntensity = (self._glowIntensity + 10) % 255
        else:
            self._glowIntensity = 0
        self.update()  # Trigger repaint

    def startTopArrowGlow(self):
        self._glowEnabled = True
        self._timer.start(150)  # Adjust for smoother animation

    def stopGlowEffect(self):
        self._glowEnabled = False
        self._timer.stop()
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Common settings for both arrows
        line_length = self.width() - 20
        arrow_size = 10
        top_line_y = (self.height() // 3)
        bottom_line_y = (2 * self.height() // 3)

        # Glow effect for top arrow
        if self._glowEnabled:
            color = QColor(255, 165, 0, self._glowIntensity)  # Orange with variable intensity
        else:
            color = QColor(128, 128, 128)  # Using RGB values for gray
        painter.setPen(QPen(color, 2))

        # Drawing the top arrow (with potential glow effect)
        painter.drawLine(0, top_line_y, line_length, top_line_y)
        painter.drawLine(line_length, top_line_y, line_length - arrow_size, top_line_y - arrow_size)
        painter.drawLine(line_length, top_line_y, line_length - arrow_size, top_line_y + arrow_size)

        # Drawing the bottom arrow (always without glow effect)
        painter.setPen(QPen(QColor(128, 128, 128), 2))
        painter.drawLine(20, bottom_line_y, self.width(), bottom_line_y)
        painter.drawLine(20, bottom_line_y, 20 + arrow_size, bottom_line_y - arrow_size)
        painter.drawLine(20, bottom_line_y, 20 + arrow_size, bottom_line_y + arrow_size)