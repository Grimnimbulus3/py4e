#Write a function called chop that takes a list and modifies it, removing the first and last elements
#, and returns None.
#Then write a function called middle that takes a list and returns a new list that contains all
# but the first and last elements.
#
#
#
def chop(t):
    l1 = len(t)
    l2 = l1-1
    l3 = l1-2
    del t[l2:l3]
    x = t[0]
    t2 = t.remove(x)
    return(t2)
#
def middle(t):
    l1 = len(t)
    l2 = l1-1
    l3 = l1-2
    del t[l2:l3]
    x = t[0]
    t2 = t.remove(x)
    return(t)
#
a = [1,2,3,4]
print(a)
x = chop(a)
y = middle(a)
print(x)
print(y)
