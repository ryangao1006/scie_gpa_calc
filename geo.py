# Initialize total score
total_score = 0.0

def calculate_geo_score():
    #gloabbling all the score marks in geo
    global total_score
    global bfl_list
    global formatives
    global summatives
    global presentation
    global eoy


    total_score = 0.0
    bfl_list = []
    formatives = []
    summatives = []

    # Input 2 BFL scores (each worth 10%)
    for i in range(1, 3):
        while True:
            try:
                score = float(input(f"Enter BFL{i} score (percentage): "))
                bfl_list.append(score)
                break
            except ValueError:
                print("Invalid input")
        total_score += score * 0.1
    
    # Input 2 formative assessment score (each worth 5%)
    for i in range(1, 3):
        while True:
            try:
                formative = float(input("Enter formative assessment score (percentage): "))
                formatives.append(formative)
                break
            except ValueError:
                print("Invalid input")
        total_score += formative * 0.05
    
    # Input 2 best summative assessment score (each worth 10%)
    for i in range(1, 3):
        while True:
            try:
                summative = float(input("Enter summative assessment score (percentage): "))
                summatives.append(summative)
                break
            except ValueError:
                print("Invalid input")
        total_score += summative * 0.1
    
    # Input presentation score (worth 10%)
    while True:
        try:
            presentation = float(input("Enter presentation score (percentage): "))
            break
        except ValueError:
            print("Invalid input")
    total_score += presentation * 0.1
    
    # Input EoY Exams score (worth 40%)
    while True:
        try:
            eoy = float(input("Enter EoY Exam score (percentage): "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    total_score += eoy * 0.40
    
    # Display the total mark
    print("Final Geography mark:")
    print(total_score)

if __name__ == "__main__":
    calculate_geo_score()
