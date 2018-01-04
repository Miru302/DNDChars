from character import Character

# Creating Brenuor
Bruenor = Character("Brenuor")
Bruenor.set_atributes(17, 10, 15, 8, 9, 6)
Bruenor.set_proficiency("Swords", "Axes", "Smithing")

# Testing
# print Bruenor.stats()
# print Brenuor.proficiency
# print "Proficient in " + Brenuor.proficiency[0] + " and " + Brenuor.proficiency[1]
print 'Strenght modifier =', Bruenor.CHRmod
