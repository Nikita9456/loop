num=int(input('enter the num'))
i=num
sum=0
while i>0:
    d=i%10
    sum=sum+d**3
    i=i//10
if sum==num:
    print("its armstrong")
else:
    print("not armstron")