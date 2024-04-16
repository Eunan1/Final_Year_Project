from PyQt6.QtWidgets import QGraphicsOpacityEffect
from PyQt6.QtCore import QPropertyAnimation

def applyFadeEffect(widget, start_value=0, end_value=1, duration=1000):
    """
    Apply a fade effect to a widget.
    
    Parameters:
    - widget: The widget to apply the fade effect to.
    - start_value: The starting opacity value (0 is fully transparent, 1 is fully opaque).
    - end_value: The ending opacity value.
    - duration: The duration of the fade effect in milliseconds.
    """
    # Check if the widget already has an opacity effect applied
    if not isinstance(widget.graphicsEffect(), QGraphicsOpacityEffect):
        opacity_effect = QGraphicsOpacityEffect(widget)
        widget.setGraphicsEffect(opacity_effect)
    else:
        opacity_effect = widget.graphicsEffect()

    animation = QPropertyAnimation(opacity_effect, b"opacity")
    animation.setDuration(duration)
    animation.setStartValue(start_value)
    animation.setEndValue(end_value)
    animation.start()

    # Optional: return the animation if you need to keep a reference to it or connect signals
    return animation