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
import time
temps_celsius = np.array([22, 25, 28, 24, 26])
Fahrenheit  = temps_celsius *  1.8 + 32
print(f'''Temperatures in Celsius: {temps_celsius} 
Temperatures in Fahrenheit: {Fahrenheit}''')
avg_fahrenheit = np.mean(Fahrenheit)
print(f"Average Temperature in Fahrenheit: {avg_fahrenheit:.1f}")

test_score=np.array([85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 87, 84])
print(np.shape(test_score))
print(f"total number of elements in the array: {len(test_score)}")
print(f"Maximum test score: {np.max(test_score)}")
print(f"Minimum test score: {np.min(test_score)}")
print(f"range: {np.max(test_score) - np.min(test_score)}")



# Create data first (outside timing)
arr = np.arange(1, 50001)
lis = list(range(1, 50001))

# NumPy sum timing
start = time.perf_counter()
arrsum = np.sum(arr)
end = time.perf_counter()
arraytime = end - start
print(f"NumPy array sum: {arrsum}")
print(f"Time taken: {arraytime:.4f} seconds")

# List sum timing
start = time.perf_counter()
lissum = sum(lis)
end = time.perf_counter()
listtime = end - start
print(f"List sum: {lissum}")
print(f"Time taken: {listtime:.4f} seconds")

# Speed comparison
speed = listtime / arraytime
print(f"NumPy is {speed:.2f} times faster than list")






