n=int(input("enter the num"))
k=1
i=1
while i<=n:
    s=1
    while s<=n-i:
        print("",end="")
        s=s+1
    j=1
    while j<=k:
        print(j,end="")
        j=j+1
    k=k+1
    a=i
    while a>1:
        print(a,end="")
        a=a-1
        print()
    i=i+1
