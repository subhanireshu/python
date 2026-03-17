n = int(input("Enter a number: "))

if(n%3==0 and n%5==0):
    print("ZOOM : Number is Multiple of 3 and 5")
elif(n%5==0):
    print("ZAP: Number is multiple of 5")
elif(n%3==0):
    print("ZIP: Number is multiple of 3")
else:
    print("INVALID: Number is not multiple of 3 and 5")
