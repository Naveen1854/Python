# Step 1: Specifying Constants for School, Class, Subjects marks,
# total snd number of students

SCHOOL_NAME = 'TS Model School'
CLASS_NAME = 'Class XI'
TOTAL_SUBJECT_MARKS = 50
TOTAL_MARKS = TOTAL_SUBJECT_MARKS * 3
NUMBER_STUDENTS  = 3

# Step 2: Get Students name, physics, chemistry and maths marks for Stident 1 and
# Calculate total marks for Student 1
student1 = input("Enter name of student 1: ")
student1_phys_marks =  int(input("Enter physics marks out of 50 for student 1: "))
student1_chem_marks =  int(input("Enter Chemistry marks out of 50 for student 1: "))
student1_math_marks =  int(input("Enter Mathematics marks out of 50 for student 1: "))
total_student1_marks = student1_phys_marks + student1_chem_marks + student1_math_marks

# Step 3: Calculating physics, chemistry and marks percentage of student 1
student1_phys_perc = round((student1_phys_marks / TOTAL_SUBJECT_MARKS) * 100,2)
student1_chem_perc = round((student1_chem_marks / TOTAL_SUBJECT_MARKS) * 100,2)
student1_math_perc = round((student1_math_marks / TOTAL_SUBJECT_MARKS) * 100,2)

# Step 4: Print results for student 1
print(f'\n{SCHOOL_NAME} - {CLASS_NAME} - {student1}')
print(f"{'-' * 72}")
print(f"| {'Subject':^15} | {'Total Marks':^15} | {'MArks_Obtained':^15} | {'Percentage':^15}|")
print(f"{'-' * 72}")
print(f"| {'physics':^15} | {TOTAL_SUBJECT_MARKS:^15} | {student1_phys_marks:^15}",
      f"| {student1_phys_perc:^15}|")
print(f"| {'Chemistry':^15} | {TOTAL_SUBJECT_MARKS:^15} | {student1_chem_marks:^15}",
      f"| {student1_chem_perc:^15}|")
print(f"| {'Mathematics':^15} | {TOTAL_SUBJECT_MARKS:^15} | {student1_math_marks:^15}",
      f"| {student1_math_perc:^15}|")
print(f"{'-' * 72}")
print(f"| {'Total':^15} | {TOTAL_MARKS:^15} | {total_student1_marks:^15}",
      f"| {round((total_student1_marks / TOTAL_MARKS) * 100,2):^15}|")
print(f"{'-' * 72}\n\n")


# Step 5: Calculate total marks for Student 2
student2 = input("Enter name of student 2: ")
student2_phys_marks =  int(input("Enter physics marks out of 50 for student 2: "))
student2_chem_marks =  int(input("Enter Chemistry marks out of 50 for student 2: "))
student2_math_marks =  int(input("Enter Mathematics marks out of 50 for student 2: "))
total_student2_marks = student2_phys_marks + student2_chem_marks + student2_math_marks

# Step 6: Calculating physics, chemistry and marks percentage of student 2
student2_phys_perc = round((student2_phys_marks / TOTAL_SUBJECT_MARKS) * 100,2)
student2_chem_perc = round((student2_chem_marks / TOTAL_SUBJECT_MARKS) * 100,2)
student2_math_perc = round((student2_math_marks / TOTAL_SUBJECT_MARKS) * 100,2)

# Step 7: Print results for student 2
print(f'\n{SCHOOL_NAME} - {CLASS_NAME} - {student2}')
print(f"{'-' * 72}")
print(f"| {'Subject':^15} | {'Total Marks':^15} | {'MArks_Obtained':^15} | {'Percentage':^15}|")
print(f"{'-' * 72}")
print(f"| {'physics':^15} | {TOTAL_SUBJECT_MARKS:^15} | {student2_phys_marks:^15}",
      f"| {student2_phys_perc:^15}|")
print(f"| {'Chemistry':^15} | {TOTAL_SUBJECT_MARKS:^15} | {student2_chem_marks:^15}",
      f"| {student2_chem_perc:^15}|")
