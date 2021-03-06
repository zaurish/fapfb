import os, time
from selenium.common.exceptions import WebDriverException, NoSuchElementException

#Własne wyjątki:

class ErrorDownloadElement(Exception):
    """Obsługa błędu związanego z pobraniem pstego elementu wydarzenia"""
    def __init__(self, x = 'elementu'):
        super().__init__("Błąd nie pobrano " + x + " wydarzenia")
        print("Błąd nie pobrano " + x + " wydarzenia. Ponawianie próby ...")

#Funkcje:
def terminate(browser = 0):
    if browser != 0:
        browser.close()
    input("\nNaciśnij dowolny przycisk aby zakończyć pracę programu...")
    exit()

def otworzPlikRaportu():
    try:
        raport = open('raport.txt', 'w', encoding="utf-8")
        return raport
    except Exception as e:
        print("Wystąpił nieoczekiwany błąd w trakcie tworzenia pliku raportu: ", e)
        print("\nProgram nie będzie poprawnie działał...")
        print("\nSprobuj uruchomić go ponownie, jezeli problem sie powtorzy skontaktuj sie z twórcą.")
        terminate()

def zamknijPlikRaportu(raport):
    try:
        raport.close()
        print("Plik raportu został prawidłowo zamknięty.")
    except Exception as e:
        print("Wystąpił nieoczekiwany błąd w trakcie zamykania pliku raportu: ", e)
        print("\nNiektore dane mogly nie zostac prawidlowo zapisane.")
        print("\nUpewnij się przed publikacją raportu o jego aktualnosci.")

def pobierzLinkiWydarzen(listaWydarzen):
    if os.path.isfile('linki_wydarzen.txt'):
        with open('linki_wydarzen.txt', 'r', encoding = "utf-8") as zawartosc:
            for linia in zawartosc:
                linia = linia.replace("\n", "") #usuwa znaki konca linii
                linia = linia.replace("\r", "") #usuwa znaki konca linii
                if len(linia) < 24: #jezeli linia pusta to pomija
                    continue
                listaWydarzen.append(linia)
    else:
        print("Plik z danymi wejściowymi nie istnieje!!!")
        print("\nByc moze znajduje sie on w blednej lokalizacji lub zostal usuniety")
        terminate()
    if len(listaWydarzen) == 0: #jezeli lista jest pusta zakoncz działanie programu
        print("Plik wejsciowy nie zawiera linków wydarzen")
        terminate()
    else:
        return listaWydarzen
    return listaWydarzen

def pobierzTytulOrganizatorzy(browser):
    info = 'Brak nazwy wydarzenia oraz informacji o organizatorach'
    komunikat = "\nRaport zostanie wygenerowany, jednak w miejscu tytulu dla tego wydarzenia\n" \
            "pojawi sie informacja o jego braku. Mozesz sprobowac go wpisac recznie przed publikacja raportu"
    try:
       tytul = browser.find_element_by_class_name("_5gmx")
       tytul = tytul.text
       if tytul == '': #jezeli tytuł jest pusty wywołuje wyjatek
          raise ErrorDownloadElement(x = 'tytuł i organzatorzy')
    except NoSuchElementException:
        print("Nie zaleziono nazwy wydarzenia na stronie!\n Sprawdź czy opis istnieje!")
        print(komunikat)
        return info
    except ErrorDownloadElement:
        browser.refresh()
        time.sleep(7)
        tytul = browser.find_element_by_class_name("_5gmx")
    except Exception as e:
        print("Wystąpil blad: ", e)
        print(komunikat)
        return info
    return tytul

def pobierzDataCzasMiejsce(browser, temp):
    info = 'Brak informacji'
    komunikat = "\nRaport zostanie wygenerowany, jednak w raporcie zostanie zawarta inforamcja o braku miejsca\n" \
                "lub czasu dla tego wydarzenia. Mozesz sprobowac go wpisac recznie przed publikacja raportu"
    try:
        ids = browser.find_elements_by_class_name('_xkh')  # pobiera wszystkie elementy do listy z klasy
        # print(len(ids))
        # print(ids[0].text)
        # print(ids[1].text)
        if len(ids) != 2:
            raise ErrorDownloadElement()
        if temp == 'czas':
            i = ids[0].text
        elif temp == "miejsce":
            i = ids[1].text
        return i
    except NoSuchElementException:
        print("Nie zaleziono daty wydarzenia na stronie!\n Sprawdź czy ona istnieje!")
        print(komunikat)
        return info
    except ErrorDownloadElement:
        browser.refresh()
        time.sleep(7)
        ids = browser.find_elements_by_class_name('_xkh')
        try:
            if temp == 'czas':
                i = ids[0].text
            elif temp == "miejsce":
                i = ids[1].text
        except Exception as e:
            print(komunikat)
            return info
    except Exception as e:
        print("Wystąpil blad: ", e)
        print(komunikat)
        return info
    return i

def pobierzFrekwencja(browser):
    info = 'Brak informacji o frekwecji'
    komunikat = "\nRaport zostanie wygenerowany, jednak w raporcie zostanie zawarta inforamcja o braku frekwencji\n" \
                "dla tego wydarzenia. Mozesz sprobowac wpisac ja recznie przed publikacja raportu"
    try:
        frekwencja =  browser.find_element_by_class_name("_5z74")
        if frekwencja == '':
            raise ErrorDownloadElement(x = 'frekwencji')
    except NoSuchElementException:
        print("Nie znaleziono informacji o frekwencji na stronie!\n Sprawdź czy została ona podana!")
        print(komunikat)
        return info
    except ErrorDownloadElement:
        browser.refresh()
        time.sleep(7)
        frekwencja = browser.find_element_by_class_name("_5z74")
    except Exception as e:
        print("Wystąpil blad: ", e)
        print(komunikat)
        return info
    return frekwencja.text

def pobierzOpis(browser):
    info = 'Brak opisu wydarzenia'
    komunikat = "\nRaport zostanie wygenerowany, jednak w raporcie zostanie zawarta inforamcja o braku opisu\n" \
                "dla tego wydarzenia. Mozesz sprobowac wpisac go recznie przed publikacja raportu"
    try:
        opis = browser.find_element_by_class_name("_63ew")
        if opis == '':
            raise ErrorDownloadElement(x = 'opisu')
    except NoSuchElementException:
        print("Nie znaleziono opisu wydarzenia na stronie!\nSprawdź czy istnieje!")
        print(komunikat)
        return info
    except ErrorDownloadElement:
        browser.refresh()
        time.sleep(7)
        opis = browser.find_element_by_class_name("_63ew")
    except Exception as e:
        print("Wystąpil blad: ", e)
        print(komunikat)
    opis = opis.text
    opis = "".join([s for s in opis.splitlines(True) if s.strip()]) #usuniecie pustych linii z opisu
    return opis

def sprawdzPoprawnoscDanych(dana):
    x = 'Brak informacji'
    if dana == '':
        dana = x
        return dana

def pobierzCalaZawartoscPliku(nazwaPliku):
    with open(nazwaPliku, 'r', encoding = "utf-8") as obiektPliku:
        tresc = obiektPliku.read()
        return tresc