#tässä versiossa toimii ilta ja yölisä, mutta viikonpäivää ei ole määritelty
def laske_tuntipalkka(tyotunnit_6_18, tyotunnit_18_23, tyotunnit_23_6, tuntipalkka):
    perustuntipalkka = tyotunnit_6_18 * tuntipalkka
    iltalisapalkka = tyotunnit_18_23 * (tuntipalkka + (tuntipalkka * 0.15))
    yolisapalkka = tyotunnit_23_6 * (tuntipalkka + (tuntipalkka * 0.3))

    kokonaispalkka = perustuntipalkka + iltalisapalkka + yolisapalkka

    return kokonaispalkka


tyotunnit_6_18 = float(input("Kuinka monta tuntia olit töissä 6-18? "))
tyotunnit_18_23 = float(input("Kuinka monta tuntia olit töissä 18-23? "))
tyotunnit_23_6 = float(input("Kuinka monta tuntia olit töissä 23-6? "))
tuntipalkka = float(input("Mikä on tuntipalkkasi? "))

kokonaispalkka = laske_tuntipalkka(tyotunnit_6_18, tyotunnit_18_23, tyotunnit_23_6, tuntipalkka)

print("Palkkasi on:", round(kokonaispalkka, 2))


