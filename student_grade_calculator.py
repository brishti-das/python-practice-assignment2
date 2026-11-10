s_name = input("Enter Student Name: ")
marks = []

for i in range(3):
    mark = int(input(f"Enter marks for {i+1} subjects: "))
    marks.append(mark)

total = sum(marks)

avg = total / len(marks)
def grade_calculate(avg):
    scale = {
        80 : "A+",
        70 : "A",
        60 : "B",
        50 : "C",
        0 : "F"
    }
    for marks, grade in scale.items():
        if avg >= marks:
            return grade
        
final_grade = grade_calculate(avg)
print("\nStudent Name: ",s_name)
print("Total Marks: ", total)
print(f"Average Marks: {avg:.2f}")      
print(f"Final Grade: {final_grade}")