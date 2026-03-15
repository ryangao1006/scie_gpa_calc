# Initialize total score
total_score = 0.0

def calculate_econ_score():
    #globalling all the grades
    global total_score
    global eoy
    global atl_list
    global assessment_list

    total_score = 0.0
    atl_list = []
    assessment_list = []

    # Input 2 ATL scores (each worth 10%)
    for i in range(1, 3):
        while True:
            try:
                score = float(input(f"Enter ATL{i} score (percentage): "))
                atl_list.append(score)
                break
            except ValueError:
                print("Invalid input")
        total_score += score * 0.1
    
    # Input best 4 assessments scores (each worth 10%)
    for i in range(1, 5):
        while True:
            try:
                assessment = float(input(f"Enter assessment {i} score (percentage): "))
                assessment_list.append(assessment)
                break
            except ValueError:
                print("Invalid input")
        total_score += assessment * 0.1
    
    # Input EoY exam score (worth 40%)
    while True:
        try:
            eoy = float(input("Enter EoY exam score (percentage): "))
            break
        except ValueError:
            print("Invalid input")
    total_score += eoy * 0.4
    
    # Display the total mark
    print("Final Economics mark:")
    print(total_score)

if __name__ == "__main__":
    calculate_econ_score()