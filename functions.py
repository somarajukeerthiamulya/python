#prime with while
"""
n=int(input())
c=1
i=1
while(n>=i):
    if(n%i==0):
        c=c+1
    i=i+1
if(c==2):
    print("prime")
        
else:
    print("not prime")
"""
#elif
"""
marks = int(input())
if(marks==100 and marks>=92):
    print("grade a+")
elif(marks<=91 and marks>=82):
    print("grade a")
elif(marks<=81 and marks>=72):
    print("grade b+")
elif(marks<=71 and marks>=62):
    print("grade b")
elif(marks<=61 and marks>=52):
    print("grade c+")
elif(marks<=51 and marks>=42):
    print("grade c")
elif(marks<=41 and marks>=32):
    print("grade d")
else:
    print("fail")
"""
#for with else
"""
n=int(input())
for i in range(0,n+1):
    break;
else:
    print(i)
"""

#continue
"""
n=int(input())
for i in range(1,n+1):
    if(i==3):
        continue
    
    print(i)
"""
#functions
"""
def a():#function gedinition
    print("hii")
    print("helo")
a()#function call
"""
#add function
"""
def add(n,m):
    print(n+m)
n=int(input())
m=int(input())
add(n,m)
"""
#fun add
"""
def add(a,b):#function definition
    print("sum:",a+b)
#main program
x=int(input("enter x :"))
y=int(input("enter y :"))
add(x,y)#function call
"""
#area of circle
#with argument and with return type
"""
def fact(n):#function definition
    f=1
    for i in range(1,n+1):
        f=f*i
    return(f)
n=int(input())
print(fact(n))#function call
"""
#with argument and without return type
"""
def fact(n):#function definition
    f=1
    for i in range(1,n+1):
        f=f*i
    print("factorial is:",f)
n=int(input())
print(fact(n))#function call
"""
#without argument and without return type
"""
def fact():
    n=int(input())
    f=1
    for i in range(1,n+1):
        f=f*i
    print("factorial is :",f)
fact()
"""
#without argument and with return type
"""
def fact():
    n=int(input())
    f=1
    for i in range(1,n+1):
        f=f*i
    return(f)
print(fact())
"""
#prime number_using without argument and with return type functions
"""
def prime():
    n=int(input())
    c=0
    for i in range(1,100):
        if(n%i==0):
            c=c+1
    for j in range(2,i):
        if(j%i==0):
            c=c+1
        if(c==2):
            print("prime")
            break
        else:
            print("not prime")
            break
    return(n)
prime()
"""
#prime number_using without argument and without return type functions
"""
def prime():
    n=int(input())
    c=0
    for i in range(1,100):
        if(n%i==0):
            c=c+1
    for j in range(2,i):
        if(j%i==0):
            c=c+1
        if(c==2):
            print("prime")
            break
        else:
            print("not prime")
            break
    print("number is :",n)
prime()
"""
#perfect number_functions
"""
def per():
    n=int(input())
    s=0
    for i in range(1,n):
        if(n%i==0):
            s=s+i
    return(s)
if(s==n):
    print("perfect")
else:
    print(" not perfect")
per()
"""
#armstrong number
"""
def arm(n):#function definition
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
#strong number
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
    print======rint("strong:")
else:
    print("not strong:")
"""
#strong number with argument and without return type(not possible)
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
num = s
#print('str value:',str(n))
#print("a value:",a)

if(t==num):
    print("strong:")
else:
    print("not strong:")
"""
#strong number without argument and with return type
"""
def str():
    s=0
    while(n>0):
        d=n%10
"""
#parameters of one
"""
def fun(name):
    print(name+"datascientist")
fun("amulya")
fun("keerthi")
"""
#parameters of two
"""
def name(f1,f2):
    print(f1+" "+f2)
name("keerthi","amulya")
"""
#args in args
"""
def fun(*args):
    for arg in args:
        print(arg)
fun("hii","helo","gm")
"""
"""
def sample(id,name,salary):
    print("id",id)
    print("name",name)
    print("salary",salary)
sample(id=111,name="amulya",salary=100000)
sample(111,"amulya",100000)
sample(id=100000,name=111,salary="amulya")
"""
#keyword arguments
"""
def printinfo(name,age):
    print("name",name)
    print("age",age)
    return;
printinfo(age=19,name="amulya")
"""
#default keywords
"""
def sample(id,name,salary=1000000):
    print("id",id)
    print("name",name)
    print("salary",salary)
sample(111,"amulya") 
"""
#default keywords(non default argument follows the default arguments)
"""
def add(a=0,b=0,c=0,d=0):
    print(a+b+c+d)
    print(a+b+c)
    print(a+b)
add(1,2,3,4)
"""
#variable length arguments(args not buildin function)
"""
def myfun(*args):
    for arg in args:
        print(args)
myfun("hii",11,"bye",12)
"""
#examples
"""
def add(*args):
    s=0
    for i in args:
        s=s+i
    print("s is:",s)
#main program
add(1,2,3,5,78,8,3,5,7,9,5,3)
"""
#args
"""
def sample(arg1,*args):
    print("1st arg is:",arg1)
    for arg in args:
        print("next arguments *args:",arg)
sample("hii","hello","bye")
"""
















