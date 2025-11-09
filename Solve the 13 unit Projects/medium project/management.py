class Management:
    """
    A class to represent a user management system.

    Attributes:
        first_n (str): The user's first name.
        last_n (str): The user's last name.
        email (str): The user's email address.
        password (str): The user's password.
        status (str): The user's account status (default is "inactive").

    Methods:
        display_inf():
            Displays the user's information in a formatted output.
    """

    def __init__(self, first_n, last_n, email, password, status="inactive"):
        self.first_n = first_n
        self.last_n = last_n
        self.email = email
        self.password = password
        self.status = status

    def display_inf(self):
        print(
            f"""
First name : {self.first_n}
Last name : {self.last_n}
Email : {self.email}
Status : {self.status}
----------------------
"""
        )
