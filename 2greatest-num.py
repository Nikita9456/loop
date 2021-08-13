num1=int(input("enter the num"))
num2=int(input("enter the num"))
num3=int(input("enter the num"))
num4=int(input("enter the num"))
if num1<num2 and num1<num3:
    if num1<num4:
        print("num3 and num4is greatest")
elif num2<num3 and num3<num4:
    if num2<num1:
        print("num4 and num1 is gretesrt")   
elif num3<num4 and num3<num2:
    if num3<num1:
        print("num1 and num2 is greatest")
elif num4<num3 and num3<num2:
    if num4<num1:
        print("num1 and num3 is greatest") 
elif num4<num2 and num2<num3:
    if num4<num1:
        print("num1 and num3 is gretesrt")                          

        