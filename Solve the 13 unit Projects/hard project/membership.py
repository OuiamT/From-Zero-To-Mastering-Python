class Member:
    """Represents a member with personal details and membership status."""

    def __init__(self, f_name, l_name, member_id, member_status):
        """
        Initializes a new Member object.

        Parameters
        ----------
        f_name : str
            The member's first name.
        l_name : str
            The member's last name.
        member_id : int or str
            The unique identification number for the member.
        member_status : str
            The current status of the membership (e.g., "Active", "Inactive").
        """
        self.f_name = f_name
        self.l_name = l_name
        self.member_id = member_id
        self.member_status = member_status

    def status_etap(self):
        """
        Checks the current member status and sets it to "Inactive"
        if the status is empty or not explicitly "Active".
        """
        if (self.member_status == "") or (self.member_status != "Active"):
            self.member_status = "Inactive"

    def display_members(self):
        """Prints the member's details (First Name, Last Name, ID, and Status) to the console"""
        print(
            f"""
First Name: {self.f_name}
Last Name: {self.l_name}
MemberShip ID: {self.member_id}
Status: {self.member_status}
-------------------
"""
        )
