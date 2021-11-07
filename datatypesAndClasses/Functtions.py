'''
def add (num1, num2):
    num3 = num1 + num2
    return num3

sum = add(9,4)
print("sum =", sum )
'''


#sum of n numbers

num = int (input("Enter the value"))
if(num < 0):
    print ("Enter a valid value")
else:
    sum=0
    while (num > 0):
        sum += num
        num -= 1

print("total sum of num ",num, 'is',sum)
