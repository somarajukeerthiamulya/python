#factorial
#with arguments and with return type(possible)
"""
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return(f)
n=int(input("enter:"))
print(fact(n))
"""
#with arguments and without return type(possible)
"""
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    print("factorial:",f)
n=int(input("enter:"))
fact(n)
"""
#without arguments and with return type(possible)
"""
def fact():
    n=int(input("enter:"))
    f=1
    for i in range(1,n+1):
        f=f*i
    return(f)
print(fact())
"""
#without arguments and without return type(possible)
"""
def fact():
    n=int(input("enter:"))
    f=1
    for i in range(1,n+1):
        f=f*i
    print("factorial:",f)
fact()
"""
#-------------------------------------------------------------------------------------
#prime number
#with arguments and with return type(not possible)
#
"""
def prime(n):
    c=0
    for i in range(1,n+1):
        if(n%i==0):
            c=c+1
        return(c)
n=int(input("enter:"))
print(prime(n))
if(c==2):
    print("prime")
else:
    print("not prime")
"""
#with arguments and without return type(not possible)
#
"""
def prime(n):
    c=0
    for i in range(1,n+1):
        if(n%i==0):
            c=c+1
    print("c is:",c)
n=int(input("enter:"))
if(c==2):
    print("prime")
else:
    print("not prime")
"""
#without arguments and with return type(not possible)
"""
def prime():
    c=0
    n=int(input("enter:")
    for i in range(1,n+1):
        if(n%i==0):
            c=c+1
    return(c)
if(c==2):
    print("prime")
else:
    print("not prime")
"""
#without arguments and without return type(not possible)
"""
def prime():
    n=int(input())
    c=0
    for i in range(1,n+1):
        if(n%i==0):
            c=c+1
    print("prime num is:",c)
if(c==2):
    print("prime")
else:
    print("not prime")
"""
#-------------------------------------------------------------------------------------------------
#palindrome
#with arguments and with return type(possible)
"""
def palindrome(num):
    temp=num
    rev=0
    while(num>0):
        dig=num%10
        rev=rev*10+dig
        num=num//10
    return(rev)
num=int(input("enter:"))
rev=palindrome(num)
if(num==rev):
    print("palindrome number")
else:
    print("not palindrome number")
"""
#with arguments and without return type(not possible)
"""
def palindrome(num):
    temp=num
    rev=0
    while(num>0):
        dig=num%10
        rev=rev*10+dig
        num=num//10
    print("number is",rev)
num=int(input("enter:"))
rev=palindrome(num)
if(num==rev):
    print("palindrome number")
else:
    print("not palindrome")
"""
#without arguments and with return type(not possible)
"""
def palindrome():
    num=int(input("enter:"))
    temp=num
    rev=0
    while(num>0):
        dig=num%10
        rev=rev*10+dig
        num=num//10
    return(rev)
rev=print(palindrome())
if(num==rev):
    print("palindrome number")
else:
    print("not palindrome")
"""
#without arguments and without return type(not possible)
"""
def palindrome():
    num=int(input("enter:"))
    temp=num
    rev=0
    while(num>0):
        dig=num%10
        rev=rev*10+dig
        num=num//10
    print("number is",rev)
rev=print(palindrome())
if(num==rev):
    print("palindrome number")
else:
    print("not palindrome")
"""
#--------------------------------------------------------------------------------------
#even or odd
#with arguments and with return type(possible)(no value to return)
"""
def dig(num):
    if(num%2==0):
        print(num ,"is even")
    else:
        print(num ,"is odd")
    #return(num)
#num=int(input("enter:")
dig(5)
"""
#with arguments and without return type(possible)(no value to return)
"""
def dig(num):
    if(num%2==0):
        print(num ,"is even")
    else:
        print(num ,"is odd")
    #return(num)
#num=int(input("enter:")
dig(5)
"""
#without arguments and with return type(not possible)(no value to return)
"""
def dig():#without arguments not possible
    if(num%2==0):
        print(num ,"is even")
    else:
        print(num ,"is odd")
    #return(num)
#num=int(input("enter:")
dig(5)
"""
#without arguments and without return type(possible)(no value to return)
"""
def dig():#without arguments not possible
    if(num%2==0):
        print(num ,"is even")
    else:
        print(num ,"is odd")
    #return(num)
#num=int(input("enter:")
dig(5)
"""
#--------------------------------------------------------------------------------------------
#perfect number
#with arguments and with return type(logic error)
"""
def perfect(n):
    s=0
    for i in range(1,n+1):
        if(n%i==0):
            s=s+i
    return(s)
n=int(input("enter:"))
result=perfect(n)
if(n==result):
    print("perfect number")
else:
    print("not perfect number")
"""
#with arguments and without return type(not possible)or(logic error)
"""
def perfect(n):
    s=0
    for i in range(1,n):
        if(n%i==0):
            s=s+i
    print("s is:",s)
n=int(input("enter:"))
a=perfect(n)
if(n==a):
    print("perfect number")
else:
    print("not perfect number")
"""
#without arguments and with return type(possible)
"""
def perfect():
    s=0
    for i in range(1,n):
        if(n%i==0):
            s=s+i
    return(s)
n=int(input("enter:"))
result=perfect()
if(n==result):
    print("perfect number")
else:
    print("not perfect number")
"""
#without arguments and without return type(possible)(logic error)
"""
def perfect():
    s=0
    for i in range(1,n):
        if(n%i==0):
            s=s+i
    print("s is:",s)
n=int(input("enter:"))
result=perfect()
if(n==result):
    print("perfect number")
else:
    print("not perfect number")
"""
#-------------------------------------------------------------------------------------------
#armstrong number
#with arguments and with return type(logic error)
"""
def arm(n):
    s=0
    while(n>0):
        d=n%10
        c=d**3
        s=s+c
        n=n//10
    return(s)
n=int(input())
t=n
t=arm(n)
print(t)#function call
if(t==n):
    print("armstrong")
else:
    print("not armstrong")
"""
#with arguments and without return type(logic error)
"""
def arm(n):
    s=0
    while(n>0):
        d=n%10
        c=d**3
        s=s+c
        n=n//10
    print("s is:",s)
n=int(input())
t=n
t=arm(n)
print(t)
if(t==n):
    print("armstrong")
else:
    print("not armstrong")
"""
#without arguments and with return type(not possible)
"""
def arm():
    s=0
    while(n>0):
        d=n%10
        c=d**3
        s=s+c
        n=n//10
    return(s)
n=int(input("enter:"))
t=n
t=arm()
print(t)#function call
if(t==n):
    print("armstrong")
else:
    print("not armstrong")
"""
#without arguments and without return type(logic error)
"""
def arm():
    s=0
    while(n>0):
        d=n%10
        c=d**3
        s=s+c
        n=n//10
    print("s is:",s)
n=int(input())
t=n
t=arm()
print(t)
if(t==n):
    print("armstrong")
else:
    print("not armstrong")
"""
#---------------------------------------------------------------------------------------
#strong number
#with arguments and with return type
"""
def str(n):
    s=0
    while(n>0):
        f=1
        d=n%10
        for i in range(1,d+1):
            f=f*i
        s=s+f
        n=n//10
    return(s)
n=int(input())
t=n
t=str(n)
#print(t)
if(t==n):
    print("strong:")
else:
    print("not strong:")
"""
#with arguments and without return type(logical errror)
"""
def str(n):
    s=0
    while(n>0):
        f=1
        d=n%10
        for i in range(1,d+1):
            f=f*i
        s=s+f
        n=n//10
    print("s is:",s)
n=int(input())
t=n
t=str(n)
#print(t)
if(t==n):
    print("strong:")
else:
    print("not strong:")
"""
#without arguments and with return type
"""
def str():
    s=0
    while(n>0):
        f=1
        d=n%10
        for i in range(1,d+1):
            f=f*i
        s=s+f
        n=n//10
    return(s)
n=int(input())
t=n
t=str()
#print(t)
if(t==n):
    print("strong:")
else:
    print("not strong:")
"""
#without arguments and without return type
"""
def str():
    s=0
    while(n>0):
        f=1
        d=n%10
        for i in range(1,d+1):
            f=f*i
        s=s+f
        n=n//10
    return(s)
   print("s is:",s)
t=n
t=str()
#print(t)
if(t==n):
    print("strong:")
else:
    print("not strong:")
"""
#---------------------------------------------------------------------------------------
#fibanocci series
#with arguments and with return type
"""
def fib(n):
    a=0
    b=1
    if(n==1):
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n+1):
            c=a+b
            a=b
            b=c
            print(c)
        return(c)
n=int(input("enter:"))
fib(n)
"""
#with arguments and without return type
"""
def fib(n):
    a=0
    b=1
    if(n==1):
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n+1):
            c=a+b
            a=b
            b=c
            print(c)
        print("c is",c)
n=int(input("enter:"))
fib(n)
"""
#without arguments and with return type
"""
def fib():
    a=0
    b=1
    if(n==1):
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n+1):
            c=a+b
            a=b
            b=c
            print(c)
        return(c)
n=int(input("enter:"))
fib()
"""
#without arguments and without return type
"""
def fib():
    a=0
    b=1
    if(n==1):
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n+1):
            c=a+b
            a=b
            b=c
            print(c)
        print("c is:",c)
n=int(input("enter:"))
fib()
"""
#-----------------------------------------------------------------------------------
#recursion
#with arguments and with return type
"""
def fact(n):
    if(n==0):
        return 1
    f=n*fact(n-1)
    return(f)
n=int(input())
result=fact(n)
print(result)
"""
#with arguments and without return type
"""
def fact(n):
    if(n==0):
        return 1
    f=n*fact(n-1)
    print("f is:",f)
n=int(input())
result=fact(n)
print(result)
"""
#without arguments and with return type
"""
def fact():
    n=int(input())
    if(n==0):
        return 1
    f=n*fact(n-1)
    return(f)
#n=int(input())
result=fact()
print(result)
"""
#without arguments and without return type
"""
def fact():
    if(n==0):
        return 1
    f=n*fact(n-1)
    print("f is:",f)
n=int(input())
result=fact()
print(result)
"""
#---------------------------------------------------------------------------------
#max
"""
l=[1,2,3,4,5]
m=0
for i in l:
    if(i>m):
        m=i
print(m)

d=[23,7,11,21,9,62]
m1=d[0]
m2=[1]
for n in d:
    if(n>m1):
        m2=m1
        m1=n
    elif(n>m2):
        m2=n
print(m1)
print(m2)
"""    



























