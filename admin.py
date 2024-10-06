from src.user_management import User
from src.fitness_class import FitnessClass

class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password, 'Admin')

    def create_class(self, class_name, class_type, capacity, time):
        if class_name in FitnessClass.classes:
            return "Class already exists."
        new_class = FitnessClass(class_name, class_type, capacity, time)
        FitnessClass.classes[class_name] = new_class
        return f"Class {class_name} created successfully."

    def schedule_class(self, class_name, time):
        if class_name not in FitnessClass.classes:
            return "Class does not exist."
        FitnessClass.classes[class_name].time = time
        return f"Class {class_name} scheduled successfully."

    def cancel_class(self, class_name):
        if class_name not in FitnessClass.classes:
            return "Class does not exist."
        del FitnessClass.classes[class_name]
        return f"Class {class_name} cancelled successfully."
