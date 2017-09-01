import traceback

class GameCall(Exception):
    """Game call raise message"""
    def isError(self):
        return False

class IntCall(GameCall):
    def __init__(self):
        super(IntCall, self).__init__("Interruption request")

class SkipCall(GameCall):
    def __init__(self):
        super(SkipCall, self).__init__("Skipping frame")

class GameError(GameCall):
    def __init__(self, error):
        super(GameError, self).__init__("An error occured")
        self.error = error

    def isError(self):
        return True

    def printStackTrace(self):
        traceback.print_exc()

