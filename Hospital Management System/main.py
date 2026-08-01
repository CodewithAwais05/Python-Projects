import json
import os

PATIENT_DATA_FILE = "patient_data.json"
DOCTOR_DATA_FILE = "doctor_data.json"
APPOINTMENT_DATA_FILE = "appointment_data.json"

if os.path.exists(PATIENT_DATA_FILE):
    with open(PATIENT_DATA_FILE, 'r') as file:
        patient_data = json.load(file)
else:
    patient_data = {}
if os.path.exists(DOCTOR_DATA_FILE):
    with open(DOCTOR_DATA_FILE, 'r') as file:
        doctor_data = json.load(file)
else:
    doctor_data = {}
if os.path.exists(APPOINTMENT_DATA_FILE):
    with open(APPOINTMENT_DATA_FILE, 'r') as file:
        appointment_data = json.load(file)
else:
    appointment_data = {}


# =====================================================
#                    PATIENT CLASS:                    
# =====================================================

class Patient:
    def __init__(self):
        self.patient_id = ""
        self.patient_name = ""
        self.patient_age = 0
        self.patient_gender = ""
        self.patient_address = ""
        self.patient_phone = ""
        self.patient_blood_group = ""
        self.patient_disease = ""

    def add_patient(self):
        self.patient_id = input("Enter patient ID: ")
        if self.patient_id in patient_data:
            print("Patient ID already exists.")
            return
        self.patient_name = input("Enter patient name: ")
        self.patient_age = int(input("Enter patient age: "))
        self.patient_gender = input("Enter patient gender: ")
        self.patient_address = input("Enter patient address: ")
        self.patient_phone = input("Enter patient phone: ")
        self.patient_blood_group = input("Enter patient blood group: ")
        self.patient_disease = input("Enter patient disease: ")

        patient_data[self.patient_id] = self.to_dict()
        print("Patient added successfully!")
        self.save_data()

    def view_all_patient(self):
        if not patient_data:
            print("No patients found.")
            return

        print("\n=====================================================")
        print("                   Patient Details:                    ")
        print("=====================================================\n")
        for patient_id in patient_data:
            print("Patient ID:", patient_data[patient_id]["patient_id"])
            print("Patient Name:", patient_data[patient_id]["patient_name"])
            print("Patient Age:", patient_data[patient_id]["patient_age"])
            print("Patient Gender:", patient_data[patient_id]["patient_gender"])
            print("Patient Address:", patient_data[patient_id]["patient_address"])
            print("Patient Phone:", patient_data[patient_id]["patient_phone"])
            print("Patient Blood Group:", patient_data[patient_id]["patient_blood_group"])
            print("Patient Disease:", patient_data[patient_id]["patient_disease"])
            print()

    
    def update_patient(self):
        patient_id = input("Enter patient ID to update: ")
        if patient_id not in patient_data:
            print("Patient not found.")
            return
        
        print("1. Update Address")
        print("2. Update Phone")
        print("3. Update Disease")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            new_address = input("Enter new address: ")
            patient_data[patient_id]["patient_address"] = new_address
        elif choice == 2:
            new_phone = input("Enter new phone: ")
            patient_data[patient_id]["patient_phone"] = new_phone
        elif choice == 3:
            new_disease = input("Enter new disease: ")
            patient_data[patient_id]["patient_disease"] = new_disease
        else:
            print("Invalid choice.")
            return
        print("Patient updated successfully!")
        self.save_data()
        
    def delete_patient(self):
        patient_id = input("Enter patient ID to delete: ")
        if patient_id not in patient_data:
            print("Patient not found.")
            return

        del patient_data[patient_id]
        print("Patient deleted successfully!")
        self.save_data()
    
    def search_patient(self):
        patient_id = input("Enter patient ID to search: ")
        if patient_id not in patient_data:
            print("Patient not found.")
            return

        print("\n=====================================================")
        print("                   Patient Details:                    ")
        print("=====================================================\n")
        print("Patient ID:", patient_data[patient_id]["patient_id"])
        print("Patient Name:", patient_data[patient_id]["patient_name"])
        print("Patient Age:", patient_data[patient_id]["patient_age"])
        print("Patient Gender:", patient_data[patient_id]["patient_gender"])
        print("Patient Address:", patient_data[patient_id]["patient_address"])
        print("Patient Phone:", patient_data[patient_id]["patient_phone"])
        print("Patient Blood Group:", patient_data[patient_id]["patient_blood_group"])
        print("Patient Disease:", patient_data[patient_id]["patient_disease"])

    def save_data(self):
        with open(PATIENT_DATA_FILE, 'w') as file:
            json.dump(patient_data, file, indent=4)

    def to_dict(self):
        return {
            "patient_id": self.patient_id,
            "patient_name": self.patient_name,
            "patient_age": self.patient_age,
            "patient_gender": self.patient_gender,
            "patient_address": self.patient_address,
            "patient_phone": self.patient_phone,
            "patient_blood_group": self.patient_blood_group,
            "patient_disease": self.patient_disease
        }


