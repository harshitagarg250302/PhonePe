from app_constant import package_class_mapping
class User:
    users_list ={}
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
        # Logic to register the user
        if not User.users_list.get(self.username): User.users_list[self.username]= self;
        else:
            return "User already exists"
        return "User registered successfully."

    def login(self):
        if self.username not in User.users_list:
            return "Username does not exist."
        if User.users_list[self.username].password != self.password:
            return "Incorrect password."
        return "User logged in successfully."
