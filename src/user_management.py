# Assuming we have a global dictionary to store users
users_db = {}

class User:
    def __init__(self, username, password, package):
        self.username = username
        self.password = password
        self.package = package
        self.booked_classes = 0
        self.max_classes = self.set_max_classes()

    def set_max_classes(self):
        if self.package == 'Platinum':
            return package_class_mapping.get('Platinum')
        elif self.package == 'Gold':
            return package_class_mapping.get('Gold')
        elif self.package == 'Silver':
            return package_class_mapping.get('Silver')
        return 0

    def can_book_class(self):
        return self.booked_classes < self.max_classes

    def register(self):
        if self.username in users_db:
            return "Username already exists."
        users_db[self.username] = self
        return "User registered successfully."

    def login(self):
        if self.username not in users_db:
            return "Username does not exist."
        if users_db[self.username].password != self.password:
            return "Incorrect password."
        return "User logged in successfully."