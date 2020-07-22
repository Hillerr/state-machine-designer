class InitialStateError(Exception):
    """Exception raised for errors in the initial state

    Attributes:
        message (str): The message that will be printed 
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class LastStateError(Exception):
    """Exception raised for errors in the last state

    Attributes:
        message (str): The message that will be printed 
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class CurrentStateError(Exception):
    """Exception raised for errors in the current state

    Attributes:
        message (str): The message that will be printed 
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)