print(f"| {'Mathematics':^15} | {TOTAL_SUBJECT_MARKS:^15} | {student2_math_marks:^15}",
      f"| {student2_math_perc:^15}|")
print(f"{'-' * 72}")
print(f"| {'Total':^15} | {TOTAL_MARKS:^15} | {total_student2_marks:^15}",
      f"| {round((total_student2_marks / TOTAL_MARKS) * 100,2):^15}|")
print(f"{'-' * 72}\n\n")


# Step 8: Calculate total marks for Student 3
student3 = input("Enter name of student 3: ")
student3_phys_marks =  int(input("Enter physics marks out of 50 for student 3: "))
student3_chem_marks =  int(input("Enter Chemistry marks out of 50 for student 3: "))
student3_math_marks =  int(input("Enter Mathematics marks out of 50 for student 3: "))
total_student3_marks = student3_phys_marks + student3_chem_marks + student3_math_marks

# Step 9: Calculating physics, chemistry and marks percentage of student 3
student3_phys_perc = round((student3_phys_marks / TOTAL_SUBJECT_MARKS) * 100,2)
student3_chem_perc = round((student3_chem_marks / TOTAL_SUBJECT_MARKS) * 100,2)
student3_math_perc = round((student3_math_marks / TOTAL_SUBJECT_MARKS) * 100,2)

# Step 10: Print results for student 3
print(f'\n{SCHOOL_NAME} - {CLASS_NAME} - {student3}')
print(f"{'-' * 72}")
print(f"| {'Subject':^15} | {'Total Marks':^15} | {'MArks_Obtained':^15} | {'Percentage':^15}|")
print(f"{'-' * 72}")
print(f"| {'physics':^15} | {TOTAL_SUBJECT_MARKS:^15} | {student3_phys_marks:^15}",
      f"| {student2_phys_perc:^15}|")
print(f"| {'Chemistry':^15} | {TOTAL_SUBJECT_MARKS:^15} | {student3_chem_marks:^15}",
      f"| {student3_chem_perc:^15}|")
print(f"| {'Mathematics':^15} | {TOTAL_SUBJECT_MARKS:^15} | {student3_math_marks:^15}",
      f"| {student3_math_perc:^15}|")
print(f"{'-' * 72}")
print(f"| {'Total':^15} | {TOTAL_MARKS:^15} | {total_student3_marks:^15}",
      f"| {round((total_student3_marks / TOTAL_MARKS) * 100,2):^15}|")
print(f"{'-' * 72}\n\n")

# Step 11: Calculate total marks obtained by all students in each subject
total_phys_marks = student1_phys_marks + student2_phys_marks + student3_phys_marks
total_chem_marks = student1_chem_marks + student2_chem_marks + student3_chem_marks
total_math_marks = student1_math_marks + student2_math_marks + student3_math_marks

# Step 12: Calculate class average for each subject
class_phys_avg = total_phys_marks / NUMBER_STUDENTS
class_chem_avg = total_chem_marks / NUMBER_STUDENTS
class_math_avg = total_math_marks / NUMBER_STUDENTS

# Step 13: Calculate class averages for each student
class_phys_perc = (class_phys_avg / TOTAL_SUBJECT_MARKS) * 100
class_chem_perc = (class_chem_avg / TOTAL_SUBJECT_MARKS) * 100
class_math_perc = (class_math_avg / TOTAL_SUBJECT_MARKS) * 100

# Step 14: Calculate total marks obtained by all students
total_student_marks = total_student1_marks + total_student2_marks + total_student3_marks

# Step 15: Calculate overall percentage
overall_perc = (total_student_marks / (NUMBER_STUDENTS * TOTAL_MARKS)) * 100

# Step 16: Print the class average percentage for each subject
print("\nClass Average And Percentage for Each Subject: ")
print(f"Physics Average is {class_phys_avg:.2f} and Percentage is {class_phys_perc:.2f}%")
print(f"Chemistry Average is {class_chem_avg:.2f} and Percentage is {class_chem_perc:.2f}%")
print(f"Mathematics Average is {class_math_avg:.2f} and Percentage is {class_math_perc:.2f}%")
print(f"Overall Percentsge: {overall_perc:.2f}%")