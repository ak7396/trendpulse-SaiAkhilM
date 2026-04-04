'''
##problem statement

Question
You are building a simulated classroom test score system using NumPy. The system generates random scores, analyzes performance across subjects, and normalizes the data for fair comparison — all using NumPy array operations.

Task 1 — Generate and Inspect the Data Using numpy.random.seed(42), generate a 2D NumPy array called scores of shape (5, 4) representing 5 students and 4 subjects, filled with random integers between 50 and 100 (inclusive). Then extract and print the following:

The score of the 3rd student in the 2nd subject
All scores of the last 2 students (all subjects)
All scores for the first 3 students in subjects 2 and 3 only
Task 2 — Analyze with Broadcasting Using the scores array from Task 1, perform the following without any Python loops:

Compute the column-wise mean (average score per subject), rounded to 2 decimal places
Add a curve to the scores by adding [5, 3, 7, 2] to every student's row (one value per subject) using broadcasting, storing the result in curved_scores — ensure no score exceeds 100 after curving
Compute the row-wise max of curved_scores (best subject score per student)
Task 3 — Normalize and Identify Using curved_scores from Task 2:

Normalize each student's scores to a 0–1 scale using min-max normalization per row: (score - row_min) / (row_max - row_min). The result should be a 2D array of the same shape
Using the normalized array, identify and print the student index (row) and subject index (column) of the single highest value across the entire array
Finally, extract all scores from curved_scores that are strictly above 90 as a 1D array using boolean masking

'''
import numpy as np
print("-"*30,"Task 1","-"*30)
scores=np.random.seed(42)
scores=np.random.randint(50,101,size=(5,4))
#print(scores)
print(f'''The score of the 3rd student in the 2nd subject is 
{scores[2,1]}''')
print(f'''All scores of the last 2 students
{scores[3:5,:]}''')
print(f'''All scores of the first 3 students in subjects 2 and 3
{scores[0:3,1:3]}''')


## task 2
print("-"*30,"Task 2","-"*30)

average_score_persubject=scores.mean(axis=0)
print(f"Average score per subject: {average_score_persubject.round(2)}")
# as per condition add a cure as guven which is [5,2,7,2]
curve=np.array([5,3,7,2])
#2.1
curved_scores_without_exceed =scores + curve
curved_scores=np.clip(curved_scores_without_exceed,0,100)#clip will make sure the min and max values are in the givem limits if it goes 102 it  makes to 100
print(f"curved_scores:\n{curved_scores}")
#2.2
Row_wise_max = np.max(curved_scores, axis=1)
print(f"best subject score per student is \n{Row_wise_max}")

#3.0
print("-"*30,"Task 3","-"*30)
max=curved_scores.max(axis=1,keepdims=True)# keepdims will make sure the diemnssions are favorable for broadcasting if we miss that the arry dim will be like(5,)not possible for broadcasting
#print(f"max{max}")
min=curved_scores.min(axis=1,keepdims=True)
#print(f"min{min}")
#print("#"*30)
nor=(curved_scores-min)/(max-min)
print(nor)
print(f"The shape of the normalized array is {nor.shape}")

#3.1 indexing using flattening
idx = np.argmax(nor)#.argmax will return first higedt value of the array

#print(idx)
row, col = np.unravel_index(idx, nor.shape)#Flat index → multi-dimensional index
#print(row,col) #This line converts the flattened position of the maximum value into the actual row and column position inside the 2D array.'''  
print(f"Highest value is at student index {row}, subject index {col}")
#3.2 bboolean masking
higest_scores=curved_scores[curved_scores>90]
print(f"scores greater than 90n are {higest_scores}")





