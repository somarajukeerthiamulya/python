"""
months=set(("january","june","may"))
print(type(months))
months.update(("sep","oct","nov"))
print(months)
months.pop()
print(months)
months.pop()
print(months)
months.pop()
print(months)

integers=set((1,2,3,3,4,5,5,6,7,7,8,9,9))
print(type(integers))
print(integers)
integers.remove(5)
print(integers)
integers.pop()
print(integers)
print(integers.remove(2))

s1=set(["a","b"])
s2=set(["c","d"])
print(s1.union(s2))
"""
#interesction and union
"""
s1={"a","b","c"}
s2={"c","b"}
print(s1.intersection(s2))
print(s1 and s2)
print(s1|s2)

s1={"m","t"}
s2={"t","w","th"}
s3={3,4,5}
#print(s1.union(s2))
#print(s1.intersection(s2))
#print(s1|s2)
#print(s1.s2)
print(s1.difference(s2))

d1={"m","t","th"}
d2={"t","m"}
print(d1>d2)
print(d1<d2)
print(d1==d2)
#biggest of three
n=int(input())
l=int(input())
m=int(input())
if(n>l and n>m):
    print("n is bigger")
if(l>n and l>m):
    print("l is bigger")
if(m>l and m>n):
    print("m is bigger")
"""
n=int(input())
if(n>19):
    print("can vote")
else:
    print("not eligible")
   
