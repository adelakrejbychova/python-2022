from datetime import datetime

# Vstup uživatele a převedení na datum
vstup_uzivatele_datum = input('Na jaký den byste chtěl/a koupit představení? ')
datum = datetime.strptime(vstup_uzivatele_datum,"%d.%m.%Y")

# Vydefinování hlavní a vedlejší sezóny
start_den_hlavni = datetime(2021,7,1)
konec_den_hlavni = datetime(2021,8,10)
start_den_vedlejsi = datetime(2021,8,11)
konec_den_vedlejsi = datetime(2021,8,31)

if start_den_hlavni <= datum <= konec_den_vedlejsi:
    if start_den_hlavni <= datum <= konec_den_hlavni:
        cena = 250
    else:
        cena = 180
    vstup_uzivatele_pocet = int(input('Kolik lístků chcete koupit? '))
    celkova_cena = cena * vstup_uzivatele_pocet 
    print(f'Cena vašich vstupenek je {celkova_cena} Kč. ')
else:
    print('V této době je kino bohužel zavřené.')