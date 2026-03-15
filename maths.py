# ==========================================
# Mathematics GPA/Total Score Calculator
# ==========================================

def get_score(prompt):
    """
    获取用户输入的分数，并进行有效性验证。
    确保输入是数字且在 0-100 之间。
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

# 初始化总分
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
    
    # 1. 输入 5 次 AFL 成绩 (每次占 6%, 共 30%)
    # 原文逻辑：循环 5 次 (range(1, 6))，每次乘以 0.06
    print("\n[Part 1] AFL Scores (5 assessments, 6% each)")
    for i in range(1, 6):
        prompt = f"Enter AFL {i} score (percentage): "
        score = get_score(prompt)
        afl_list.append(score)
        total_score += score * 0.06
        # 可选：打印当前累计分
        # print(f"-> Current Total: {total_score:.2f}")
    
    # 2. 输入 Mock Exam 成绩 (占 20%)
    print("\n[Part 2] Mock Exam (20%)")
    mock_score = get_score("Enter Mock Exam score (percentage): ")
    mock_list.append(mock_score)
    total_score += mock_score * 0.2
    
    # 3. 输入 Myimaths 成绩 (占 10%)
    print("\n[Part 3] Myimaths (10%)")
    myimaths_score = get_score("Enter Myimaths score (percentage): ")
    total_score += myimaths_score * 0.1
    
    # 4. 输入 EOY Exam (期末考试) 成绩 (占 40%)
    print("\n[Part 4] End of Year (EOY) Exam (40%)")
    eoy_score = get_score("Enter EOY Exam score (percentage): ")
    total_score += eoy_score * 0.4
    
    # ==========================================
    # 输出最终结果
    # ==========================================
    print("\n" + "="*30)
    print(f"Final Mathematics Mark: {total_score:.2f}")
    

if __name__ == "__main__":
    calculate_maths_score()