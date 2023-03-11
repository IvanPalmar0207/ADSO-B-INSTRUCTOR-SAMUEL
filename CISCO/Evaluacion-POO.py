'Ejercicio No1'
'''class A:
    def __str__(self):
        return 'a'
class B:
    def __str__(self):
        return 'b'
class C(A,B):
    pass

o=C()
print(o)'''

'Ejercicio No2'
'''class A:
    def __init__(self):
        pass
a=A(1)
print(hasattr(a, 'A'))'''

'Ejercicio No3'

'''class I:
    def __init__(self):
        self.s='abc'
        self.i=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i==len(self.s):
            raise StopIteration
        v=self.s[self.i]
        self.i+=1
        return v

for x in I():
    print(x,end='')'''
    
'Ejercicio No4'
'''def f(x):
    try:
        x=x/x
    except:
        print('a',end='')
    else:
        print('b',end='')
    finally:
        print('c',end='')
f(1)
f(0)'''
    
'Ejercicio No5'
'''class A:
    X=0
    def __init__(self,v=0):
        self.Y=v
        A.X+=v
a=A()
b=A(1)
c=A(2)
print(c.X)'''

'''try:
    raise Exception(1,2,3)
except Exception as e:
    print(len(e.args))'''
    
'''class A:
    def __init__(self):
        self.a=1
class B(A):
    def __init__(self):
        A.__init__()
        self.b=2'''
        
'''class A:
    A=1
print(hasattr(A,'A'))'''

#Mi puntaje en esta evaluacion fue del 75%
    