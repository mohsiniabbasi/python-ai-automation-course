score = int(input("Enter your marks: "))
if score >= 95:
    print("A+")
elif score >= 85:
    print("A")
elif score >= 75 and score < 85:
    print("B+")
elif score >= 65 and score < 75:
    print("B")
elif score >= 55 and score < 65:
    print("C+")
elif score >= 45 and score < 55:
    print("C")
else:
    print("Fail, get ready for treatment from DAD")
