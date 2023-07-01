import csv

students = []
courses = []

# Load students from CSV file
def load_students():
    with open('students.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)

# Save students to CSV file
# Save students to CSV file
def save_students():
    with open('students.csv', 'w', newline='') as file:
        fieldnames = ['student_id', 'name', 'year_level', 'course_code']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)


# Load courses from CSV file
def load_courses():
    with open('courses.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            courses.append(row)

# Save courses to CSV file
def save_courses():
    with open('courses.csv', 'w', newline='') as file:
        fieldnames = ['course_code', 'course_name']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(courses)

# Add a new student
def add_student():
    student_id = input("Enter Student ID: ")
    if not student_id.isdigit():
        print("Error: Student ID should contain numbers only.")
        return

    # Check if the student ID already exists
    for student in students:
        if 'student_id' in student and student['student_id'] == student_id:
            print("Error: Student ID already exists. Please enter a unique ID.")
            return

    name = input("Enter Name: ")
    if not name:
        print("Error: Name cannot be empty.")
        return

    year_level = input("Enter Year Level: ")
    if not year_level:
        print("Error: Year Level cannot be empty.")
        return

    course_code = input("Enter Course Code: ")
    if not course_code:
        print("Error: Course Code cannot be empty.")
        return

    # Check if the course code exists
    course_exists = False
    for course in courses:
        if 'course_code' in course and course['course_code'] == course_code:
            course_exists = True
            break

    if not course_exists:
        add_course = input("Course code does not exist. Do you want to add it? (y/n): ")
        if add_course.lower() == 'y':
            course_name = input("Enter Course Name: ")
            if not course_name:
                print("Error: Course Name cannot be empty.")
                return

            new_course = {'course_code': course_code, 'course_name': course_name}
            courses.append(new_course)
            save_courses()
            print("Course added successfully.")
        else:
            return

    new_student = {'student_id': student_id, 'name': name, 'year_level': year_level, 'course_code': course_code}
    students.append(new_student)
    save_students()
    print("Student added successfully.")



# Edit student information
def edit_student():
    search_term = input("Enter Student ID or Name to edit: ")
    student = None

    # Find the student based on student ID or name
    for s in students:
        if s['student_id'] == search_term or s['name'].lower() == search_term.lower():
            student = s
            break

    if student:
        print("Edit Options:")
        print("1. Name")
        print("2. Year Level")
        print("3. Course Code")
        choice = input("Enter the number of the field to edit: ")

        if choice == "1":
            new_name = input("Enter the new Name: ")
            student['name'] = new_name
        elif choice == "2":
            new_year_level = input("Enter the new Year Level: ")
            student['year_level'] = new_year_level
        elif choice == "3":
            new_course_code = input("Enter the new Course Code: ")

            # Check if the new course code exists
            course_exists = False
            for course in courses:
                if course['course_code'] == new_course_code:
                    course_exists = True
                    break

            if not course_exists:
                add_course = input("Course code does not exist. Do you want to add it? (y/n): ")
                if add_course.lower() == 'y':
                    course_name = input("Enter Course Name: ")
                    if not course_name:
                        print("Error: Course Name cannot be empty.")
                        return

                    new_course = {'course_code': new_course_code, 'course_name': course_name}
                    courses.append(new_course)
                    save_courses()
                    print("Course added successfully.")
                else:
                    return

            student['course_code'] = new_course_code
        else:
            print("Invalid choice. No changes made.")

        save_students()
        print("Student information updated successfully!")
    else:
        print("Student not found.")

# Delete a student
# Delete a student
def delete_student():
    search_term = input("Enter Student ID or Name to delete: ")
    deleted = False

    # Find the student based on student ID or name
    for student in students:
        if student['student_id'] == search_term or student['name'].lower() == search_term.lower():
            students.remove(student)
            deleted = True

    if deleted:
        save_students()
        print("Student deleted successfully!")
    else:
        print("No student found with the given ID or name.")


# Add a new course
def add_course():
    course_code = input("Enter Course Code: ")
    if not course_code:
        print("Error: Course Code cannot be empty.")
        return

    # Check if the course code already exists
    for course in courses:
        if course['course_code'] == course_code:
            print("Error: Course Code already exists. Please enter a unique code.")
            return

    course_name = input("Enter Course Name: ")
    if not course_name:
        print("Error: Course Name cannot be empty.")
        return

    new_course = {'course_code': course_code, 'course_name': course_name}
    courses.append(new_course)
    save_courses()
    print("Course added successfully.")

# Delete a course
def delete_course():
    course_code = input("Enter Course Code to delete: ")
    deleted = False

    for course in courses:
        if course['course_code'] == course_code:
            courses.remove(course)
            # Delete students associated with the course
            for student in students:
                if student['course_code'] == course_code:
                    students.remove(student)
            deleted = True

    if deleted:
        save_courses()
        save_students()
        print("Course deleted successfully!")
    else:
        print("No course found with the given code.")

def search_student():
    search_term = input("Enter search term: ")

    results = []
    for student in students:
        if (
            search_term.lower() in student['student_id'].lower() or
            search_term.lower() in student['name'].lower() or
            search_term.lower() in student['course_code'].lower()
        ):
            results.append(student)

    if not results:
        print("No matching students found.")
    else:
        print("Matching Students:")
        for student in results:
            print(f"Student ID: {student['student_id']}")
            print(f"Name: {student['name']}")
            print(f"Year Level: {student['year_level']}")
            print(f"Course Code: {student['course_code']}")
            print("--------------------")


# Show all students
def show_all_students():
    if not students:
        print("No students found.")
    else:
        print("All Students:")
        for student in students:
            print(f"Student ID: {student['student_id']}")
            print(f"Name: {student['name']}")
            print(f"Year Level: {student['year_level']}")
            print(f"Course Code: {student['course_code']}")
            print("--------------------")

# Show all courses
def show_all_courses():
    if not courses:
        print("No courses found.")
    else:
        print("All Courses:")
        for course in courses:
            print(f"Course Code: {course['course_code']}")
            print(f"Course Name: {course['course_name']}")
            print("--------------------")
def search_course():
    search_term = input("Enter search term: ")

    results = []
    for course in courses:
        if (
            search_term.lower() in course['course_code'].lower() or
            search_term.lower() in course['course_name'].lower()
        ):
            results.append(course)

    if not results:
        print("No matching courses found.")
    else:
        print("Matching Courses:")
        for course in results:
            print(f"Course Code: {course['course_code']}")
            print(f"Course Name: {course['course_name']}")
            print("--------------------")

def edit_course():
    course_code = input("Enter the Course Code to edit: ")

    # Find the course based on course code
    for course in courses:
        if course['course_code'] == course_code:
            print("Current Course Details:")
            print(f"Course Code: {course['course_code']}")
            print(f"Course Name: {course['course_name']}")

            new_course_code = input("Enter the new Course Code (leave empty to keep the current value): ")
            new_course_name = input("Enter the new Course Name (leave empty to keep the current value): ")

            if new_course_code:
                course['course_code'] = new_course_code
            if new_course_name:
                course['course_name'] = new_course_name

            save_courses()
            print("Course updated successfully!")
            return

    print("No course found with the given code.")



# Main program loop
def main():
    load_students()
    load_courses()

    while True:
        print("\nStudent and Course Management System")
        print("1. Add Student")
        print("2. Edit Student")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. Show All Students")
        print("6. Add Course")
        print("7. Edit Course")
        print("8. Delete Course")
        print("9. Search Course")
        print("10. Show All Courses")
        print("11. Exit")

        choice = input("Enter your choice (1-11): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            edit_student()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            search_student()
        elif choice == '5':
            show_all_students()
        elif choice == '6':
            add_course()
        elif choice == '7':
            edit_course()
        elif choice == '8':
            delete_course()
        elif choice == '10':
            show_all_courses()
        
        elif choice == '9':
            search_course()
        elif choice == '11':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()