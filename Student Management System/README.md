# 🎓 Student Management System

A simple, menu-driven **Student Management System** built in Python. It allows you to add, view, update, and delete student records — including academic and guardian details — with persistent storage using JSON.

This project is part of my **[Python-Projects](https://github.com/CodewithAwais05/Python-Projects)** repository.

---

## 📌 Features

- ➕ **Add Student** — Store personal, academic, and guardian information
- 📋 **View All Students** — Display all records in a clean, formatted layout
- 🔍 **View Student by ID** — Look up a specific student's full profile
- ✏️ **Update Student** — Edit name, contact, email, address, guardian info, or enrolled subjects
- 🗑️ **Delete Student** — Remove a student record by ID
- 💾 **Persistent Storage** — All data is saved to and loaded from a local `students.json` file, so records persist between runs

---

## 🗂️ Student Data Structure

Each student record is organized into three groups:

| Category            | Fields |
|----------------------|--------|
| **Student Info**      | Name, Student ID, DOB, Gender, Contact No, Email, Address, Class & Section |
| **Academic Details**  | Admission Date, Roll No, Subjects Enrolled |
| **Guardian Info**     | Guardian Name, Guardian Contact No, Guardian Email, Emergency Contact |

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Data Storage:** JSON (`students.json`)
- **Concepts Used:** Object-Oriented Programming (OOP), File Handling, CRUD Operations

---

## 📂 Project Structure

```
Student Management System/
│
├── student_management.py     # Main application file
├── students.json              # Auto-generated data file (created on first run)
├── Screenshots/               # Output screenshots
└── README.md                   # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your system

### Installation & Run

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/Python-Projects.git
   ```
2. Navigate to the project folder:
   ```bash
   cd "Python Projects/Student Management System"
   ```
3. Run the script:
   ```bash
   python student_management.py
   ```

---

## 🖥️ Usage

On running the program, you'll see a menu like this:

```
=============================================
      STUDENT MANAGEMENT SYSTEM
=============================================
  1. Add Student
  2. View All Students
  3. View Student by ID
  4. Delete Student
  5. Update Student
  6. Exit
=============================================
```

Simply enter the number corresponding to the action you want to perform, and follow the prompts.

---

## 📸 Screenshots

Screenshots of the program's output are available in the [`Screenshots`](./Screenshots) folder, including:

- Main menu
- Adding a new student
- Viewing all students
- Updating student details
- Deleting a student

---

## 💡 Future Improvements

- [ ] Input validation (e.g., email format, phone number length)
- [ ] Search students by name or class/section
- [ ] Export student records to CSV/PDF
- [ ] Attendance and fee tracking modules
- [ ] GUI version using Tkinter
- [ ] Migrate storage from JSON to SQLite database

---

## 👤 Author

**Awais**
Feel free to connect or reach out with feedback and suggestions!

---

## 📄 License

This project is open-source and available under the [MIT License](../LICENSE).
