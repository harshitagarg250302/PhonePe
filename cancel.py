from datetime import datetime, timedelta
def cancel_booking(self, user, class_name):
        if class_name in self.classes:
            fitness_class = self.classes[class_name]
            current_time = datetime.now()
            if fitness_class.time - current_time < timedelta(minutes=30):
                return "Cannot cancel booking less than 30 minutes before the class starts."

            if user in fitness_class.attendees:
                fitness_class.attendees.remove(user)
                user.booked_classes -= 1

                # If there are users on the waitlist, promote the first one
                if fitness_class.waitlist:
                    next_user = fitness_class.waitlist.pop(0)
                    fitness_class.attendees.append(next_user)
                    next_user.booked_classes += 1

                return f"Booking canceled for {class_name}."
            elif user in fitness_class.waitlist:
                fitness_class.remove_from_waitlist(user)
                return f"Removed from waitlist for {class_name}."
        return "No booking or waitlist entry found to cancel."
