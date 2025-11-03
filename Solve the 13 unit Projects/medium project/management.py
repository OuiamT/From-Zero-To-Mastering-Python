class Management:
    
    def __init__(self, first_n, last_n, email, password, status = "inactive"):
        self.first_n = first_n
        self.last_n = last_n
        self.email = email
        self.password = password
        self.status = status
    
    def display_inf(self):
        print(f"""
First name : {self.first_n}
Last name : {self.last_n}
Email : {self.email}
Status : {self.status}
----------------------
""")