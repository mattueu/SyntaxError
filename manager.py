class Manager:
    """
    Represents a manager with a name and password.
    """

    def __init__(self):
        self.name_of_owner = ""
        self.password_ = ""

    def set_name(self, name: str) -> None:
        """
        Sets the name of the manager.
        """
        self.name_of_owner = name

    def set_password(self, password: str) -> None:
        """
        Sets the password of the manager.
        """
        self.password_ = password