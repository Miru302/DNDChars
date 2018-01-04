from character import Character

# Creating Bruenor
Bruenor = Character("Bruenor")
Bruenor.set_atributes(17, 10, 15, 8, 9, 6)
Bruenor.set_proficiency("Swords", "Axes", "Smithing")

Bruenor.proficiency.append("Spears")
# Testing
# print Bruenor.stats()
# print Bruenor.proficiency
# print "Proficient in " + Bruenor.proficiency[0] + " and " + Bruenor.proficiency[1]
# print 'Strenght modifier =', Bruenor.CHRmod

print (type(Bruenor.proficiency))
for i in range(len(Bruenor.proficiency)):
    print (Bruenor.proficiency[i])
