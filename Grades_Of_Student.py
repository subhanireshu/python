Marks=int(input("Enter the Marks:"))
if(Marks >= 90):
    print("Grade:A")
elif(Marks>=80 and Marks<90):
    print("Grade:B")
elif(Marks>=60 and Marks<80):
    print("Grade:C")
elif(Marks>=35 and Marks<60):
    print("Grade:D")
else:
    print("STUDENT FAILED")