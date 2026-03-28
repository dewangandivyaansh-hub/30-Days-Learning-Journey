#Grade Calculator

math=float(input("Enter your marks in Mathematics:"))
sci=float(input("Enter your marks in Science:"))
eng=float(input("Enter your marks in English:"))

total=math+sci+eng

percentage=total/3

if percentage>=90:
    grade='A'
elif percentage>=75:
    grade='B'
elif percentage>=60:
    grade='C'
elif percentage>=40:
    grade='D'
else:
    grade='FAIL'

print("TOTAL:",total)
print("PERCENTAGE:",percentage)
print("GRADE:",grade)
