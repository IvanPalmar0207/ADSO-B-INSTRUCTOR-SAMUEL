'''x,y,z=3,2,1
z,y,x=x,y,z
print(x,y,z)'''

'''d={}
d['2']=[1,2]
d['1']=[3,4]
for i in d.keys():
    print(d[i][1],end='')'''
    
'''def fun (d,k,v):
    d[k]=v
dic={}
print(fun(dic,1,'v'))'''

'''def fun(x):
    return 1 if x%2!=0 else 2
print(fun(fun(1)))'''

'''d={'one':1,'three':3,'two':2}
for i in sorted(d.values()):
    print(i,end='')'''

'''z=2
y=1
x=y<z or z>y and y>z or z<y
print(x)'''

'''d={1:0,2:1,3:2,0:1}
x=0
for y in range(len(d)):
    x=d[x]
print(x)'''

#print('a','b',sep='"')

'''x='\'
print(len(x))'''

'''v=1+1//2+1/2+2
print(v)'''

'''list1=[[c for c in range(r)] for r in range(3)]

for i in list1:
    if len(i) <2:
        print()'''

'''class A:
    def __init__(self,name):
        self.name = name
a=A('class')
print(a)'''

'''x=16
while x>0:
    print('*',end='')
    x//=2'''

'''class A:
    pass
class B:
    pass
class C(A,B):
    pass

print(issubclass(C,A) and issubclass(C,B))'''

'''class A:
    A=1
    def __init__(self):
        self.a=0
print(hasattr(A, 'A'))'''

'''i=4

while i>0:
    i-=2
    print('*')
    if i==2:
        break
else:
    print('*')'''
'''x=
print(len(x))'''

'''class X:
    pass
class Y(X):
    pass
class Z(Y):
    pass
x=X()
z=Z()
print(isinstance(x,Z),isinstance(z,X))'''


#fallos

class A:
    A=1
    def __init__(self,v=2):
        self.v=v+A.A
        A.A+=1
    def set(self,v):
        self.v+=v
        A.A+=1
        return
a=A()
a.set(2)
print(a.v)