from constants import package_class_mapping

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
        # Logic to register the user
        pass

    def login(self):
        # Logic to log the user in
        pass
