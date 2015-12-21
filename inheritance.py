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

#inherit all properties of class PartyAnimal
class FootballFan(PartyAnimal):
	points = 0

	def touchdown(self):
		self.points = self.points + 7
		
		#call party function
		self.party()

		print self.name,"points",self.points

s = PartyAnimal("Maya")
s.party()

j = FootballFan("Sana")
j.party()
j.touchdown()
print dir(j)