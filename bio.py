total = 0
assess = ""
GPA = []  # 建议使用空列表，稍后 append，或者保持原样但确保索引正确
# 既然原代码用了固定索引 [0],[1],[2]，我们保持原结构，但修复逻辑

def askforscore(assess_name):
    try:
        score = float(input("Please enter your score for " + assess_name + ": "))
        while score < 0:
            score = float(input("Your score must be greater than or equal to 0. Please enter again: "))
        return score
    except ValueError:
        print("Invalid input. Please enter a number.")
        return askforscore(assess_name)

def calculate_bio_score():
    # globalling all the grades scores. 
    global total
    global bfl_score
    global ongoing
    global test_scores_before_drop
    global EOY

    total = 0
    
    # 1. Ask for the score of BFL (10%)
    assess = "BFL"
    BFL = askforscore(assess)
    total = total + BFL * 0.1
    
    # 2. Ask for the score of ongoing grade (30%)
    assess = "ongoing grade"
    ongoing = askforscore(assess)
    total = total + ongoing * 0.3
    
    # 3. Ask for the score of the three assessments results
    # 我们将分数存入列表
    test_scores = []
    test_scores_before_drop = []
    
    assess = "Test1 topic7"
    test_scores.append(askforscore(assess))
    test_scores_before_drop.append(askforscore(assess))
    
    assess = "Test2 topic9,10"
    test_scores.append(askforscore(assess))
    test_scores_before_drop.append(askforscore(assess))
    
    assess = "Test3 topic11,12,13"
    test_scores.append(askforscore(assess))
    test_scores_before_drop.append(askforscore(assess))
    
    # 4. Drop the test with the lowest score
    # 修复点：不需要循环，直接找到最小值并移除
    if len(test_scores) > 0:
        lowest = min(test_scores)
        test_scores.remove(lowest)
        print(f"Dropped lowest test score: {lowest}")
    
    # 计算剩余两个测试的总分 (每个占10%，共20%)
    # 此时 test_scores 列表中应该只剩下两个分数
    remaining_tests_total = sum(test_scores) * 0.1 
    # 注意：原逻辑是 GPA[0]*0.1 + GPA[1]*0.1，等同于 sum(remaining) * 0.1
    total = total + remaining_tests_total
    
    # 5. Ask for the score of EOY (40%)
    assess = "EOY"
    EOY = askforscore(assess)
    total = total + EOY * 0.4
    
    # 6. Print out the total score
    print("-" * 30)
    print(f"Your total score for this semester is: {total:.2f}")

if __name__ == "__main__":
    calculate_bio_score()