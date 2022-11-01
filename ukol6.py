class Znamky:
    def __init__(self, soubor_ke_cteni, soubor_k_prepsani):
        self.soubor_ke_cteni = soubor_ke_cteni
        self.soubor_k_prepsani = soubor_k_prepsani
    def prepis(self):
        with open(self.soubor_ke_cteni, mode='r',encoding = 'utf-8') as file:
            radky = file.readlines()
        modifikovane_radky=[polozka.replace("\t1","\tA").replace("\t2","\tB").replace("\t3","\tC").replace("\t4","\tD").replace("\t5","\tF") for polozka in radky]
        with open(self.soubor_k_prepsani, mode='w',encoding = 'utf-8') as file:
            file.writelines(modifikovane_radky)

znamky = Znamky('znamky.txt', 'znamky2.txt')
znamky.prepis()