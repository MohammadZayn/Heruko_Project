class ElementNotFoundException(Exception):
    def __init__(self, message="Element not found"):
        self.message = message
        super().__init__(self.message)