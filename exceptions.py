class Impossible(Exception):
    """Exception raised when action is impossible to preform

    the reason is given as the exception message.
    """


class QuitWithoutSaving(SystemExit):
    """Can be raised to exit the game withoug automatically saving."""
