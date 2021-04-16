def Fibonacci_series(num):
    if(num==0):
        return 0
    elif(num==1):
        return 1
    else:
        return (Fibonacci_series(num-2)+Fibonacci_series(num-1))
num=int(input("enter the range"))
for number in range(0,num):
    print(Fibonacci_series(number))

