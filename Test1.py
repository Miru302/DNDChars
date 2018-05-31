from character import Character

# Creating Bruenor
Bruenor = Character("Bruenor")
Bruenor.set_atributes(17, 10, 15, 8, 9, 6)
Bruenor.set_proficiency_list("Swords", "Axes", "Smithing")

Bruenor.proficiency_list.append("Spears")
# Testing
print Bruenor.stats()
# print Bruenor.proficiency
# print "Proficient in " + Bruenor.proficiency[0] + " and " + Bruenor.proficiency[1]
# print 'Strenght modifier =', Bruenor.CHRmod

print (type(Bruenor.proficiency_list))
for i in range(len(Bruenor.proficiency_list)):
    print (Bruenor.proficiency_list[i])

print Bruenor.STR
