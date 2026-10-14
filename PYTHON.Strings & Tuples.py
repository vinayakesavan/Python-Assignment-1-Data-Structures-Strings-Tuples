a="Hello "
b=input("enter your name:")
c=(a+b)
print(c)
d=", welcome to Python programming"
z=(c+d)
print(z)
print(z[0])
print(z[-1])
print(z[0:5])
print(z[-11:])
k=(z[::-1])

print(k)

p=(k[12:18])
print(p[::-1])


strM = "Python beginner tutorial"
print(strM)
print(strM.upper())
print(strM.lower())
print(strM.capitalize())

print(strM.count("t"))
print(strM.replace("Python","Machine Learning"))


'''Tuples'''
tup1=[10,20,30]
print(tup1)
tup2=[40,50,60]
print(tup2)


t_combine=(tup1+tup2)
print(t_combine)
print(t_combine+t_combine+t_combine)
print(t_combine[2])
print(t_combine[0:3])
print(t_combine[-3:])
