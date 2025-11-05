# marks (0–100) and print the corresponding grade (A/B/C/D/)

marks = int(input("The total marks of the student out of 600"))

grade =  (marks/600)*100


if grade>=85 and grade<=100:
    print(f"congrats,you got 'A' grade,with a {grade}%")
elif grade>=70 and grade<=84:
    print(f"good score, you got 'B' grade ,with a {grade}%")
elif grade>=50 and grade<=69:
    print(f"good score, you got 'C' grade ,with a {grade}%")
else :
    print(f"good score, you got 'D' grade ,with a {grade}%")