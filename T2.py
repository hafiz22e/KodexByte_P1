class Student:
    # 1. The Constructor (__init__)
    # This sets up the student's data as soon as the object is created.
    def __init__(self, name, mark1, mark2, mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
        print(f"Student record created for: {self.name}")

    # 2. Method to display the student's details
    def display_info(self):
        print("\n--- Student Details ---")
        print(f"Name: {self.name}")
        print(f"Subject 1: {self.mark1}")
        print(f"Subject 2: {self.mark2}")
        print(f"Subject 3: {self.mark3}")

    # 3. Method to calculate and display the average
    def display_average(self):
        # Calculate the average by adding the marks and dividing by 3
        average = (self.mark1 + self.mark2 + self.mark3) / 3
        
        # Display the result, formatted to 2 decimal places
        print(f"\nAverage Marks for {self.name}: {average:.2f}")


# Create a student object
student_one = Student(name="Hamza", mark1=85.0, mark2=92.5, mark3=78.0)

# Call the methods to see the output
student_one.display_info()
student_one.display_average()

print("\n---------------------------")

# You can easily create a second student without rewriting the logic!
student_two = Student(name="Hamza Ishaq", mark1=60.0, mark2=75.0, mark3=80.0)
student_two.display_info()
student_two.display_average()
