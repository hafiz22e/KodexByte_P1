class Student:
    def __init__(self, name, m1, m2, m3):
        self.name = name
        self.marks = [m1, m2, m3]

    # Display student details
    def display(self):
        print("\n--- Student Details ---")
        print("Name:", self.name)
        print("Marks:", self.marks)

    # Calculate average
    def calculate_average(self):
        avg = sum(self.marks) / len(self.marks)
        print("Average Marks:", avg)


# ---- Main Program ----

# Input from user
name = input("Enter student name: ")
m1 = float(input("Enter marks of subject 1: "))
m2 = float(input("Enter marks of subject 2: "))
m3 = float(input("Enter marks of subject 3: "))

# Create object
student1 = Student(name, m1, m2, m3)

# Display details
student1.display()

# Show average
student1.calculate_average()
