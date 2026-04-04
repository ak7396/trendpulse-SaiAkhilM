'''
You need to create a simple grade management system that works with text files.

Task 1: Create and Write Student Data (Basic)

Write a Python program that creates a file called students.txt and writes the following student records to it (one record per line):

Alice,85
Bob,92
Charlie,78
Diana,95
Each line contains a student's name and their score separated by a comma.

Constraints:

Use the appropriate file mode to create/overwrite the file
Each record must be on a new line
Close the file properly after writing
Task 2: Read and Display Data (Basic)

Write a Python program that:

Opens the students.txt file
Reads all the content
Displays each student's name and score in the format: "Student: [Name], Score: [Score]"
Constraints:

Use a 'with' block for file handling
Handle the case where the file might not exist
Expected Output:

Student: Alice, Score: 85
Student: Bob, Score: 92
Student: Charlie, Score: 78
Student: Diana, Score: 95
Task 3: Append New Student and Create Log (Basic)

Write a Python program that:

Adds a new student record "Eve,88" to the existing students.txt file without deleting previous records
Creates a log file called activity.log that records this action with a message: "Added new student: Eve"
Constraints:

Use append mode for adding the student
The new student should appear after all existing students
Create a separate log file for the activity message'''


'''file=open("students.txt","w") #x is used to create a new file if it does not exist and if it exist then it will give an error
file.write("Alice,85\n")#write is used to write the data in the file and \n is used to move to the next line after writing the data
file.write("Bob,90\n")
file.write("Charlie,78\n")
file.write("Diana,95\n")
file.close()#close is used to close the file after writing the data in it

with open ("students.txt","r") as infile :
    line=infile.readlines()#readlines is used to read the data from the file and it returns a list of lines in the file
with open("output.txt","w") as outfile :
    #a is used to append the data in the file if it already exist and if it does not exist then it will create a new file
    for newlines in line:
        name,score=newlines.strip().split(",")
        #strip is used to remove the newline character from the end of the line and split is used to split the line into name and score using comma as a separator
        outfile.write(f"Student:{name},Score:{score}\n")
        #write is used to write the data in the file and \n is used to move to the next line after writing the data
     '''

with open("students.txt","a") as file :
    file.write("Eve,88\n")
with open ("activity.log","w") as log_file:
    log_file.write("Added new student: Eve\n")