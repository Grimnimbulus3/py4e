#practice for chapter 14, and Week 1 of the fourth course

#ASCII character set

#ord function gets the ascii number out
print(ord('H'))
print(ord('e'))
print(ord('\n'))

##UTF =Unicode
#UTF-16 two bytes
#UTF-32 four bytes
#UTF-8 1-4 bytes  RECOMMENDED AND AUTO DETECTIION W/ ASCII

#14.1 Object Oreinted Definitions and terminology

#an OBJECT is a self-contained piece of code and data
#Class - a template or blueprints for objects
#Method or Message:  A definied capability of class
#Field or attribute: A bit of data in a class
#Object or Instance: A particular instance of a class

#14.2 Classes: our first class and objexts
class PartyAnimal:
     x = 0
     def party(self):
         self.x = self.x + 1
         print(" So far", self.x)
an = PartyAnimal()
an.party()
an.party()
an.party()
PartyAnimal.party(an)
print ("Type", type(an))
print ("Dir ", dir(an))
print ("Type", type(an.x))
print ("Type", type(an.party))

#14.3: Object life cycle

#constructor sets up a set of initial values
#destrucot is optional and trips when the object is destroyed

#Many instances
class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, nam):
          self.name = nam
          print( self.name,'constructed')
    def party(self):
        self.x = self.x + 1
        print(self.name,'party count', self.x)
s = PartyAnimal('Sally')
j = PartyAnimal('Jim')
s.party()
j.party()
s.party()

#14.4 object inheritance
