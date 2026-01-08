attendance_records = []

def mark_attendance():
    name = input("Enter student name: ")
    status = input("Enter attendance status (Present/Absent): ")
    attendance_records.append({
        "name": name,
        "status": status
    })
    print("Attendance recorded successfully.\n")

def view_attendance():
    if not attendance_records:
        print("No attendance records available.\n")
        return

    print("\nAttendance Records")
    for record in attendance_records:
        print("Student Name:", record["name"])
        print("Status:", record["status"])
        print("--------------------")

def exit_system():
    print("Exiting Attendance Management System...")

def main():
    while True:
        print("\nAttendance Management System")
        print("1. Mark Attendance")
        print("2. View Attendance")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            mark_attendance()
        elif choice == "2":
            view_attendance()
        elif choice == "3":
            exit_system()
            break
        else:
            print("Invalid choice. Try again.")

main()
