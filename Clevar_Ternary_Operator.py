age=int(input("Enter the Age:"))
vote=("Person can vote","Person can't vote")[age<=18]
print(vote)