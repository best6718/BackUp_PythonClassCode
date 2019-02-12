"""
Karena Huang
CS80K Python
2/12/19
exercise3_3.py
"""
prompt = input("Please enter a score between 0.0 and 1.0: ")
try:
    float(prompt)
except:
    print("Bad score")
score = prompt
score = float(score)
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
