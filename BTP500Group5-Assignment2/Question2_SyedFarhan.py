# Completed by: Farhan Zaheer Hussainy – Group #[Your Group Number]
# Question 2: Hash Table – Student Records

class StudentRecords:
    def __init__(self):
        # Preloaded students (hash table using dictionary)
        self.records = {
            101: {"name": "Alice", "gpa": 3.6},
            102: {"name": "Sara", "gpa": 2.5},
            103: {"name": "John", "gpa": 3.0}
        }

    # Insert a new student
    def insert(self, student_id, name, gpa):
        if student_id in self.records:
            print("Error: Student ID already exists.\n")
            return
        self.records[student_id] = {"name": name, "gpa": gpa}
        print(f"Student '{name}' added successfully.\n")

    # Retrieve a student
    def retrieve(self, student_id):
        if student_id in self.records:
            student = self.records[student_id]
            print("\n--- Student Found ---")
            print(f"ID   : {student_id}")
            print(f"Name : {student['name']}")
            print(f"GPA  : {student['gpa']}\n")
        else:
            print("Error: Student record not found.\n")

    # Delete a student
    def delete(self, student_id):
        if student_id in self.records:
            deleted = self.records.pop(student_id)
            print(f"Student '{deleted['name']}' deleted successfully.\n")
        else:
            print("Error: Student record not found.\n")

    # Display all students
    def display_all(self):
        if not self.records:
            print("No student records available.\n")
        else:
            print("\n====== ALL STUDENT RECORDS ======")
            print("{:<10} {:<15} {:<5}".format("ID", "Name", "GPA"))
            print("-" * 35)
            for sid, info in self.records.items():
                print("{:<10} {:<15} {:<5}".format(sid, info["name"], info["gpa"]))
            print()


# -------- MAIN PROGRAM --------
def main():
    system = StudentRecords()

    

    while True:
        print("===== Student Record System =====")
        print("1. Insert Student")
        print("2. Retrieve Student")
        print("3. Delete Student")
        print("4. Display All Students")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        # INSERT
        if choice == "1":
            try:
                sid = int(input("Enter Student ID: "))
                name = input("Enter Name: ")
                gpa = float(input("Enter GPA (0-4): "))

                if gpa < 0 or gpa > 4:
                    print("Error: GPA must be between 0 and 4.\n")
                    continue

                system.insert(sid, name, gpa)

            except ValueError:
                print("Error: Invalid input type.\n")

        # RETRIEVE
        elif choice == "2":
            try:
                sid = int(input("Enter Student ID to retrieve: "))
                system.retrieve(sid)
            except ValueError:
                print("Error: Invalid ID.\n")

        # DELETE
        elif choice == "3":
            try:
                sid = int(input("Enter Student ID to delete: "))
                system.delete(sid)
            except ValueError:
                print("Error: Invalid ID.\n")

        # DISPLAY
        elif choice == "4":
            system.display_all()

        # EXIT
        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.\n")


# Run program
if __name__ == "__main__":
    main()