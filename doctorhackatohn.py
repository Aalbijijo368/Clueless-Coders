from datetime import datetime
import pandas as pd

class Doctor:
    def __init__(self, name, availability):
        self.name = name
        self.availability = availability  # List of tuples (start_time, end_time)

class Patient:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class AppointmentScheduler:
    def __init__(self):
        self.doctors = []
        self.appointments = pd.DataFrame(columns=["Doctor", "Patient ID", "Patient Name", "Appointment Time"])

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def schedule_appointment(self):
        doctor_name = input("Enter doctor's name: ")
        patient_id = input("Enter patient's ID: ")
        patient_name = input("Enter patient's name: ")
        appointment_time_str = input("Enter appointment time (YYYY-MM-DD HH:MM): ")
        appointment_time = datetime.strptime(appointment_time_str, "%Y-%m-%d %H:%M")

        for doctor in self.doctors:
            if doctor.name == doctor_name:
                if appointment_time in doctor.availability:
                    self.appointments = self.appointments.append({"Doctor": doctor_name,
                                                                   "Patient ID": patient_id,
                                                                   "Patient Name": patient_name,
                                                                   "Appointment Time": appointment_time},
                                                                  ignore_index=True)
                    print(f"Appointment scheduled for {patient_name} with {doctor_name} at {appointment_time}")
                    break
                else:
                    print("Doctor not available at that time.")
                    break
        else:
            print("Doctor not found.")

    def display_schedule(self):
        print(self.appointments)

    def save_schedule_to_excel(self, file_path):
        self.appointments.to_excel(file_path, index=False)

# Example usage
if __name__ == "__main__":
    # Create doctors with their availability
    doctor1 = Doctor("Dr. Smith", [(datetime(2024, 2, 28, 9, 0), datetime(2024, 2, 28, 10, 0)),
                                   (datetime(2024, 2, 28, 11, 0), datetime(2024, 2, 28, 12, 0))])
    doctor2 = Doctor("Dr. Johnson", [(datetime(2024, 2, 28, 10, 0), datetime(2024, 2, 28, 11, 0)),
                                     (datetime(2024, 2, 28, 12, 0), datetime(2024, 2, 28, 13, 0))])

    # Create appointment scheduler and add doctors
    scheduler = AppointmentScheduler()
    scheduler.add_doctor(doctor1)
    scheduler.add_doctor(doctor2)

    # Schedule appointments
    scheduler.schedule_appointment()
    scheduler.schedule_appointment()

    # Display schedule
    scheduler.display_schedule()

    # Save schedule to Excel file
    scheduler.save_schedule_to_excel("appointments.xlsx")
