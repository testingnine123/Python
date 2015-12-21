class PartyAnimal:
   x = 0

   #functions usually have at least 1 attribute. "self" is often used
   def party(self) :
     self.x = self.x + 1
     print "So far",self.x

#create an obejct
an = PartyAnimal()

#call the methods of the class usng the obejct
an.party()
an.party()
an.party()
