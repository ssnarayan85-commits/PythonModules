##Define a String
a = "Welcome to Python"
b = "Welcome to python, training"
print (a)
'''
##Print a particular char
print (a[3])

#Find the location of a char or Indexing
print (a.index('t'))

##print the lenght of a string
print (len(a))

##print the range of characters or Slicing
print (a[0:4])
print(a[2:7]) ## Prints from index 2 and till index (7-1)
print(a[:5]) ##  considers 0 as the starting index, prints from 0 to 5
print(a[-2]) ## prints 2nd from last
print(a[2:-2]) ## prints from 2nd index till (-2-1) position

##Reverse  a STring
print (a[::-1]) ##from reverse, the index starts from -1

##Concatenate two strings
print ("HI " + a)

#print multiple times or Repetition
print(a *3)
'''

#Type Specific methods:
##Find()
print(a.find('com')) ##Returns the index from where the given string starts
print(a.replace('Pyt', 'PYT')) ## Replaces the characters
print(a.count('o',0,4)) ##prints the number of occourences of 'o' from index 0 to index (4-1)
print(b.split(','))  ## Retu6+rns a list separated by commas