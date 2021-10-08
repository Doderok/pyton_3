
a=float(input("введите число \n"))
if (a%5!=0) and (a%7!=0):
    print("00")
elif (a%5==0) and (a%7!=0): 
    print("01")
elif (a%5!=0) and (a%7==0):
    print("10")
elif (a%5==0) and (a%7==0):
    print("11")
