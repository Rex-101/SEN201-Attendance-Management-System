NAME: TOCHI REX AJERO

MATRIC NUMBER: 24/13953

URL: https://github.com/Rex-101/SEN201-Attendance-Management-System


Project Title: Attendance Management System
SDLC Model Used: Waterfall Model

1. Requirement Analysis

The requirement analysis phase involves identifying and documenting the needs of users and the problems associated with manual attendance tracking.

Problem Description

In many institutions, attendance is recorded manually using paper registers. This method is time-consuming, prone to errors, and makes it difficult to retrieve attendance records or calculate attendance statistics. There is a need for a computerized system to automate attendance recording and management.

Functional Requirements

The Attendance Management System shall:

Allow entry of student names and identifiers.

Allow marking attendance as Present or Absent.

Store attendance records for each student.

Calculate total attendance for each student.

Display attendance records and summaries.

Allow viewing attendance history.

Non-Functional Requirements

The system shall:

Be easy to use and understand.

Be reliable and accurate.

Respond quickly to user input.

Run on a computer system.

Be maintainable and extensible.

2. System Design

The system design phase focuses on defining how the Attendance Management System will work internally.

Architectural Design

The system is designed as a command-line software application consisting of three main modules:

Input Module

Accepts student names.

Accepts attendance status (Present or Absent).

Processing Module

Stores attendance records.

Updates attendance counts.

Calculates attendance totals.

Output Module

Displays attendance records.

Displays attendance summaries.

Data Design

Each attendance record consists of:

Student name

Attendance status (Present / Absent)

Total number of times present

Total number of classes held

Data is stored in appropriate data structures such as lists and dictionaries.

Process Design

When a student is marked present, their attendance count increases.

When a student is marked absent, no increment is made.

Attendance totals are recalculated automatically.

3. Implementation

The Attendance Management System was implemented using the Python programming language.
The implementation follows the system design strictly, and all names and terminologies used in the design phase are consistently applied in the code.

The system includes functions to:

Add students.

Mark attendance.

View attendance records.

Display attendance summaries.

4. Testing

The testing phase ensures that the system meets all functional and non-functional requirements.

Testing Activities

Unit Testing: Each function was tested independently.

Integration Testing: Interaction between modules was tested.

System Testing: The entire system was tested with multiple students and attendance entries.

Sample Test Case

Input: Mark a student as Present
Expected Output: Attendance count increases correctly
Result: Test passed successfully

5. Deployment

After successful testing, the Attendance Management System was deployed as a Python-based command-line application.
The system can be executed on any computer system with Python installed.

Deployment involves copying the source code to the target environment and running the program using the Python interpreter.

6. Maintenance

The maintenance phase involves improving and updating the system after deployment.

Maintenance Activities

Fixing errors identified during use.

Updating attendance rules.

Improving system performance.

Adding features such as file storage, database integration, or graphical user interface.

Conclusion

The Attendance Management System successfully follows the complete Software Development Life Cycle using the Waterfall model. The system automates attendance tracking, improves accuracy, and reduces the challenges associated with manual attendance management. This project demonstrates the practical application of software engineering principles in developing a functional software solution.
