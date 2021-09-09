#prime number or not_for loop
"""
n=int(input())
c=0
for i in range(1,n+1):
    if(n%i==0):
        c=c+1
if(c==2):
    print("prime number")
else:
    print("not prime number")
"""
#prime number or not_while loop
"""
n=int(input())
c=0
i=1
while(n>=i):
    if(n%i==0):
        c=c+1
    i=i+1
if(c==2):
    print("prime number")
else:
    print("not prime number")
    
"""
#prime number or not_for loop(range)
"""
n=int(input())
m=int(input())
for i in range(n,m+1):
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
                break
            else:
                print(i)
                break
"""

#prime number or not_while loop(range)
"""
incomplete
n=int(input())
m=int(input())
for i in range(n,m+1):
    while(n>=i):
        if(n%j==0):
            c=c+1
        i=i+1
if(c==2):
    print(j)
"""

#even or odd_for loop
"""
n=int(input())
if(i%2==0):
    print("even number")
else:
    print("odd number")
"""

#even or odd_while loop
"""
n=int(input())
while(n%2==0):
    print("even number")
else:
    print("odd number")
"""

#even or odd_for loop(range)
"""
n=int(input())
for i in range(1,100):
    if(i%2==0):#if(i%2!=0) for odd 
        print(i)
print("\n")
"""

#even or odd_while loop(range)
"""
n=int(input())
c=1
while(n>=c):
    if(c%2==0):
            print(c)
    c=c+1
print("\n")
"""

#palindrome_for loop(incomplete)
"""
n=int(input())
t=n
r=0
for d in range(1,n+1):
    d=n%10
    r=r*10+d
    n=n//10
if(t==r):
    print("palindrome number")
else:
    print("not palindrome number")
"""

#palindrome_while loop
"""
n=int(input())
r=0
t=n
while(n>0):
    d=n%10
    r=r*10+d
    n=n//10
if(t==r):
    print("palindrome number")
else:
    print("not palindrome number")
"""    

#perfect number_for loop
"""
n=int(input())
s=0
for i in range(1,n):
    if(n%i==0):
        s=s+i
if(s==n):
    print("perfect number")
else:
    print("not perfect number")
"""
#perfect number while loop
"""
n=int(input())
s=0
i=1
while(i<n):
    if(n%i==0):
        s=s+i
    i=i+1
if(s==n):
    print("perfect number")
else:
    print("not perfect number")
"""
#armstrong number(incomplete)
"""
n=int(input())
s=0
t=n
for d in range(1,n+1):
    d=n%10
    s=s+d**3
    t=t//10
if(s==n):
    print("armstrong number")
else:
    print("not armstrong number")
"""
#factors of a number_for loop
"""
n=int(input())
for i in range(1,n+1):
    if(n%i==0):
        print(i)
"""
#factors of a number_while loop
"""
n=int(input())
i=1
while(n>=i):
    if(n%i==0):
        print(i)
    i=i+1
"""
#factorial_for loop
"""
n=int(input())
f=1
for i in range(1,n+1):
    f=f*i
print(f)
"""
#factorial_while loop
"""
n=int(input())
f=1
i=1
while(i<=n):
    f=f*i
    i=i+1
print(f)
"""   

    
            




