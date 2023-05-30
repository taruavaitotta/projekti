#import datetime

# Kysytään veroprosentti käyttäjältä
veroprosentti = float(input("Syötä veroprosentti: "))

# Kysytään tuntipalkka käyttäjältä
tuntipalkka = float(input("Syötä tuntipalkka: "))

# Kysytään viikonpäivä käyttäjältä
viikonpaiva = input("Syötä viikonpäivä (ma-su): ")

# Kysytään kellonajan aloitusaika ja lopetusaika käyttäjältä
aloitusaika = int(input("Syötä kellonajan aloitusaika (00-24): "))
lopetusaika = int(input("Syötä kellonajan lopetusaika (00-24): "))

# Määritellään tuntimäärä palkan laskemista varten
tuntimaara = 0

# Määritellään lisäprosentti palkan laskemista varten
lisa_prosentti = 0


ilta_lisa = tuntipalkka + tuntipalkka * 0.15
yolisa = tuntipalkka + tuntipalkka * 0.30
lauantailisa = tuntipalkka + tuntipalkka * 0.20
sunnuntailisa = tuntipalkka * 2
arkipyhakorvaus = tuntipalkka * 2
verot = tuntimaara * tuntipalkka - (tuntimaara*tuntipalkka*veroprosentti/100)
tyoelakemaksu = (tuntimaara*tuntipalkka*0.0715)
tyottomyysvakuutusmaksu = (tuntimaara*tuntipalkka*0.015)

# Tarkistetaan kellonajan ja viikonpäivän perusteella lisäprosentit ja tuntimäärä
if viikonpaiva in ['ma', 'ti', 'ke', 'to', 'pe']:
    if aloitusaika >= 6 and lopetusaika <= 18:
        tuntimaara = lopetusaika - aloitusaika  # Tuntimäärä aloitus- ja lopetusajan välillä
        #tulostetaan palkka, josta on vähennetty verot ja lakisääteiset työttömyysvakuutusmaksut
        print(tuntimaara * tuntipalkka - (tuntimaara*tuntipalkka*veroprosentti/100) - (tuntimaara*tuntipalkka*0.0715)-(tuntimaara*tuntipalkka*0.015))
    elif aloitusaika < 18 and lopetusaika > 18 :
        korvaus = (18 - aloitusaika) * tuntipalkka + ((lopetusaika - 18) * tuntipalkka + tuntipalkka * 0.15)
        print(korvaus)
    

if viikonpaiva in ['la']:
    if aloitusaika >=6 and lopetusaika <=18:
        tuntimaara = lopetusaika - aloitusaika
        print(tuntimaara * (tuntipalkka + tuntipalkka * 0.20) - (tuntimaara*(tuntipalkka + tuntipalkka * 0.20)*veroprosentti/100) - (tuntimaara*(tuntipalkka + tuntipalkka * 0.20)*0.0715)-(tuntimaara*(tuntipalkka + tuntipalkka * 0.20)*0.015))
    elif aloitusaika < 18 and lopetusaika > 18 :
        korvaus = (18 - aloitusaika) * lauantailisa + ((lopetusaika - 18) * lauantailisa + tuntipalkka * 0.15)
        print(korvaus)

if viikonpaiva in ['su']:
    if aloitusaika >=6 and lopetusaika <=18:
        tuntimaara = lopetusaika - aloitusaika
        print((tuntimaara * tuntipalkka * 2) - ((tuntimaara*tuntipalkka*2)*veroprosentti/100) - ((tuntimaara*tuntipalkka * 2)*0.0715)-((tuntimaara*tuntipalkka * 2) *0.015))
    elif aloitusaika < 18 and lopetusaika > 18 :
        korvaus = (18 - aloitusaika) * sunnuntailisa + ((lopetusaika - 18) * sunnuntailisa + tuntipalkka * 0.15)
        print(korvaus)
    

