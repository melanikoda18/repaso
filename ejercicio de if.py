sign=""
repeticion=""
while repeticion!="salir":
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
    u_d = grade % 10  
    if u_d>=7 and letter!="A" and letter !="F": #asi se excluye"!=" y hay dos condiciones dentro de una toma de desiciones
        sign="+"
    elif u_d <3 and grade != 100 and letter !="F" :
        sign="-" 
    else :
        sign=""       
    print (f"your final grade is: {letter}{sign} ")
    if grade >= 70:
        print("Congratulations, you passed the subject")
    else:
        print("work harder ") 
    repeticion=input("si desea salir escriba 'salir: ").lower()