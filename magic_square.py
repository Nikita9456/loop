n=[[8,3,4],
   [1,5,9],
   [6,7,2]]
i=0
sum1=0
while i<len(n):
    r=0
    while r<len(n[i]):
        sum1=sum1+n[i][r]
        r=r+1
    i=i+1
print(sum1)
a=0
sum2=0
while a<len(n):
    c=0
    while c<len(n[a]):
        sum2=sum2+n[a][c]
        c=c+1
    a=a+1
print(sum2)
b=0
sum3=0
while b<len(n):
    k=0
    while k<len(n[b]):
        sum3=sum3+n[k][k]
        k=k+1
    b=b+1
print(sum3)
if sum1==sum2==sum3:
    print("magic square")
else:
    print("not magic square")



