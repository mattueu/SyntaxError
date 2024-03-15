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


class DailyTotal:
    """
    Represents the total amount for a day.
    """

    def __init__(self):
        self.date = ""
        self.total_amount = 0.0
        self.transactions = []

    def set_date(self, date: str) -> None:
        """
        Sets the date the lane is rented.
        """
        self.date = date

    def get_total(self) -> float:
        """
        Retrieves the total amount for the day.
        """
        return self.total_amount

    def get_transactions(self) -> list:
        """
        Retrieves the list of transactions for the day.
        """
        return self.transactions


class Transaction:
    """
    Represents a transaction for renting a lane.
    """

    def __init__(self):
        self.date = ""
        self.customer_start_rental = ""
        self.customer_name = ""
        self.lane_number = ""
        self.customer_end_rental = ""

    def set_name(self, name: str) -> None:
        """
        Sets the name of the customer.
        """
        self.customer_name = name

    def set_lane_start_time(self, time: int) -> None:
        """
        Sets the start time for the customer's lane.
        """
        self.customer_start_rental = time

    def get_lane(self) -> int:
        """
        Retrieves the lane number assigned to the customer.
        """
        return self.lane_number

    def get_date(self) -> str:
        """
        Retrieves the date of the transaction.
        """
        return self.date

    def set_lane_end_time(self, time: int) -> None:
        """
        Sets the end time for the customer's lane.
        """
        self.customer_end_rental = time


class Lane:
    """
    Represents a lane for renting.
    """

    def __init__(self):
        self.lane_number = 0
        self.lane_cost = 0.0

    def set_lane_cost(self, amount: float) -> None:
        """
        Sets the hourly rate for the lane.
        """
        self.lane_cost = amount

    def set_lane_number(self, number: int) -> None:
        """
        Assigns the lane number to the customer.
        """
        self.lane_number = number

    def get_lane_start_date(self) -> str:
        """
        Retrieves the start date of the lease of the lane.
        """
        return self.start_date

    def get_lane_cost(self) -> float:
        """
        Retrieves the hourly rate for the lane.
        """
        return self.lane_cost
