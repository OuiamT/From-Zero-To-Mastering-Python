class Member:
    def __init__(self, f_name, l_name, member_id, member_status):
        self.f_name = f_name
        self.l_name = l_name
        self.member_id = member_id
        self.member_status = member_status

    def status_etap(self):
        if (self.member_status == "") or (self.member_status != "Active"):
            self.member_status = "Inactive"

    def display_members(self):
        print(f"""
First Name: {self.f_name}
Last Name: {self.l_name}
MemberShip ID: {self.member_id}
Status: {self.member_status}
-------------------
""")