# =====================================================
#                    DOCTOR CLASS:                    
# =====================================================

class Doctor:
    def __init__(self):
        self.doctor_id = ""
        self.doctor_name = ""
        self.doctor_specialization = ""
        self.doctor_phone = ""
        self.doctor_email = ""
        self.doctor_experience = ""

    def add_doctor(self):
        self.doctor_id = input("Enter doctor ID: ")
        if self.doctor_id in doctor_data:
            print("Doctor ID already exists.")
            return
        self.doctor_name = input("Enter doctor name: ")
        self.doctor_specialization = input("Enter doctor specialization: ")
        self.doctor_phone = input("Enter doctor phone: ")
        self.doctor_email = input("Enter doctor email: ")
        self.doctor_experience = input("Enter doctor experience: ")

        doctor_data[self.doctor_id] = self.to_dict()
        print("Doctor added successfully!")
        self.save_data()

    def view_all_doctors(self):
        if not doctor_data:
            print("No doctors found.")
            return

        print("\n=====================================================")
        print("                   Doctor Details:                    ")
        print("=====================================================\n")
        for doctor_id in doctor_data:
            print("Doctor ID:", doctor_data[doctor_id]["doctor_id"])
            print("Doctor Name:", doctor_data[doctor_id]["doctor_name"])
            print("Doctor Specialization:", doctor_data[doctor_id]["doctor_specialization"])
            print("Doctor Phone:", doctor_data[doctor_id]["doctor_phone"])
            print("Doctor Email:", doctor_data[doctor_id]["doctor_email"])
            print("Doctor Experience:", doctor_data[doctor_id]["doctor_experience"])
            print()

    
    def update_doctor(self):
        doctor_id = input("Enter doctor ID to update: ")
        if doctor_id not in doctor_data:
            print("Doctor not found.")
            return

        print("1. Update Phone")
        print("2. Update Email")
        print("3. Update Experience")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            new_phone = input("Enter new phone: ")
            doctor_data[doctor_id]["doctor_phone"] = new_phone
        elif choice == 2:
            new_email = input("Enter new email: ")
            doctor_data[doctor_id]["doctor_email"] = new_email
        elif choice == 3:
            new_experience = input("Enter new experience: ")
            doctor_data[doctor_id]["doctor_experience"] = new_experience
        else:
            print("Invalid choice.")
            return
        print("Doctor updated successfully!")
        self.save_data()
        
    def delete_doctor(self):
        doctor_id = input("Enter doctor ID to delete: ")
        if doctor_id not in doctor_data:
            print("Doctor not found.")
            return

        del doctor_data[doctor_id]
        print("Doctor deleted successfully!")
        self.save_data()
    
    def search_doctor(self):
        doctor_id = input("Enter doctor ID to search: ")
        if doctor_id not in doctor_data:
            print("Doctor not found.")
            return

        print("\n=====================================================")
        print("                   Doctor Details:                    ")
        print("=====================================================\n")
        print("Doctor ID:", doctor_data[doctor_id]["doctor_id"])
        print("Doctor Name:", doctor_data[doctor_id]["doctor_name"])
        print("Doctor Specialization:", doctor_data[doctor_id]["doctor_specialization"])
        print("Doctor Phone:", doctor_data[doctor_id]["doctor_phone"])
        print("Doctor Email:", doctor_data[doctor_id]["doctor_email"])
        print("Doctor Experience:", doctor_data[doctor_id]["doctor_experience"])

    def save_data(self):
        with open(DOCTOR_DATA_FILE, 'w') as file:
            json.dump(doctor_data, file, indent=4)

    def to_dict(self):
        return {
            "doctor_id": self.doctor_id,
            "doctor_name": self.doctor_name,
            "doctor_specialization": self.doctor_specialization,
            "doctor_phone": self.doctor_phone,
            "doctor_email": self.doctor_email,
            "doctor_experience": self.doctor_experience
        }


# =====================================================
#                    APPOINTMENT CLASS:                    
# =====================================================

