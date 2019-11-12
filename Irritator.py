# v 0.9
# created by Kamil Kołodziejczyk

from sys import path
from modules import modules, menu, engine
from selenium.common.exceptions import InvalidArgumentException
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

path.append('..\\modules')
path.append('..\\config')

listaWydarzen = []
optionsList = [1,2,3,8,9,0]
flag = True

menu.wyswietlWstep()

while flag:
    menu.wyswietlMenuGlowne()
    try:
        p = int(input("--> "))
    except Exception:
        exit()

    if p not in optionsList:
        print("No akurat takej opcji to nie mam!")
        exit()

    if p == 1: # full download
        modules.pobierzDaneZPliku(listaWydarzen) #pobranie zawartosci pliku wejsciowego do listy wydarzen
        allWydarzen = len(listaWydarzen) #Utworzenie licznika wydarzeń
        licznik = 1
        browser = webdriver.Firefox()
        engine.downloadEvent(browser, listaWydarzen, licznik, allWydarzen)
        input("\nWcisnij Enter aby kontynuowac...\n")

    elif p == 2: #one-time download for one event
        event = str(input("Wklej adres url wydarzenia: \n"))
        try:
            assert len(event) > 24
            l = []
            listaWydarzen = l[:]
            listaWydarzen.append(event)
            print("Mam! Czekaj!")
            browser = webdriver.Firefox()
            engine.downloadEvent(browser, listaWydarzen)
            input("\nWcisnij Enter aby kontynuowac...\n")
        except InvalidArgumentException:
            browser.close()
            print("Bład!!! Wprowadzony adres url jest nieprawidlowy. Sprawdz jego porawnosc i sprobuj jeszcze raz")
            input("\nWcisnij Enter aby kontynuowac...")
        except AssertionError:
            print("Wprowadzony adres url wydaje sie byc za krotki. Sprawdz jego porawnosc i sprobuj jeszcze raz")
            input("\nWcisnij Enter aby kontynuowac...")
    elif p == 3:
        modules.pobierzDaneZPliku(listaWydarzen)
        browser = webdriver.Firefox()
        modules.logowanieDoStrony(browser, timesleep = 3)
        for wydarzenie in listaWydarzen:
            browser.execute_script("window.open('{}')".format('{}'.format(wydarzenie)))
    elif p == 8:
        menu.firstUseInstruction()
        input("\nWcisnij Enter aby kontynuowac...")
    elif p == 9:
        menu.useInstruction()
        input("\nWcisnij Enter aby kontynuowac...")
    elif p == 0:
        menu.aboutIrritator()
        input("\nWcisnij Enter aby kontynuowac...")





