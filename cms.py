import random
import string

class Student:
    def __init__(self, id, name, phone_number, programme):
        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.programme = programme
    
    def to_dict(self):
        return {
            'ID': self.id,
            'Name': self.name,
            'Phone Number': self.phone_number,
            'Programme': self.programme
        }

class Staff:
    def __init__(self, id, name, department):
        self.id = id
        self.name = name
        self.department = department
    
    def to_dict(self):
        return {
            'ID': self.id,
            'Name': self.name,
            'Department': self.department
        }

class Meeting:
    def __init__(self, meeting_id, student_id, staff_id, meeting_notes):
        self.meeting_id = meeting_id
        self.student_id = student_id
        self.staff_id = staff_id
        self.meeting_notes = meeting_notes
    
    def to_dict(self):
        return {
            'Meeting ID': self.meeting_id,
            'Student ID': self.student_id,
            'Staff ID': self.staff_id,
            'Meeting Notes': self.meeting_notes
        }

# In-memory data structures to store student, staff, and meeting data
students = []
staff = []
meetings = []

# Function to input student details
def input_student_details():
    id = input("Enter student ID: ")
    name = input("Enter student name: ")
    phone_number = input("Enter student phone number: ")
    
    while True:
        programme = input("Enter student programme (AI, DA, MC, G): ").upper()
        if programme in ['AI', 'DA', 'MC', 'G']:
            break
        else:
            print("Invalid programme. Please enter AI, DA, MC, or G.")

    student = Student(id, name, phone_number, programme)
    students.append(student)

# Function to view all students
def view_all_students():
    print("All Students:")
    for student in students:
        print("ID:", student.id)
        print("Name:", student.name)
        print("Phone Number:", student.phone_number)
        print("Programme:", student.programme)
        print()

# Function to input staff details
def input_staff_details():
    id = input("Enter staff ID: ")
    name = input("Enter staff name: ")
    department = input("Enter staff department: ")
    staff_member = Staff(id, name, department)
    staff.append(staff_member)

# Function to view all staff
def view_all_staff():
    print("All Staff:")
    for staff_member in staff:
        print("ID:", staff_member.id)
        print("Name:", staff_member.name)
        print("Department:", staff_member.department)
        print()

# Function to input meeting details
def input_meeting_details():
    meeting_id = input("Enter meeting ID: ")
    student_id = input("Enter student ID: ")
    staff_id = input("Enter staff ID: ")
    meeting_notes = input("Enter meeting notes: ")

    # Check if student ID exists
    student_exists = False
    for student in students:
        if student.id == student_id:
            student_exists = True
            break
    
    # Check if staff ID exists
    staff_exists = False
    for staff_member in staff:
        if staff_member.id == staff_id:
            staff_exists = True
            break

    if not student_exists:
        print("Student ID not found.")
        return
    elif not staff_exists:
        print("Staff ID not found.")
        return

    # If both student and staff IDs are valid, add the meeting
    meeting = Meeting(meeting_id, student_id, staff_id, meeting_notes)
    meetings.append(meeting)

# Function to view meeting history
def view_meeting_history():
    print("Meeting History:")
    for meeting in meetings:
        print("Meeting ID:", meeting.meeting_id)
        print("Student ID:", meeting.student_id)
        print("Staff ID:", meeting.staff_id)
        print("Meeting Notes:", meeting.meeting_notes)
        print()

# Function to update a student
def update_student():
    student_id = input("Enter the ID of the student you want to update: ")
    for student in students:
        if student.id == student_id:
            print("Current details:")
            print("Name:", student.name)
            print("Phone Number:", student.phone_number)
            print("Programme:", student.programme)
            print()
            student.name = input("Enter updated name: ")
            student.phone_number = input("Enter updated phone number: ")
            student.programme = input("Enter updated programme: ")
            print("Student details updated successfully.")
            return
    print("Student ID not found.")

# Function to delete a student
def delete_student():
    student_id = input("Enter the ID of the student you want to delete: ")
    for student in students:
        if student.id == student_id:
            students.remove(student)
            print("Student deleted successfully.")
            return
    print("Student ID not found.")

# Function to create CSV files for data structures
def create_csv_files():
    student_dicts = [student.to_dict() for student in students]
    student_df = pd.DataFrame(student_dicts)
    student_df.to_csv('student_details.csv', index=False)

    staff_dicts = [staff_member.to_dict() for staff_member in staff]
    staff_df = pd.DataFrame(staff_dicts)
    staff_df.to_csv('staff_details.csv', index=False)

    meeting_dicts = [meeting.to_dict() for meeting in meetings]
    meeting_df = pd.DataFrame(meeting_dicts)
    meeting_df.to_csv('academic_advising_details.csv', index=False)

# Main function
def main():
    while True:
        print("1. Input Student Details")
        print("2. Input Staff Details")
        print("3. Student Meeting Detail")
        print("4. View All Students")
        print("5. View All Staff")
        print("6. View Meeting History")
        print("7. Update a Student")
        print("8. Delete a Student")
        print("9. Create CSV files for Data Structures")
        print("10. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            input_student_details()
        elif choice == '2':
            input_staff_details()
        elif choice == '3':
            input_meeting_details()
        elif choice == '4':
            view_all_students()
        elif choice == '5':
            view_all_staff()
        elif choice == '6':
            view_meeting_history()
        elif choice == '7':
            update_student()
        elif choice == '8':
            delete_student()
        elif choice == '9':
            create_csv_files()
        elif choice == '10':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
