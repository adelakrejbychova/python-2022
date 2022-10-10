def cislo(tel_cislo):
    if len(tel_cislo) == 13 and tel_cislo[0:4] == '+420' or len(tel_cislo) == 9:
        tel_cislo = True
        return tel_cislo
    else:
        tel_cislo = False
        print('Zadal jsi špatné číslo.')
        return tel_cislo

zadane_cislo=input('Zadej číslo: ').replace(" ","")
overeni_cisla = cislo(zadane_cislo)

if overeni_cisla:
    def text(text_zpravy):
        cena_sms = ((len(text_zpravy) // 180) + 1) * 3
        return cena_sms
    zadana_zprava = input('Zadej znění zprávy: ')
    cena = text(zadana_zprava)
    print(f'Cena SMS je {cena} Kč. ')