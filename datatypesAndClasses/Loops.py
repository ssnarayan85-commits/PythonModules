a=5

##while loop
while (a>0):
    print('a=', a)
    a=a-1
print('good bye')


##For loop:
for i in range(5):
    print(i)
print('good bye')

for i in range(3,6): ##it does not print 6
    print(i)
print('good bye')

for i in range(3,8,2): ##jumps two value or skips one value ..print odd numbers
    print(i)


##Nested loops:
#Print prime numbers
i=1
while (i < 20):
    if(i%2 == 0):
        print(i , 'is even number')
    else:
        print(i, ' is odd number')
    i += 1
