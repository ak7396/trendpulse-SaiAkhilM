'''
Problem Statement:

Create a grade calculation system that uses *args and **kwargs to handle different scoring scenarios.

Requirements:

Create a function calculate_grade() with:

Parameters:
*scores - Variable number of test scores
**adjustments - Optional keyword arguments for bonus points (e.g., attendance=5, project=10)
Returns: Final grade percentage (float)
Logic: Average of scores + sum of all bonus adjustments
Task: Calculate grades for:

Student with scores: 85, 90, 78 (no bonus)
Student with scores: 70, 65, 80 (with attendance=5, project=10 bonus)
Example Output:

Final Grade: 84.33%
Final Grade: 86.67%
'''


def calculate_grade(*score,**adjustments):
    if not score:
        raise ValueError("At least one score is required.")
    #using it if the score has empty value, then it will raise an error
    #not will check 
    avg=sum(score)/len(score)#finds aberage of scores
    final_total=avg+sum(adjustments.values())
    '''as ** stors in dictionary, so we are adding the
      values which are stored in dictionary by using 
    the function called sum(adjustment.values()) 
    '''
    return(final_total)   

pk= calculate_grade(90,80,70,60,50,att=5)
print(f"final grade is {pk:.2f}")
#rounfing off to 2 decimal places
