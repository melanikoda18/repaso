letter=""
grade = int(input("enter your note: "))
if grade >= 90:
    letter = "A"
elif grade >=  80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
elif grade < 60:
    letter = "F"
print (f"your final grade is: {letter} ")
if grade >= 70:
    print("Congratulations, you passed the subject")
else:
    print("work harder ")    