"""
Karena Huang
CS80K Python
2/19/19
exercise4_7.py
"""
def computegrade(score):
    score = str(score)
    print("Enter score: " + score)
    try:
        score = float(score)
    except:
        print("Bad score")
        return

    if (score > 1.0 or score < 0.0):
        print("Bad score")
    elif (score >= 0.0 and score <= 1.0):
        if (score >= 0.9):
            print("A")
        elif (score < 0.9) and (score >= 0.8):
            print("B")
        elif (score < 0.8) and (score >= 0.7):
            print("C")
        elif (score < 0.7) and (score >= 0.6):
            print("D")
        else:
            print("F")


computegrade(0.95)
computegrade("perfect")
computegrade(10.0)
computegrade(0.75)
computegrade(0.5)
