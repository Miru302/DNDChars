'''
The character Class
'''


class Character(object):
    def __init__(self, name):
        self.name = name

    def set_atributes(self, STR, DEX, CON, INT, WIS, CHR):
        self.STR = STR
        self.DEX = DEX
        self.CON = CON
        self.INT = INT
        self.WIS = WIS
        self.CHR = CHR

        self.STRmod = (STR - 10) / 2
        self.DEXmod = (DEX - 10) / 2
        self.CONmod = (CON - 10) / 2
        self.INTmod = (INT - 10) / 2
        self.WISmod = (WIS - 10) / 2
        self.CHRmod = (CHR - 10) / 2

    def set_proficiency_list(self, *args):
        self.proficiency_list = list(args)

    def stats(self):
        return ('Strenght {} \nDexterity {} \nConstitution {} \nIntelect {} \nWisdom {} \nCharisma {}'
                .format(self.STR, self.DEX, self.CON, self.INT, self.WIS, self.CHR))
