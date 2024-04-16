from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QPen
from PyQt6.QtCore import Qt

class ArrowWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumHeight(80)
        self._glowEnabled = False  # Tracks whether the glow effect is enable

    def toggleGlowEffect(self):
        self._glowEnabled = not self._glowEnabled
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        line_length = self.width() - 20
        top_line_y = self.height() // 3
        bottom_line_y = 2 * self.height() // 3
        arrow_size = 10  # Size of the arrowhead

        # Draw top line with arrowhead pointing to the right
        self._drawTopLineWithArrow(painter, top_line_y, line_length, arrow_size)
        
        # Draw bottom line with arrowhead pointing to the left
        self._drawBottomLineWithArrow(painter, bottom_line_y, line_length, arrow_size)

    def _drawTopLineWithArrow(self, painter, line_y, line_length, arrow_size):
        # Set pen for the line and arrowhead
        painter.setPen(QPen(Qt.GlobalColor.lightGray, 3))
        
        # Draw the line
        painter.drawLine(10, line_y, line_length + 10, line_y)
        
        # Draw the arrowhead pointing to the right
        arrow_start = line_length + 10
        painter.drawLine(arrow_start, line_y, arrow_start - arrow_size, line_y - arrow_size)
        painter.drawLine(arrow_start, line_y, arrow_start - arrow_size, line_y + arrow_size)

    def _drawBottomLineWithArrow(self, painter, line_y, line_length, arrow_size):
        # Set pen for the line and arrowhead
        painter.setPen(QPen(Qt.GlobalColor.lightGray, 3))
        
        # Draw the line
        painter.drawLine(10, line_y, line_length + 10, line_y)
        
        # Draw the arrowhead pointing to the left
        arrow_start = 10  # Starting point for the left-pointing arrow
        painter.drawLine(arrow_start, line_y, arrow_start + arrow_size, line_y - arrow_size)
        painter.drawLine(arrow_start, line_y, arrow_start + arrow_size, line_y + arrow_size)


