'''from datetime import date

date_1=date(1992,1,16)
date_2=date(1991,2,5)
print(date_1-date_2)'''

'''def o(p):
    def q():
        return '*' * p
    return q

r=o(1)
s=o(2)
print(r()+s())'''

'''my_list=[1,2,3]

foo=tuple(map(lambda x: x**x, my_list))
print(foo)'''

'''import calendar

print(calendar.weekheader(2))'''

'''my_tuple=(0,1,2,3,4,5,6)
foo=list(filter(lambda x: x-0 and x-1,my_tuple))
print(foo)'''

'''from datetime import datetime
datetime=datetime(2019,11,27,11,27,22)
print(datetime.strftime('%y/%B/%d %H:%M:%S'))'''


'''def i():
    s='abcdef'
    for c in s[::2]:
        yield c

for x in i():
    print(x,end='')'''
    
'''def fun(n):
    s='+'
    for i in range(n):
        s+=s
        yield s
for i in fun(2):
    print(i,end='')'''
    
'''import calendar

c=calendar.Calendar()
for days in c.iterweekdays():
    print(days,end=' ')'''