class Recept:
    def __init__(self, nazev, narocnost, url_adresa):
        self.nazev = nazev
        self.narocnost = narocnost
        self.url_adresa = url_adresa
        self.vyzkouseno = False
    def __str__(self):
        if self.vyzkouseno:
            return f'Recept na {self.nazev} najdeš na adrese {self.url_adresa}, náročnost receptu je {self.narocnost}/10 a byl již vyzkoušen. '
        else: 
            return f'Recept na {self.nazev} najdeš na adrese {self.url_adresa}, náročnost receptu je {self.narocnost}/10 a ještě nebyl vyzkoušen. '
    def zmen_narocnost(self, nova_hodnota):
        self.narocnost = nova_hodnota
        print (f'Náročnost receptu na {self.nazev} byla změněna na {self.narocnost}/10. ')
    def zkusit(self):
        self.vyzkouseno = True
        return True

class Kucharka:
    def __init__(self, nazev, autor):
        self.nazev = nazev
        self.autor = autor
        self.recepty = []
    def __str__(self):
        return f'Kuchařka se jmenuje {self.nazev}, je od autora {self.autor} a obsahuje {len(self.recepty)} recepty. '
    def pocet_receptu(self):
        return f'Počet receptů v kuchařce {self.nazev} je {len(self.recepty)}. '
    def pridej_recept(self,recept):
        self.recept = recept
        self.recepty.append(recept)

tiramisu = Recept('Tiramisu', 5 ,'https://fresh.iprima.cz/recepty/tiramisu')
print(tiramisu)
muffiny = Recept('Muffiny', 3, 'https://www.apetitonline.cz/menu/muffiny-varianty-z-jednoho-testa')
muffiny.zkusit()
muffiny.zmen_narocnost(2)
print(muffiny)

moje_kucharka = Kucharka('Dezerty', 'Adéla')
print(moje_kucharka) 
moje_kucharka.pridej_recept(tiramisu)
moje_kucharka.pridej_recept(muffiny)
moje_kucharka.pridej_recept('koláč')
print(moje_kucharka.pocet_receptu())
print(moje_kucharka)
