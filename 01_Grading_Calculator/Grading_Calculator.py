# List to store the marks
marks = []


# Getting user total subjects
while True:
    try:
        total_subjetcs_input = input("Enter the total number of subjects: ")
        total_subjects = int(total_subjetcs_input)
        if total_subjects > 0:
            break
        else:
            print("Subjects must be a positive integer. Please try again.") 
    except ValueError:
        print("Invalid input. Please enter a valid number for total subjects.")

#input and validation phase
for i in range(total_subjects):
    while True:
        try:
            input_mark = input(f"Enter mark {i + 1}: ")
            mark = float(input_mark)

            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Invalid input. Please enter a mark between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Calculate Phase
total_marks = sum(marks)
avg_marks = total_marks / len(marks)


# Grading Phase
if min(marks) < 33:
    final_grade = "F"
    message = "You failed because you scored below 33 in one or more subjects."
elif avg_marks >= 80:
    final_grade = "A+"
    message = "Excellent! Your GPA 5.0 goal is on track."
elif avg_marks >= 70:
    final_grade = "A"
    message = "Very Good! A little more effort for A+."
elif avg_marks >= 60:
    final_grade = "A-"
    message = "Good, but you can do better."
elif avg_marks >= 33:
    final_grade = "Passed"
    message = "You passed, but need much more focus for SSC."
else:
    final_grade = "F"
    message = "Unfortunately, you failed."


# Output Phase
print("-----Results-----")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {avg_marks:.2f}")
print(f"Final Grade: {final_grade}")
print(f"Message: {message}")