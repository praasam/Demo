import sys
#False
#True
#None = None
#int = 123
#float = 123.456
#=1234+567J
#array
from array import array

var1 = {"rn":1, "name":"Pra"}
print(var1) #accessing value
print(type(var1))
print(id(var1))
print(sys.getsizeof(var1))
print(len(var1))
print(max(var1))
print(min(var1))

var1 = [1,2,3,4,5,6,7,8] #list
var2 = set(var1) #set
print(var1)
print(var2)

var1 = [1,2,3,4,1,2,3,4] #list
var2 = set(var1) #set

del(var1)
del(var2)
print(var1)
print(var2)

#class - user defined type
class C1:
    pass

obj1 = C1()
print(type(obj1))
print(id(obj1))
print(obj1)    