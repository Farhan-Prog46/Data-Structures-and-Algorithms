# Completed by: Syed Farhan Zaheer Hussainy – Group #5
# Question 2: Hash Table – Student Records

class StudentRecords:
    def __init__(self):
        # Hash table using Python dictionary
        self.records = {
            101: {"name": "Alice", "gpa": 3.6},
            102: {"name": "Sara", "gpa": 2.5},
            103: {"name": "John", "gpa": 3.0}
        }

    # Insert a new student
    def insert(self, student_id, name, gpa):
        if student_id in self.records:
            print("Error: Student ID already exists.\n")
        else:
            self.records[student_id] = {"name": name, "gpa": gpa}
            print(f"Student '{name}' added successfully.\n")

    # Retrieve a student record
    def retrieve(self, student_id):
        if student_id in self.records:
            student = self.records[student_id]
            print("Student Record Found:")
            print(f"ID   : {student_id}")
            print(f"Name : {student['name']}")
            print(f"GPA  : {student['gpa']}\n")
        else:
            print("Error: Student record not found.\n")

    # Delete a student record
    def delete(self, student_id):
        if student_id in self.records:
            deleted_student = self.records.pop(student_id)
            print(f"Student '{deleted_student['name']}' deleted successfully.\n")
        else:
            print("Error: Student record not found.\n")

    # Display all student records
    def display_all(self):
        print("====== ALL STUDENT RECORDS ======")
        print("{:<10} {:<15} {:<5}".format("ID", "Name", "GPA"))
        print("-" * 35)
        for student_id, info in self.records.items():
            print("{:<10} {:<15} {:<5}".format(student_id, info["name"], info["gpa"]))
        print()


# Main program
def main():
    system = StudentRecords()

    print("Initial Records:")
    system.display_all()

    print("Inserting a new student:")
    system.insert(104, "Farhan", 2.8)

    print("Retrieving student with ID 101:")
    system.retrieve(101)

    print("Deleting student with ID 102:")
    system.delete(102)

    print("Final Records:")
    system.display_all()


if __name__ == "__main__":
    main()