import json

class Student:

    def __init__(self):
        self.student = {}
        self.academic = {}
        self.guardian = {}

    def student_info(self, name="", student_id=None, dob="", gender="", contact_no=None, email="", address="", class_section=""):
        self.student = {
            "name": name,
            "student_id": student_id,
            "dob": dob,
            "gender": gender,
            "contact_no": contact_no,
            "email": email,
            "address": address,
            "class_section": class_section
        }

    def academic_details(self, admission_date="", roll_no=None, subjects_enrolled=None):
        self.academic = {
            "admission_date": admission_date,
            "roll_no": roll_no,
            "subjects_enrolled": subjects_enrolled
        }

    def guardian_info(self, guardian_name="", guardian_contact_no=None, guardian_email="", emergency_contact=None):
        self.guardian = {
            "guardian_name": guardian_name,
            "guardian_contact_no": guardian_contact_no,
            "guardian_email": guardian_email,
            "emergency_contact": emergency_contact
        }

    def to_dict(self):
        return {
            "student": self.student,
            "academic": self.academic,
            "guardian": self.guardian
        }


class StudentManager:

    def __init__(self):
        self.students = []

    # ---------- helper for formatting ----------
    def print_header(self, text, symbol="=", width=45):
        print(symbol * width)
        print(text.center(width))
        print(symbol * width)

    def print_section(self, title):
        print(f"\n--- {title} ---")

    def print_field(self, label, value):
        print(f"  {label:<20}: {value}")

    # ---------- core methods ----------
    def add_student(self):
        self.print_header("ADD NEW STUDENT")

        s = Student()
        s.student_info(
            name=input("Name: "),
            student_id=input("ID: "),
            dob=input("DOB: "),
            gender=input("Gender: "),
            contact_no=input("Contact No: "),
            email=input("Email: "),
            address=input("Address: "),
            class_section=input("Class & Section: ")
        )
        s.academic_details(
            admission_date=input("Admission Date: "),
            roll_no=input("Roll No: "),
            subjects_enrolled=[subj.strip() for subj in input("Subjects (comma separated): ").split(",")]
        )
        s.guardian_info(
            guardian_name=input("Guardian Name: "),
            guardian_contact_no=input("Guardian Contact: "),
            guardian_email=input("Guardian Email: "),
            emergency_contact=input("Emergency Contact: ")
        )
        self.students.append(s)
        self.save_to_file()
        print("\n✅ Student added successfully!")

    def save_to_file(self, filename="students.json"):
        data = [s.to_dict() for s in self.students]
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    def load_from_file(self, filename="students.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)

            self.students = []
            for entry in data:
                s = Student()
                s.student = entry["student"]
                s.academic = entry["academic"]
                s.guardian = entry["guardian"]
                self.students.append(s)

            print(f"📂 {len(self.students)} student record(s) loaded successfully!")
        except FileNotFoundError:
            print("⚠️  No saved file found. Starting fresh.")

    def display_student(self, s, index=None):
        title = f"Student {index}" if index else "Student Record"
        self.print_header(title, symbol="-")

        self.print_section("Student Info")
        for key, value in s.student.items():
            self.print_field(key, value)

        self.print_section("Academic Details")
        for key, value in s.academic.items():
            self.print_field(key, value)

        self.print_section("Guardian Info")
        for key, value in s.guardian.items():
            self.print_field(key, value)

    def view_all_students(self):
        if not self.students:
            print("\n⚠️  No students to show.")
            return

        self.print_header(f"ALL STUDENTS ({len(self.students)})")
        for idx, s in enumerate(self.students, start=1):
            self.display_student(s, idx)
        print("=" * 45)

    def view_student_by_id(self, student_id):
        for s in self.students:
            if s.student.get("student_id") == student_id:
                self.display_student(s)
                print("-" * 45)
                return
        print(f"\n❌ Student with ID '{student_id}' not found.")

    def delete_student(self, student_id):
        for s in self.students:
            if s.student.get("student_id") == student_id:
                self.students.remove(s)
                self.save_to_file()
                print(f"\n🗑️  Student '{s.student.get('name')}' deleted successfully!")
                return
        print(f"\n❌ Student with ID '{student_id}' not found.")

    def update_student(self, student_id):
        for s in self.students:
            if s.student.get("student_id") == student_id:

                self.print_header("UPDATE STUDENT", symbol="-")
                print("1. Update Name")
                print("2. Update Contact")
                print("3. Update Email")
                print("4. Update Address")
                print("5. Update Guardian")
                print("6. Update Subjects")
                print("-" * 45)

                choice = input("Enter option: ")

                if choice == "1":
                    s.student["name"] = input("Enter new name: ")

                elif choice == "2":
                    s.student["contact_no"] = input("Enter new contact number: ")

                elif choice == "3":
                    s.student["email"] = input("Enter new email: ")

                elif choice == "4":
                    s.student["address"] = input("Enter new address: ")

                elif choice == "5":
                    self.print_section("Guardian Information Update")
                    s.guardian["guardian_name"] = input("Guardian Name: ")
                    s.guardian["guardian_contact_no"] = input("Guardian Contact: ")
                    s.guardian["guardian_email"] = input("Guardian Email: ")
                    s.guardian["emergency_contact"] = input("Emergency Contact: ")

                elif choice == "6":
                    subjects = input("Enter subjects separated by comma: ")
                    s.academic["subjects_enrolled"] = [subj.strip() for subj in subjects.split(",")]

                else:
                    print("\n❌ Invalid option!")
                    return

                self.save_to_file()
                print("\n✅ Student updated successfully!")
                return

        print(f"\n❌ Student with ID '{student_id}' not found.")


def print_menu():
    print("\n" + "=" * 45)
    print("      STUDENT MANAGEMENT SYSTEM".center(45))
    print("=" * 45)
    print("  1. Add Student")
    print("  2. View All Students")
    print("  3. View Student by ID")
    print("  4. Delete Student")
    print("  5. Update Student")
    print("  6. Exit")
    print("=" * 45)

manager = StudentManager()
manager.load_from_file()
while True:
    print_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        manager.add_student()
    elif choice == "2":
        manager.view_all_students()
    elif choice == "3":
        sid = input("Enter Student ID: ")
        manager.view_student_by_id(sid)
    elif choice == "4":
        sid = input("Enter Student ID to delete: ")
        manager.delete_student(sid)
    elif choice == "5":
        sid = input("Enter Student ID to update: ")
        manager.update_student(sid)
    elif choice == "6":
        print("\n👋 Exiting... Goodbye!")
        break
    else:
        print("\n❌ Invalid choice, try again.")


