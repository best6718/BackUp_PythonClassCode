sentence = input("Give us a sentence w lower and uppercase letters plz thx: ")
sentence = sentence.lower()
for i in sentence:
    if(i == " "):
        sentence.replace(" ", "")
    print(i)
