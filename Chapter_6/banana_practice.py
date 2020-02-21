fruit = 'banana'
letter = fruit[1]
print("Print(letter)")
print(letter) # should return a, since fruit[0] is b not fruit[1]
print("Returns a, since fruit[0] is b not fruit[1]")
length = len(fruit)
last = fruit[length-1]
print("Last:",last)
last = fruit[-1]
print("Last:",last)
# last in the previous 2 statements should be the same
print("last in the previous 2 statements should be the same")
#
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1
#this next query gives an identical output to the previous
for char in fruit:
    print(char)
#now going to String slices
s = 'Monty Python'
print(s[0:5]) # Returns 'Monty'
print(s[6:12]) #Returns 'Python'
fruit = 'banana'
fruit[:3] # returns 'ban'
fruit[3:] # returns 'ana'
fruit[3:3] # returns ''
