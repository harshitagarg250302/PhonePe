from datetime import datetime, time
from src.user_management import User
from src.booking import BookingSystem
if __name__ == "__main__":
    # Creating users
    user1 = User("john_doe", "password123", "Platinum")
    user2 = User("jane_doe", "password456", "Gold")

    # Admin creates classes
    system = BookingSystem()
    admin = "admin"

    print(system.create_class("Yoga", "Yoga", 2, datetime.now() + timedelta(days=1), admin))
    
    # User books a class
    print(system.book_class(user1, "Yoga"))
    print(system.book_class(user2, "Yoga"))
    
    # User1 cancels and waitlist is processed
    print(system.cancel_booking(user1, "Yoga"))
