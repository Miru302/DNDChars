# Character Creator
import xml.etree.ElementTree as et

racesRoot = et.parse("Data\\Races.xml").getroot()

print racesRoot.findall("./Dwarf/*")
# root = et.fromstring(racesRoot)


# print len(racesRoot.findall('Races'))

# for race in racesRoot:
#     for subrace in race:
#         print subrace.tag, subrace.get("pro", default="Not Found")

# print racesRoot.find("Dwarf").find("HillDwarf").findtext("Description1", default="what?").strip()
