a=1
while a<=100:
    if a%3==0:
        if a%7==0:
            print("navgurukul")
        else:
            print("nav")
    elif a%7==0:
        print("gurukul")
    else:
        print(a)
    a=a+1