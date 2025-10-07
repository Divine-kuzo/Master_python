class school:
    def __init__(self, name, admin):
        self.name = name 
        self.admin = admin

    def add(self, x, y):
        return x+y, {self.name}

    def div(self, x, y):
        return x/y, {self.name}

    def sub(self, x, y):
        return x-y,{self.admin.phone_number}

    def multi(self, x, y):
        return x*y, {self.admin.phone_number}


class admin:
    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number

admin1 = admin("louis", "lo@gmail.com", "0782438038")
school1 = school("CMU", admin1)

# print(school1.admin.email)

print(school1.add(2,4))
print(school1.sub(3, 60))
print(school1.div(40,5))
print(school1.multi(3,6))