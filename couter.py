num=int(input("enter the num"))
count=0
i=1
while (i<=num):
    if (num%i==0):
            count=count+1
    i=i+1
if (count==2):
    print("prime")
else:
    print("not prime")