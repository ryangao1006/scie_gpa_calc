# Import total scores from subject files
import bio
import econ
import geo
import maths

# Create dictionary with cumulative grades
subject_grades = {
    "biology": bio.total,
    "economics": econ.total_score,
    "geography": geo.total_score,
    "mathematics": maths.total_score
} # a dictionary containing the cumulative grade, key: subject, value: grade in percentages

# biology detailes for grades, including percentage
biology_grades = {
    "BFL": 0.1,
    "ongoing grade": 0.3,
    "Test1 topic7": 0.1,
    "Test2 topic9,10": 0.1,
    "Test3 topic11,12,13": 0.1,
    "EOY": 0.4
}

def get_best(subject_grades): # return the collection of best subject and grade as collection
    highest_subject_score = max(subject_grades.items(), key=lambda x: x[1])
    highest_subject = highest_subject_score[0]
    highest_score = highest_subject_score[1]
    report_collection = [highest_subject, highest_score]
    return report_collection

def get_worst(subject_grades): # return the collection of worst subject and grade as collection
    lowest_subject_score = min(subject_grades.items(), key=lambda x: x[1])
    lowest_subject = lowest_subject_score[0]
    lowest_score = lowest_subject_score[1]
    report_collection = [lowest_subject, lowest_score]
    return report_collection

best_info = get_best(subject_grades) # [0] is the best subject, [1] is the grade of that subject
worst_info = get_worst(subject_grades) # [0] is the worst subject, [1] is the grade of that subject

print(f"Best subject: {best_info[0].capitalize()}, Score: {best_info[1]}")
print("Congratulations dude!")
print(f"Knowing what are your advantages and what are your shortages is a key for being successful at any school, in Cambridge Uni, NYU, or even in our SCIE!")
print(f"Worse subject: {worst_info[0].capitalize()}, Score: {worst_info[1]}")
print(f"Let me tell you mate, you suck at your **{worst_info[0].capitalize()}** most\nFOCUS one this as the prime subject next term.\nREDEEM YOURSELF!")


"""
Further Notes:
1. I can add different variety of conclusion celebration, or simply put, sentences for cheering up the dude. 

2. test next time is improved/the grade that need to be reached for the next 
exam to get better result, if not, say to the user to improve next semester
"""