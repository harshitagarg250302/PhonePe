Objective: Design and implement an application to allow users to choose and book fitness classes. The application should cater to user management, class scheduling, and booking, including waitlisting and cancellation features.
1. User Management

Registration and Login: Users should be able to register and log in to the system.

User Tiers. Users can be categorized into three tiers: Platinum, Gold, and Silver. Each tier has a different booking limit:

Platinum: 10 classes
Gold 5 classes

Silver: 3 classes

2. Packages
3. The user tiers align with the packages, determining the number of classes a user can book.

3. Classes:

Types Classes can include yoga, gym, and dance etc etc.

Capacity: Each class has a maximum number of attendees.

Scheduling Classes are scheduled at specific times, and multiple classes can run in a single day.

4. Booking:

Users can book a class if it has not reached capacity.

An admin can create, schedule, and cancel classes.

Waitlisting if a class is full, users can join a waitlist. When a booked user cancels, the first user on the waitlist is allocated the slot Cancellation. Users can cancel their booking up to 30 minutes before the class starts. Admins can also cancel classes.

Methods: This is just to help you understand. Actual implementation may differ. Unver Management Register/Login, Select Package

Classes (Admin) Create a class, Schedule a class, Cancel a class

Booking (User) Book a class. Cancel a class

Additional Considerations:

1. Users should be able to book classes at different sones
1. 2.Concurrency management for multiple users trying to book the same class simultaneously.
2. Handling package strategies effectively.

3. Ensuring that user cancellations restore their booking quota.
 
Evaluation Criteria:

1. Design:

Use of object-oriented design principles (classes, interfaces, inheritance, polymorphism).

Efficiency and scalability of data structures.

Flexibility and modularity of system components.

Consideration of security and data privacy principles

2. Implementation:

Functionality and accuracy of system features.

Performance and resource optimization of algorithms.

Code readability, maintainability, and adherence to coding standards.

Error handling and exception management for smooth operation.

Expectations:

Provide clean, professional-level code

Model core entities and relationships effectively

Demonstrate the solution with a method-based approach.

Use memory-based object storage, a backend database is not required.

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB