class PartyAnimal:
	x = 0
	name = ""

	#consutructor
	def __init__(self,name):
		self.name = name
		print "Name constructed is",self.name

	#function, which needs to have 1 parameter ("self")
	def party(self):
		self.x = self.x + 1
		print self.name,"party count",self.x

s = PartyAnimal("Maya")
j = PartyAnimal("Sana")

s.party()
j.party()
s.party()