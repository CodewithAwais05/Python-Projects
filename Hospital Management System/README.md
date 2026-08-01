# Hospital Management System

A simple command-line Hospital Management System written in Python. It lets you manage patients, doctors, and appointments through an interactive text-based menu, with data persisted to local JSON files.

## Features

### Patient Management
- Add a new patient (ID, name, age, gender, address, phone, blood group, disease)
- View all patients
- Update a patient's address, phone, or disease
- Delete a patient
- Search for a patient by ID

### Doctor Management
- Add a new doctor (ID, name, specialization, phone, email, experience)
- View all doctors
- Update a doctor's phone, email, or experience
- Delete a doctor
- Search for a doctor by ID

### Appointment Management
- Book an appointment (links an existing patient ID and doctor ID with a date and time)
- View all appointments
- Cancel an appointment

## How It Works

The program keeps three in-memory dictionaries — `patient_data`, `doctor_data`, and `appointment_data` — that are loaded from (and saved back to) JSON files on disk:

| Data | File |
|---|---|
| Patients | `patient_data.json` |
| Doctors | `doctor_data.json` |
| Appointments | `appointment_data.json` |

If a data file doesn't exist yet, the program starts with an empty data set for that category and creates the file the first time you add a record.

Each entity (`Patient`, `Doctor`, `Appointment`) is implemented as its own class with methods to add, view, update, delete/cancel, and (for patients/doctors) search records. Every change is immediately saved to its corresponding JSON file.

## Requirements

- Python 3.x (no external dependencies — uses only the built-in `json` and `os` modules)

## Usage

1. Save the script (e.g. as `hospital_management_system.py`).
2. Run it from the command line:
   ```bash
   python hospital_management_system.py
   ```
3. Follow the on-screen menu:
   ```
   1. Patient Management
   2. Doctor Management
   3. Appointment Management
   4. Exit
   ```
4. Navigate into a submenu (e.g. Patient Management) and choose an action such as Add, View, Update, Delete, or Search.

### Example: Adding a Patient
```
1. Patient Management
  -> 1. Add Patient
     Enter patient ID: P001
     Enter patient name: John Doe
     Enter patient age: 34
     Enter patient gender: Male
     Enter patient address: 123 Main St
     Enter patient phone: 555-1234
     Enter patient blood group: O+
     Enter patient disease: Flu
```

### Example: Booking an Appointment
```
3. Appointment Management
  -> 1. Book Appointment
     Enter appointment ID: A001
     Enter patient ID: P001   (must already exist)
     Enter doctor ID: D001    (must already exist)
     Enter appointment date (YYYY-MM-DD): 2026-08-15
     Enter appointment time (HH:MM): 10:30
```

## Notes & Limitations

- IDs (patient, doctor, appointment) are treated as unique keys — duplicates are rejected.
- Booking an appointment requires the referenced patient ID and doctor ID to already exist in `patient_data.json` and `doctor_data.json`.
- Input validation is minimal (e.g. age must be entered as a valid integer); invalid menu choices simply print an "Invalid choice." message and let you try again.
- Data files are plain JSON and are read/written locally — there is no database or network component, so this is best suited for learning, prototyping, or single-user local use.

## Project Structure

```
.
├── hospital_management_system.py   # Main application script
├── patient_data.json               # Auto-generated patient records
├── doctor_data.json                # Auto-generated doctor records
└── appointment_data.json           # Auto-generated appointment records
```