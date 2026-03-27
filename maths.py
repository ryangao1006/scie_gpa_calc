# ==========================================
# Mathematics GPA/Total Score Calculator
# ==========================================

def get_score(prompt):
    """
    Get user input score and validate it.
    Ensure input is a number and between 0-100.
    """
    while True:
        try:
            score = float(input(prompt))
            if 0 <= score <= 100:
                return score
            else:
                print("Error: Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Initialize total score
total_score = 0.0

def calculate_maths_score():
    global total_score
    global afl_list
    global mock_list
    global myimaths_score
    global eoy

    afl_list = []
    mock_list = []
    total_score = 0.0
    
    print("--- Mathematics Grade Calculator ---")
    
    # 1. Input 5 AFL scores (6% each, total 30%)
    # Original logic: loop 5 times (range(1, 6)), multiply by 0.06 each time
    print("\n[Part 1] AFL Scores (5 assessments, 6% each)")
    for i in range(1, 6):
        prompt = f"Enter AFL {i} score (percentage): "
        score = get_score(prompt)
        afl_list.append(score)
        total_score += score * 0.06
        # Optional: print current total
        # print(f"-> Current Total: {total_score:.2f}")
    
    # 2. Input Mock Exam score (20%)
    print("\n[Part 2] Mock Exam (20%)")
    mock_score = get_score("Enter Mock Exam score (percentage): ")
    mock_list.append(mock_score)
    total_score += mock_score * 0.2
    
    # 3. Input Myimaths score (10%)
    print("\n[Part 3] Myimaths (10%)")
    myimaths_score = get_score("Enter Myimaths score (percentage): ")
    total_score += myimaths_score * 0.1
    
    # 4. Input EOY Exam (End of Year) score (40%)
    print("\n[Part 4] End of Year (EOY) Exam (40%)")
    eoy = get_score("Enter EOY Exam score (percentage): ")
    total_score += eoy * 0.4
    
    # ==========================================
    # Output final result
    # ==========================================
    print("\n" + "="*30)
    print(f"Final Mathematics Mark: {total_score:.2f}")
    

if __name__ == "__main__":
    calculate_maths_score()