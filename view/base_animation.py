class BaseAnimation:
    def __init__(self, widget):
        self.widget = widget  # The widget that the animation will be applied to

    def start(self):
        """Start the animation."""
        raise NotImplementedError("The start method must be implemented by subclasses.")

    def stop(self):
        """Stop the animation."""
        raise NotImplementedError("The stop method must be implemented by subclasses.")
