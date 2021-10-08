x1=0
x2=0
d=0
a=float(input("введите число 1 \n"))
b=float(input("введите число 1 \n"))
c=float(input("введите число 1 \n"))
d=(b^2-4*a*c)
if d>0:
    x1=(-b+sqrt(d))/2/a
    x2=(-b-sqrt(d))/2/a
    print(x1," ",x2)
elif d==0:
    x1=(-b)/2/a
    print(x1)
elif d<0:
    print("корней нет")
