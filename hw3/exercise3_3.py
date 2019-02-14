"""
Karena Huang
CS80K Python
2/12/19
exercise3_3.py
"""
prompt = input("Please enter a score between 0.0 and 1.0: ")
try:
    prompt = float(prompt)
except:
    print("Bad score")
if (prompt > 1.0 or prompt < 0.0):
    print("Bad score")
elif (prompt >= 0.0 and prompt <= 1.0):
    if (prompt >= 0.9):
        print("A")
    elif (prompt < 0.9) and (prompt >= 0.8):
        print("B")
    elif (prompt < 0.8) and (prompt >= 0.7):
        print("C")
    elif (prompt < 0.7) and (prompt >= 0.6):
        print("D")
    else:
        print("F")
