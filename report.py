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

# biology detailes for grades, including percentage and weight
biology_grades = {
    "BFL": [bio.BFL, 0.1],
    "ongoing grade": [bio.ongoing, 0.3],
    "Test1 topic7": [bio.test_scores_before_drop[0], 0.1],
    "Test2 topic9,10": [bio.test_scores_before_drop[1], 0.1],
    "Test3 topic11,12,13": [bio.test_scores_before_drop[2], 0.1],
    "EOY": [bio.EOY, 0.4]
}
# economics detailes for grades, including percentage and weight
economics_grades = {
    "ATL1": [econ.atl_list[0], 0.1],
    "ATL2": [econ.atl_list[1], 0.1],
    "assessment1": [econ.assessment_list[0], 0.1],
    "assessment2": [econ.assessment_list[1], 0.1],
    "assessment3": [econ.assessment_list[2], 0.1],
    "assessment4": [econ.assessment_list[3], 0.1],
    "EOY": [econ.eoy, 0.4]
}
# geography detailes for grades, including percentage and weight
geography_grades = {
    "BFL1": [geo.bfl_list[0], 0.1],
    "BFL2": [geo.bfl_list[1], 0.1],
    "formative1": [geo.formatives[0], 0.05],
    "formative2": [geo.formatives[1], 0.05],
    "summative1": [geo.summatives[0], 0.1],
    "summative2": [geo.summatives[1], 0.1],
    "presentation": [geo.presentation, 0.1],
    "EOY": [geo.eoy, 0.4]
}
# mathematics detailes for grades, including percentage and weight
mathematics_grades = {
    "AFL1": [maths.afl_list[0], 0.06],
    "AFL2": [maths.afl_list[1], 0.06],
    "AFL3": [maths.afl_list[2], 0.06],
    "AFL4": [maths.afl_list[3], 0.06],
    "AFL5": [maths.afl_list[4], 0.06],
    "Mock Exam": [maths.mock_list[0], 0.2],
    "Myimaths": [maths.myimaths_score, 0.1],
    "EOY": [maths.eoy, 0.4]
}

def get_best(subject_grades): # return the collection of best subject and grade as collection
    # new feature on 16/03/2026: if there are multiple subjects with the same highest score, return all of them
    highest_subjects = []
    highest_score = max(subject_grades.values())
    for subject, score in subject_grades.items():
        if score == highest_score:
            highest_subjects.append(subject)
    report_collection = [highest_subjects, highest_score] # the grades are the same, so only need to return the subjects and the same score, no need to return the grade of each subject
    return report_collection
    
def get_worst(subject_grades): # return the collection of worst subject and grade as collection
    # new feature on 16/03/2026: if there are multiple subjects with the same lowest score, return all of them
    lowest_subjects = []
    lowest_score = min(subject_grades.values())
    for subject, score in subject_grades.items():
        if score == lowest_score:
            lowest_subjects.append(subject)
    report_collection = [lowest_subjects, lowest_score] # the grades are the same, so only need to return the subjects and the same score, no need to return the grade of each subject
    return report_collection

def generate_report(subject_grades):
    best_info = get_best(subject_grades) # [0] is the best subject(s), [1] is the grade of that subject
    worst_info = get_worst(subject_grades) # [0] is the worst subject(s), [1] is the grade of that subject
    print(f"Best subject: {best_info[0]}, Score: {best_info[1]}")
    print("Congratulations dude!")
    print(f"Knowing what are your advantages and what are your shortages is a key for being successful at any school, in Cambridge Uni, NYU, or even in our SCIE!")
    print(f"Worse subject: {worst_info[0]}, Score: {worst_info[1]}")
    print(f"Let me tell you mate, you suck at your **{worst_info[0]}** most\nFOCUS one this as the prime subject next term.\nREDEEM YOURSELF!")

generate_report(subject_grades) # procedure to generate the report

print(biology_grades)
print(economics_grades)
print(geography_grades)
print(mathematics_grades)

"""
Further Notes:
1. I can add different variety of conclusion celebration, or simply put, sentences for cheering up the dude. 

2. test next time is improved/the grade that need to be reached for the next 
exam to get better result, if not, say to the user to improve next semester
"""