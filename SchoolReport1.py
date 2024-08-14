# School Report App
SCHOOL_NAME = 'TS MODEL SCHOOL'
CLASS_NAME = 'CLASS XI'
TOTAL_SUBJECT_MARKS = 50
TOTAL_MARKS = TOTAL_SUBJECT_MARKS * 3
NUMBER_STUDENTS = 2
total_phys_marks = total_chem_marks = total_math_marks = 0
class_phys_avg = class_chem_avg = class_math_avg = 0.0
class_phys_perc = class_chem_perc = class_math_perc = 0.0
overall_total_student_marks = overall_perc = 0
for i in range(NUMBER_STUDENTS):
    student_name = input(f"Enter name of Student {i+1}: ")
    if len(student_name) == 0 or student_name.isalpha() == False:
        print(f'Invalid input: Student name {student_name}')
        overall_total_student_marks = None
        break;
    phys_marks_entered = input(f"Enter physics marks out of 50 for student {i+1}: ")
    chem_marks_entered = input(f"Enter chemistry marks out of 50 for student {i+1}: ")
    math_marks_entered = input(f"Enter mathematics marks out of 50 for student {i+1}: ")
    student_phys_marks =(phys_marks_entered.isdigit() and int(phys_marks_entered) or None)
    student_chem_marks =(chem_marks_entered.isdigit() and int(chem_marks_entered) or None)
    student_math_marks =(math_marks_entered.isdigit() and int(math_marks_entered) or None)
    if(student_phys_marks is None or 0 < student_phys_marks > 50 or
       student_chem_marks is None or 0 < student_chem_marks > 50 or
       student_math_marks is None or 0 < student_math_marks > 50):
       overall_total_student_marks = None
       print(f"Invalid Input: Physics Marks: {phys_marks_entered},Chemistry",
             f"Marks: {chem_marks_entered} or Maths Marks: {math_marks_entered}")
       break;
    total_student_marks = student_phys_marks + student_chem_marks + student_math_marks
    student_phys_perc = round((student_phys_marks /TOTAL_SUBJECT_MARKS) * 100, 2)
    student_chem_perc = round((student_chem_marks / TOTAL_SUBJECT_MARKS) * 100, 2)
    student_math_perc = round((student_math_marks / TOTAL_SUBJECT_MARKS) * 100, 2)
    total_phys_marks += student_phys_marks
    total_chem_marks += student_chem_marks
    total_math_marks += student_math_marks
    overall_total_student_marks += total_student_marks
    print(f"\n{SCHOOL_NAME} - {CLASS_NAME} - {student_name}")
    print(f"{'-' * 72}")
    print(f"| {'subject':^15} | {'Total Marks':^15} | {'Marks_Obtained':^15} | {'Percentage':^15}|")
    print(f"{'-' *72}")
    print(f"| {'Physics':^15} | {TOTAL_SUBJECT_MARKS:^15} | {student_phys_marks:^15}",
          f"| {student_phys_perc:^15}|")
    print(f"| {'Chemistry':^15} | {TOTAL_SUBJECT_MARKS:^15} | {student_chem_marks:^15}",
          f"| {student_chem_perc:^15}|")
    print(f"| {'Mathematics':^15} | {TOTAL_SUBJECT_MARKS:^15} | {student_math_marks:^15}",
          f"| {student_math_perc:^15}|")
    print(f"{'-' * 72}")
    print(f"| {'Total':^15} | {TOTAL_MARKS:^15} | {total_student_marks:^15}",
          f"| {round((total_student_marks / TOTAL_MARKS)*100,2):^15}|")
    print(f"{'-' * 72}")
if overall_total_student_marks is not None:
    class_phys_avg = total_phys_marks / NUMBER_STUDENTS
    class_chem_avg = total_chem_marks / NUMBER_STUDENTS
    class_math_avg = total_math_marks / NUMBER_STUDENTS
    class_phys_perc = (class_phys_avg / TOTAL_SUBJECT_MARKS) * 100
    class_chem_perc = (class_chem_avg / TOTAL_SUBJECT_MARKS) * 100
    class_math_perc = (class_math_avg / TOTAL_SUBJECT_MARKS) * 100
    overall_perc = (overall_total_student_marks / (NUMBER_STUDENTS * TOTAL_MARKS)) * 100
    print("Class Average And Percentage for Each Subject: ")
    print(f"physics Average is {class_phys_avg:.2f} and Percentage is {class_phys_perc:.2f}%")
    print(f"Chemistry Average is {class_chem_avg:.2f} and Percentage is {class_chem_perc:.2f}%")
    print(f"Mathematics Average is {class_math_avg:.2f} and Percentage is {class_math_perc:.2f}%")
    print(f"Overall Percentage: {overall_perc:.2f}%")