class Appointment:
    def __init__(self):
        self.appointment_id = ""
        self.patient_id = ""
        self.doctor_id = ""
        self.appointment_date = ""
        self.appointment_time = ""
        self.appointment_status = ""

    def add_appointment(self):
        self.appointment_id = input("Enter appointment ID: ")
        if self.appointment_id in appointment_data:
            print("Appointment ID already exists.")
            return
        self.patient_id = input("Enter patient ID: ")
        if self.patient_id not in patient_data:
            print("Patient not found.")
            return
        self.doctor_id = input("Enter doctor ID: ")
        if self.doctor_id not in doctor_data:
            print("Doctor not found.")
            return
        self.appointment_date = input("Enter appointment date (YYYY-MM-DD): ")
        self.appointment_time = input("Enter appointment time (HH:MM): ")
        self.appointment_status = "Booked"

        appointment_data[self.appointment_id] = self.to_dict()
        print("Appointment added successfully!")
        self.save_data()

    def save_data(self):
        with open(APPOINTMENT_DATA_FILE, 'w') as file:
            json.dump(appointment_data, file, indent=4)

    def view_all_appointments(self):
        if not appointment_data:
            print("No appointments found.")
            return

        print("\n=====================================================")
        print("                   Appointment Details:                    ")
        print("=====================================================\n")
        for appointment_id in appointment_data:
            print("Appointment ID:", appointment_data[appointment_id]["appointment_id"])
            print("Patient ID:", appointment_data[appointment_id]["patient_id"])
            print("Doctor ID:", appointment_data[appointment_id]["doctor_id"])
            print("Appointment Date:", appointment_data[appointment_id]["appointment_date"])
            print("Appointment Time:", appointment_data[appointment_id]["appointment_time"])
            print("Appointment Status:", appointment_data[appointment_id]["appointment_status"])
            print()

    def book_appointment(self):
        self.add_appointment()

    def cancel_appointment(self):
        appointment_id = input("Enter appointment ID to cancel: ")
        if appointment_id not in appointment_data:
            print("Appointment not found.")
            return

        del appointment_data[appointment_id]
        print("Appointment canceled successfully!")
        self.save_data()

    def to_dict(self):
        return {
            "appointment_id": self.appointment_id,
            "patient_id": self.patient_id,
            "doctor_id": self.doctor_id,
            "appointment_date": self.appointment_date,
            "appointment_time": self.appointment_time,
            "appointment_status": self.appointment_status
        }


# =====================================================
#                    MAIN FUNCTION:                    
# =====================================================

def main():
    while True:
        print("\n=====================================================")
        print("             Hospital Management System              ")
        print("=====================================================\n")
        print("1. Patient Management")
        print("2. Doctor Management")
        print("3. Appointment Management")
        print("4. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            patient = Patient()
            while True:
                print("\n=====================================================")
                print("                 Patient Management                  ")
                print("=====================================================\n")
                print("1. Add Patient")
                print("2. View All Patients")
                print("3. Update Patient")
                print("4. Delete Patient")
                print("5. Search Patient")
                print("6. Back to Main Menu")

                patient_choice = int(input("Enter your choice: "))
                if patient_choice == 1:
                    patient.add_patient()
                elif patient_choice == 2:
                    patient.view_all_patient()
                elif patient_choice == 3:
                    patient.update_patient()
                elif patient_choice == 4:
                    patient.delete_patient()
                elif patient_choice == 5:
                    patient.search_patient()
                elif patient_choice == 6:
                    break
                else:
                    print("Invalid choice.")
        elif choice == 2:
            doctor = Doctor()
            while True:
                print("\n=====================================================")
                print("                 Doctor Management                  ")
                print("=====================================================\n")
                print("1. Add Doctor")
                print("2. View All Doctors")
                print("3. Update Doctor")
                print("4. Delete Doctor")
                print("5. Search Doctor")
                print("6. Back to Main Menu")

                doctor_choice = int(input("Enter your choice: "))
                if doctor_choice == 1:
                    doctor.add_doctor()
                elif doctor_choice == 2:
                    doctor.view_all_doctors()
                elif doctor_choice == 3:
                    doctor.update_doctor()
                elif doctor_choice == 4:
                    doctor.delete_doctor()
                elif doctor_choice == 5:
                    doctor.search_doctor()
                elif doctor_choice == 6:
                    break
                else:
                    print("Invalid choice.")
        elif choice == 3:
            appointment = Appointment()
            while True:
                print("\n=====================================================")
                print("               Appointment Management               ")
                print("=====================================================\n")
                print("1. Book Appointment")
                print("2. View All Appointments")
                print("3. Cancel Appointment")
                print("4. Back to Main Menu")

                appointment_choice = int(input("Enter your choice: "))
                if appointment_choice == 1:
                    appointment.book_appointment()
                elif appointment_choice == 2:
                    appointment.view_all_appointments()
                elif appointment_choice == 3:
                    appointment.cancel_appointment()
                elif appointment_choice == 4:
                    break
                else:
                    print("Invalid choice.")
        elif choice == 4:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()