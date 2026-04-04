'''
Real-World Context:
You're maintaining a simple grade book for 5 students with their marks in 3 subjects. Use Python data structures to store and analyze this data.

Your Task:
Write a Python program using Lists, Dictionaries, Tuples, and Sets to:

Store student names and marks
Calculate averages
Find top scorer
Display results
Requirements:
Use these data structures:

List - Store student names
Dictionary - Store marks for each student
Tuple - Store subject names
Set - Store unique grades
Program should:

Display all student names
Show first 3 students (using slicing)
Calculate and print each student's average
Find student with highest average
Show all unique grades
Sample Data to Use:
Students: Raj, Priya, Amit, Sneha, Karan

Marks:
Raj: Math=85, Science=78, English=90
Priya: Math=92, Science=88, English=85
Amit: Math=70, Science=75, English=68
Sneha: Math=95, Science=90, English=92
Karan: Math=80, Science=82, English=78
Grading Logic:

Average ≥ 85: Grade A
Average ≥ 70: Grade B
Average < 70: Grade C

Expected Output:
All Students: ['Raj', 'Priya', 'Amit', 'Sneha', 'Karan']
First 3 Students: ['Raj', 'Priya', 'Amit']

Raj - Average: 84.33 - Grade: B
Priya - Average: 88.33 - Grade: A
Amit - Average: 71.00 - Grade: B
Sneha - Average: 92.33 - Grade: A
Karan - Average: 80.00 - Grade: B

Top Student: Sneha
Unique Grades: {'A', 'B'}
'''


Students=["Raj", "Priya", "Amit", "Sneha", "Karan"]
first_studnet =[]
print(f"All students: {Students}")
First_Student =Students[:3]#using slicing to get the first 3 students from the list of students
print(f"First 3 Student: {First_Student}")
    
          
S={
"Raj": { "Math":85, "Science":78, "English":90 },
"Priya": { "Math":92, "Science":88, "English":85 },
"Amit": { "Math":70, "Science":75, "English":68 },
"Sneha": { "Math":95, "Science":90, "English":92 },
"Karan": { "Math":80, "Science":82, "English":78 }
}
#using dictionary in dictionary to iterate through the students and their marks
Averages=[]#to store the average of each student
Grades=set()#to store the unique grades of each student, using set to avoid duplicates
for names,marks in S.items():#marsks is a dictionary again which store keys and values
    # again so in marks im using .values to get only marks of subjects
     Total=sum(marks.values())#to get the total marks of each student by using sum function and .values to get only the marks of subjects
     avg=Total/len(marks)#to get the average of each student by dividing the total marks by the number of subjects, using len function to get the number of subjects
     Averages.append(avg)   #to store the average of each student in the list of averages
     if avg>=85:
         grade="A"
     elif avg>=70:
         grade="B"   
     elif avg<70:
         grade="C"
     Grades.add(grade)
     print(f"{names} - Average: {avg:.2f} - Grade: {grade}")


Top_Student= max(Averages)
print(f"Top Student: {Top_Student:.2f}")
print(f"Unique Grades: {Grades}")

