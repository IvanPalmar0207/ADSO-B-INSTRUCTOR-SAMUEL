'''class A:
    def __init__(self):
        pass
a=A(1)
print(hasattr(a, 'A'))'''

'''class A:
    def __init__(self, v=2):
        self.v=v
    def set(self, v=1):
        self.v+=v
        return self.v
a=A()
b=a
b.set()
print(a.v)'''

'''print(chr(ord('p')+2))'''


'''x="\\\\"
print(len(x))'''

'''try:
    raise Exception (1,2,3)
except Exception as e:
    print(len(e.args))'''
    
    
'''class I:
    def __init__(self):
        self.s='abc'
        self.i=0
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.i == len(self.s):
            raise StopIteration
        v=self.s[self.i]
        self.i+=1
        return v
for i in I():
    print(i,end='')'''
    
'''print(float('1.3'))'''

'''class A: 
    def __init__(self,v):
        self.__a=v+1
a=A(0)
print(a.__a)'''

'''from datetime import timedelta
delta=timedelta(weeks=1,days=7,hours=11)
print(delta*2)'''

'''class Class:
    def __init__(self,val=0):
        pass
object1=Class(None)
print(object1)
'''

'''import math
print(dir(math))'''

'''class A:
    A=1
    def __init__(self):
        self.a=0
print(hasattr(A, 'a'))'''

'''numbers=[i*i for i in range(5)]
foo=list(filter(lambda x: x%2, numbers))
print(foo)'''

'''class A:
    pass
class B(A):
    pass
class C(B):
    pass

print(issubclass(A,C))'''