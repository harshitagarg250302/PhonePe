from src.fitness_class import FitnessClass


class BookingSystem:
    def __init__(self):
        self.classes = {}  # Stores classes with a unique identifier

    def create_class(self, class_name, class_type, capacity, time, admin):
        new_class = FitnessClass(class_name, class_type, capacity, time)
        self.classes[class_name] = new_class
        return f"Class {class_name} created."

    def book_class(self, user, class_name):
        if class_name not in self.classes:
            return "Class not found."
        
        fitness_class = self.classes[class_name]

        if fitness_class.is_full():
            if user not in fitness_class.waitlist:
                fitness_class.add_to_waitlist(user)
                return "Class is full. You have been added to the waitlist."
            else:
                return "You are already on the waitlist."
        
        if user.can_book_class():
            fitness_class.attendees.append(user)
            user.booked_classes += 1
            return f"Booking successful for {class_name}."
        else:
            return "Booking limit reached for your tier."

    def cancel_booking(self, user, class_name):
        if class_name in self.classes:
            fitness_class = self.classes[class_name]
            if user in fitness_class.attendees:
                fitness_class.attendees.remove(user)
                user.booked_classes -= 1

                # If there are users on the waitlist, promote the first one
                if fitness_class.waitlist:
                    next_user = fitness_class.waitlist.pop(0)
                    fitness_class.attendees.append(next_user)
                    next_user.booked_classes += 1

                return f"Booking canceled for {class_name}."
        return "No booking found to cancel."

    def cancel_class(self, class_name, admin):
        if class_name in self.classes:
            del self.classes[class_name]
            # Notify all attendees and waitlist users
            return f"Class {class_name} has been canceled by the admin."
        return "Class not found."
