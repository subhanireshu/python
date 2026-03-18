n=int(input("Enter the number:"))
sd=0
while n>0:
    d=n%10
    sd+=d
    n=n//10

print("Sum of digits:", sd)
