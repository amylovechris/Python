import sys
a = 3
b = 4

c = 5.66
d = 8.0

e = complex(c, d)
f = complex(float(a), float(b))
#complex(a,b)

print("a is type: ",type(a))
#print("a is type: "+type(a))
print("c is type: ",type(c))
print("e is type: ",type(e))

print(a + b)
print(c/d)

print(a / c)
print(a // c)

print(e)
print(e + f)

print(sys.float_info)