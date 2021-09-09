#dictionary
"""
dic={1:"amulya",2:"keerthi"}
print(type(dic))

d1={1:1,2:4,3:5}
for i in d1.keys():
    print(i)

d1={1:2,3:5,7:9}
for i in d1.values():
    print(i)

d1={1:2,2:3,3:4,5:6}
for k,v in d1.items():
    print(k,":",v)

d1={1:2,2:3,3:4,5:6}
s=0
for i in d1.values():
    s=s+i
print("s is:",s)

d1={1:"hi",2:"bye",3:"gm"}
print(len(d1))
print(d1[1])

d1={'name':'sony','age':19}
print(d1['name'])

d1={'name':'sony','age':19,'class':'first'}
print(d1['name'])
print(d1['age'])
print(d1['class'])

s={1:1,2:4,3:9,4:16}
print(s[3])
print(s.keys())
print(s.values())
print(s.items())

d1={'name':'sony','age':19,'class':'first'}
d1['age']=21
print(d1)

s={1:1,2:4,3:9,4:16}
s[1]=3
print(s)

s={1:1,2:4,3:9,4:16,5:25}
s[5]=125
print(s)

d1={'name':'sony','age':19,'class':'first'}
d1['name']='amulya'
print(d1)
d1.pop('class')
del d1['age']
print(d1)

d1={1:1,2:4,3:9,4:16,5:25}
d1[8]=d1[64]
print(d1)
d1[11]=d1.pop(2)
print(d1)

d1={1:1,2:4,3:9,4:16,5:25}
d2=d1.copy()
#d2=copy(d1)(np)
print(d2)
"""
#kwargs
"""
def sample(**kwargs):
    for k,v in kwargs.items():
        print("%s==%s" %(k,v))
sample(name='sony',age=19,clss='first')
"""
#fibanocci series
"""
n=int(input("enter:"))
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
"""
#function in function
"""
def sample1(a,b):
    print(a+b)
def sample2(a,b):
    print(a-b)
    sample1(a,b)
a=int(input())
b=int(input())
sample2(a,b)
"""
#recursion
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
#sum of num
"""
def sum(n):
    if not n:
        return(0)
    else:
        return(n[0]+sum(n[1:]))
a=sum([1,2,3,4,5])
print(a)
"""
#lambda functions(anonyomus function)
#without lambda
"""
def square(a):
    return(a*a)
result=square(5)
print(result)
"""
#with lambda function
"""
s=lambda a:a*a
print(s(5))

s=lambda a:a*a
value=s(5)
print(value)

s=lambda a,b,c:((a*b*c)/10)
value=s(11,22,33)
print(value)

s=lambda a:(3.14*a*a)
value=s(5)
print(value)

s=lambda a:(2*a*a-5*a+7)
value=s(2)
print(value)
"""
#class:collection of objects,object is an instance of class
"""
class sample:
    def function1(self):#method or function
        print("thi is an function1")
    def function2(self):#method or function
        print("thi is an function2")
#main program
obj1=sample()#object declaration
obj2=sample()#object declaration
obj1.function1()#function call
obj2.function2()#function call
print(type(obj1))
"""
#class add/dif
"""
class sample:
    def readvalues(self,a,b):
        self.a=a#instance variables
        self.b=b#instance variables
        print("a is:",a)
        print("b is:",b)
    def sum(self):
        print("sum is:",self.a+self.b)
    def dif(self):
        print("dif is:",self.a-self.b)
obj=sample()#object declaration
obj.readvalues(10,5)#function call
obj.sum()#function call
obj.dif()#function call

class sample:
    def readvalues(self,a,b):
        self.a=a
        self.b=b
        #print("a is:",a)
        #print("b is:",b)
    def sum(self):
        print("sum is:",self.a+self.b)
obj1=sample()
obj1.readvalues(10,5)
obj1.sum()

obj2=sample()
obj2.readvalues(12,6)
obj2.sum()
"""
#constructor on init method
"""
class sample:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("a is:",a)
        print("b is:",b)
    def sum(self):
        print("sum is:",self.a+self.b)
    def dif(self):
        print("dif is:",self.a-self.b)

obj1=sample(10,5)
obj1.sum()

#obj1=sample(10,5)
obj1.dif()

class sample:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def sample1(self):
        print(self.a+self.b+self.b)
        
obj1=sample("keerthi","amulya","sony")
obj1.sample1()
obj2=sample(10,5,5)
obj2.sample1()
obj3=sample(1.1,1.2,1.3)
obj3.sample1()

class sample:
    def __init__(self,name,exp,salary):
        self.name=name
        self.exp=exp
        self.salary=salary
    def output(self):
        print("name:",self.name)
        print("exp:",self.exp)
        print("salary:",self.salary)
emp=sample("amulya",1,10000000)
emp.output()

class sample:
    def __init__(self,name,exp,salary):
        self.name=name
        self.exp=exp
        self.salary=salary
    def input(self,name,exp,salary):
        self.name=name
        self.exp=exp
        self.salary=salary
    def output(self):
        print("name:",self.name)
        print("exp:",self.exp)
        print("salary:",self.salary)
emp=sample("amulya",1,10000000)
emp.output()
name=input("enter name:")
exp=input("enter exp:")
salary=input("enter salary:")
emp.input(name,exp,salary)
emp.output()        
"""
"""
class vehicle:
    def __init__(self,name,company,cost,milage):
        self.name=name
        self.company=company
        self.cost=cost
        self.milage=milage
    def input(self,name,company,cost,milage):
        self.name=name
        self.company=company
        self.cost=cost
        self.milage=milage
    def output(self):
        print("name:",self.name)
        print("company:",self.company)
        print("cost:",self.cost)
        print("milage:",self.milage)
veh=vehicle("car","audi","10Lak",100)
veh.output()
name=input("enter name:")
company=input("enter company:")
cost=input("enter cost:")
milage=input("enter milage:")
veh.input(name,company,cost,milage)
veh.output()
"""
"""
class car:#class definition
    wheels=4#class variable
    def __init__(self,company,milage,cost,speed):#constructor or init method
        self.company=company#instance variable
        self.milage=milage
        self.cost=cost
        self.speed=speed
    def output(self):
        print("company:",self.company)
        print("wheels:",self.wheels)
        print("milage;",self.milage)
        print("cost:",self.cost)
        print("speed:",self.speed)
#main program
vehicle1=car("audi",100,"1c","100kmph")#object declaration
vehicle2=car("BMW",75,"20l","75kmph")#object declaration
vehicle3=car("swift",75,"20l","75kmph")#change of wheels
vehicle4=car("RR",100,"1c","100kmph")#change of wheels
vehicle1.wheels=1
vehicle2.wheels=8
vehicle3.wheels=6
vehicle4.wheels=5
#print(vehicle1.company,vehicle1.milage,vehicle1.cost,vehicle1.speed)
#print(vehicle2.company,vehicle2.milage,vehicle2.cost,vehicle2.speed)
#print(vehicle3.company,vehicle3.milage,vehicle3.cost,vehicle3.speed)
#print(vehicle4.company,vehicle4.milage,vehicle4.cost,vehicle4.speed)
vehicle1.output()#function call
vehicle2.output()#function call
vehicle3.output()#function call
vehicle4.output()#function call
"""
"""(error)
class outer:
    def __init__(self,ov):
        self.ov=ov
        self.in1=self.inner()
    class inner:
        def __init__(self):
            self.iv=12
obj=outer(5,6)
#obj1=inner()
print("outer class value:",obj.ov)
print("inner class value:",obj.in1.iv)
"""
#inheritence
"""
class parent():#class definition
    def f1(self):
        print("it is f1")
    def f2(self):
        print("it is f2")
class child(parent):
    def f3(self):
        print("it is f3")
    def f4(self):
        print("it is f4")
c1=child()#object declaration
c1.f1()#function call
c1.f2()#function call
c1.f3()#function call
c1.f4()#function call

p1=parent()#object declaration
p1.f1()#function call
p1.f2()#function call
p1.f3()#attribute error:'parent'object has no attribute 'f3'
p1.f4()
"""
#multilevel inheritence
"""
class grandparent():
    def f1(self):
        print("it is f1")
class parent(grandparent):
    def f2(self):
        print("it is f2")
class child(parent):
    def f3(self):
        print("it is f3")
c1=child()
c1.f1()
c1.f2()
c1.f3()

p1=parent()
p1.f1()
p1.f2()
p1.f3()
"""
#multiple inheritence
"""
class parent1():
    def f1(self):
        print("it is f1")
class parent2():
    def f2(self):
        print("it is f2")
class child(parent1,parent2):
    def f3(self):
        print("it is f3")
c1=child()
c1.f1()
c1.f2()
c1.f3()
"""
#hirerical inheritence
"""
class parent():
    def f1(self):
        print("it is f1")        
class child1(parent):
    def f2(self):
        print("it is f2")
class child2(parent):
    def f3(self):
        print("it is f3")
c1=child1()
c1.f1()
c1.f2()
c2=child2()
c2.f1()
c2.f3()
"""
#real time
"""
class calcu1():
    def add(self,a,b):
        print(a+b)
class calcu2():
    def sub(self,a,b):
        print(a-b)
class calcu3():
    def mul(self,a,b):
        print(a*b)
class calcu4(calcu1,calcu2,calcu3):
    def div():
        print(a/b)
c1=calcu4()
c1.add(10,5)
c1.sub(10,5)
c1.mul(10,5)
"""
"""
class calcu1():
    def __init__(self,a,b):
        self.a = a
        self.b = b
class calcu2():
    def add(self,a,b):
        print(self.a+self.b)
class calcu3():
    def sub(self,a,b):
        print(self.a-self.b)
class calcu4():
    def mul(self,a,b):
        print(self.a*self.b)
class calcu5(calcu1,calcu2,calcu3,calcu4):
    def div(self,a,b):
        print(self.a/self.b)
c1=calcu5(10,5)
c1.add(11,1)
c1.sub(12,6)
c1.mul(18,2)
c1.div(36,6)
"""
"""
class cashier:
    def cash(self):
        print("cash")
class cros:
    def cro(self):
        print("cro")
class asss:
    def ass(self):
        print("ass")
class bms(cashier,cros,asss):
    def bm(self):
        print("bm")
    
obj=bms()
obj.cash()
obj.cro()
obj.ass()
obj.bm()
"""
"""
class A:
    def function1(self):
        print(1)
class B(A):
    pass
class C(A):
    def function2(self):
        print(2)
class D(B,C):
    pass
obj = D()
obj.function1()
obj.function2()

class parent:
    def __init__(self):
        print("it is f")
    def f1(self):
        print("it is f1")
class child(parent):
    def __init__(self):
        print("it is f2")
    def f2(self):
        print("it is f2")
obj=child()
obj.f1()
obj.f2()

class parent1:
    def __init__(self):
        print("it is f")
    def f1(self):
        print("it is f1")
class parent2(parent1):
    def __init__(self):
        print("it is f")
        super().__init__()
    def f2(self):
        print("it is f2")
class child(parent2):
    def __init__(self):
        print("it is f")
        super().__init__()
    def f3(self):
        print("it is f2")
obj=child()
obj.f1()
obj.f2()
obj.f3()
"""
#overloading
"""
a=10
b=5
print(a+b)
print(a.__add__(b))
print(a-b)
print(a.__sub__(b))
print(a*b)
print(a.__mul__(b))
print(a/b)
print(a.__mod__(b))
"""
#overloading
"""
a="keerthi"
b="amulya"
print(a+b)
print(str.__add__(a,b))
print(a.__add__(b))
"""
"""
class student:#class definition
    def __init__(self,m1,m2):#method or constructor
        self.m1=m1#instance variable
        self.m2=m2
    def __add__(self,other):
        m1=self.m1+other.m1#m1=s1.m1+s2.m1
        m2=self.m2+other.m2#m2=s1.m2+s2.m2
        s3=student(m1,m2)
        return(s3)
s1=student(10,4)
s2=student(11,5)
s3=s1+s2#s1.__add__(s2)
print(s3.m1)
print(s3.m2)
"""
"""
x=12
y=4
print(x/y)
"""
"""
x=12
y=0
print(x/y)
"""
"""
x=12
y=0
try:
    print(x/y)
except Exception:
    print("print")
"""
"""
x=12
y=0
try:
    print(x/y)
except Exception as ex:
    print("hii")

x=12
y=4
try:
    print(x/y)
except Exception as ex:
    print("hii",ex)
finally:
    print("hello")

x=12
y=0
try:
    print(x/y)
except Exception as ex:
    print("hii",ex)
finally:
    print("hello")

list1=[1,2,3,4,5]
for i in list1:
    print(i)
print(list1)
it1=iter(list1)
print(it1.__next__())
print(it1.__next__())
print(it1.__next__(),it1.__next__(),it1.__next__())
"""
"""
list1=[]
for i in range(1,10):
    list1.append(i)
print(list1)
"""
"""
def sample():
    return(1,2,3,4)
    return(5,6,7)
res=sample()
print(res)
print(res.__next__())
"""
"""
def sample():
    yield(1,2,3,4)
    yield(5)
    yield(7,8)
res=sample()
print(res)
print(res.__next__())#each and every yield will be calling
print(res.__next__())
print(res.__next__())
"""
"""
def sample():
    n=1
    while(n<=10):
        s=n*n
        yield s
        n=n+1
value=sample()
for i in value:
    print(i)
"""
#decorators
"""
def div(a,b):
    print(a/b)
div(2,4)
"""
"""
def div(a,b):
    print(a/b)
a=int(input("enter:"))
b=int(input("enter:"))
if(a>b):
    print(a/b)
else:
    a,b=b,a
    div(a,b)
"""
"""
def div(a,b):
    if(a<b):
        a,b = b,a
    print(a/b)
div(2,4)
a = int(input("Enter:"))
b = int(input("Enter:"))
print(a/b)
"""



































    
        



































