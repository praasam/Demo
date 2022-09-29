#list var1
#list is changeable/mutable
var1 = [1,2,3,4,5]
print(var1)
print(type(var1))

#set
var2 = {1,3,3,4,5,5,6}
print(var2)
print(type(var2))

#tuple
#tuple is unchangeable/immutable
var3 = (1,2,3,4,2,3,4)
print(var3)
print(type(var3))

#dict
user = {'id':1, 'name': 'sita'}
print(user.keys())
print(user.values())
print(type(user))

#to print name only
print(user['name'])

#integer
var4 = int(12+2)
print(var4)
print(type(var4))

#string
var5 = "hari"
print(var5)
print(type(var5))

#float
var6 = (1.22)
print(var6)
print(type(var6))

#complex
var7 = (12+12J)
print(var7)
print(type(var7))

from array import array
#array
var1 = array('i',[3,4,5])
print(len(var1))
print(max(var1))
print(min(var1))
print(sum(var1))

#boolean
v1 = 10
v2 = 8
result=(v1>v2)
print(result)

v3 = 8
v4 = 9
result=(v3!=v4)
print(result)