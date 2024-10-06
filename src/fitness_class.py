from datetime import datetime, timedelta

class FitnessClass:
    def __init__(self, class_name, class_type, capacity, time):
        self.class_name = class_name
        self.class_type = class_type  # yoga, gym, etc.
        self.capacity = capacity
        self.time = time  # class time
        self.attendees = []
        self.waitlist = []

    def is_full(self):
        return len(self.attendees) >= self.capacity

    def add_to_waitlist(self, user):
        self.waitlist.append(user)
    
    def remove_from_waitlist(self, user):
        del[self.waitlist[0]]

    def cancel_class(self, admin):
        # Admin cancels the class and notifies users
        pass
