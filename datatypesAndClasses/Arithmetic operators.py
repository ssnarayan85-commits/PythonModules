###Arithmetic Operators:

num1 = 5
num2 = 3

print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1%num2) ## gives the reminder
print(num1**num2) ##  (a**b) = a^b
print("num1//num2 =", num1//num2) ##  floor division rounds off the quotient to the lower number (1.66 will be 1)

##Assignment Operators:
num1 = num1 + num2
print(num1)

num1 += num2
print(num1)

num1 *= num2
print(num1)

num1 /= num2
print(num1)

num1 %= num2
print(num1)

num1 **= num2 ##  num1 = num1^num2
print ("num1 ^ num2=",num1)

##Comparison Operators:
num1 = 7
num2 = 5

print("Is num1 > num2", num1 > num2)
print("Is num1 < num2", num1 < num2)

print("Is num1 <= num2", num1 <=num2)
print("Is num1 >= num2", num1 >=num2)

print("Is num1 == num2", num1 == num2)
print("Is num1 != num2", num1 != num2)

##Logical Operators:

#or
x=True
y=False

'''
x=1
y=2
'''
print("x and y", x and y)
print("x or y", x or y)
print("not y ", not y)


##Bitwise Operators:
a=4 #100
b=2 #010

print('Bitwise AND', a & b)
print('Bitwise OR', a | b)
print('Bitwise XOR', a ^ b) ##returns 1 for odd number of 1s

##Right shift and Lef shift

print ("a >> 2", a >> 2 ) ##output will be 001
print ("a << 2", a << 2 ) ## output will be 10000


#Identity Operators:
x=10
print ('x is 5', x is 10)
print ('x is not 5', x is not 5)

## Membership Operators:

list1 = ['sasi', 20, "rekha"]
print ("20 in list1", 20 in list1)
print("rekha not in list1", 'rekha' not in list1)
