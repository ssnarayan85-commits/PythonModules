## Define a Tuple - are sequences immutable python objects or cannot be modified and it's a constant list.
## it can again consists of elements of different types.
## it has paranthesis -()
## write protected
## Faster in interation and hence the improved performance

tuples3 = ('one', 'two', 'three')
tasks = ("coding", "testing", "review")

print(tasks)
print ("prints the index of testing = ", tasks.index('testing')) ## indexing
#OR
print("printing the value at index 2 =", tuples3[2])
print ("Slicing of tasks =", tasks[0:2]) ## will print dest-1
print ("Concatenating two tuples =", tuples3 + tasks)
print ("Repetition of tuples = ", tuples3 *2)
print ("Count of tuples = ", tuples3.count('one'))
'''
##Update a Tuple ( will not work)
tasks[0] = "analysis"
print (tasks)

## Extend a tuple
tasks.extend(tuples3)
print ("Extending a tuple3 with tasks", tasks)

'''
##Print lenght of  a tuple
print (len(tasks))

##Print a particular tuple
print (tasks[2])

##print a range of tuples
print (tasks[0:2])

##Concatenate two or more tuples
tuples2 = ("delivery", "closure")
print (tasks + tuples2 )

##Print multiple times
print ((tasks + tuples2) *2)
