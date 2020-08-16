import time, os
from selenium import webdriver
from modules import modules


def downloadEvent(browser, listaWydarzen, licznik=1, allWydarzen=1):
    raport = modules.otworzPlikRaportu()  # otwarcie pliku z raportem

    #logownaie do profilu
    #modules.logowanieDoProfilu(browser)

    # pobieranie wydarzeń ze strony
    for wydarzenie in listaWydarzen:
        browser.get(wydarzenie)
        browser.implicitly_wait(5)
        # pobieranie wydarzeń ze strony wg listy pliku linki_wydarzen.txt
        nazwa = modules.pobierzTytulOrganizatorzy(browser)
        czasWydarzenia = modules.pobierzDataCzasMiejsce(browser, temp='czas')
        miejsce = modules.pobierzDataCzasMiejsce(browser, temp='miejsce')
        frekwencja = modules.pobierzFrekwencja(browser)
        opis = modules.pobierzOpis(browser)

        modules.sprawdzPoprawnoscDanych(nazwa)
        modules.sprawdzPoprawnoscDanych(czasWydarzenia)
        modules.sprawdzPoprawnoscDanych(miejsce)
        modules.sprawdzPoprawnoscDanych(frekwencja)
        modules.sprawdzPoprawnoscDanych(opis)


        # zapisywanie wydarzeń do raportu
        if allWydarzen != 1:
            raport.write(str(licznik) + "\n")
        raport.write("Tytuł i organizatorzy:\n" + nazwa + " \n")
        raport.write("Link:\n" + wydarzenie + "\n")
        raport.write("Data:\n" + czasWydarzenia + " \n")
        raport.write("Miejsce:\n" + miejsce + "\n")
        raport.write("Frekwencja:\n" + frekwencja + "\n")
        raport.write("Opis:\n" + opis)
        raport.write(
            "\n------------------------------------------------------------------------------------------\n\n")
        time.sleep(7)
        print("Zgranych wydarzeń: " + str(licznik) + "/" + str(allWydarzen))
        licznik += 1

    modules.zamknijPlikRaportu(raport)
    browser.close()
    print("\nProgram zakończył pracę\n")
    print("Zgranych wydarzeń: " + str(licznik - 1) + "/" + str(allWydarzen))
    os.system("notepad raport.txt")
