def wyswietlWstep():
    print("Witaj w programie Irritator v. 0.8.3")
    print("Autorem programu jest: Kamil Kolodziejczyk")
    print("Program sluży do tworzenia raportów wydarzeń publikowanych w portalu facebook.com\n")

def wyswietlMenuGlowne():
    print("Wciśnij klawisz w celu wyboru funkcji programu: \n")
    print("1 - Generuj raport dla wszystkich wydarzeń")
    print("2 - Generuj raport dla pojedynczego wyarzenia")
    print("3 - Wyświetl instrukcje przed pierwszym uruchomieniem programu")
    print("4 - Wyświetl instrukcje obsługi programu")
    print("5 - O programie")
    print("Każda inna opcja zakończy pracę programu")

def firstUseInstruction():
    print("Program wspołpracuje jedynie z przeglądarkami Mozilla Firefox w dowlonej wersji jednak do jego poprawnego\n"
          "dzialania niezbedne jest pobranie sterownika: geckodriver.exe, a nastepnie umieszczenie go w glownym\n"
          "folderze z programem. Mozna go pobrac ze strony: https://github.com/mozilla/geckodriver/releases.\n"
          "Przed pobraniem sprawdz czy sterownik juz nie znajduje sie w folderze")
    print("W kolejnym kroku niezbedne jest abys w folderze config odnalazl plik o nazwie credentials.txt. Otworz go,\n"
          "a nastepnie wpisz w nim KOLEJNO:\n"
          "\t- w pierwszej linii swoj login jakim logujesz się do swojego konta w portalu facebook.com\n"
          "\t- w drugiej hasło jakiego używasz\n"
          "Wazne zebyś nie uzywał zadnych białych znaków. W pliku mają się znajdować jedynie hasło i login.\n"
          "Zapisz zmiany i zaminij plik.")
    print("Konfiguracje ta wykonujesz tylko raz przed pierwszym uruchomieniem programu.")
    print("Wykonaj powyzsze instrukcje i uruchom ponownie program.")

def useInstruction():
    print("Dzialanie programu jest banalnie proste. Wyszukujesz wydarzenia w portalu facebook.com. Kopiujesz adresu url\n"
          "wydarzen, a nastepnie wklejasz je kolejno do pliku tekstowego \"linki_wydarzen.txt\". Kolejne wydarzenia\n"
          "musza byc oddzielone od siebie enterem. W pliku tym mozesz w OSOBNYCH liniach dodawać notatki do 24 znaków\n"
          "ktore nie beda brane pod uwagę przez aplikacje")
    print("Po skopiowaniu wszystkich wydarzen pozostajacych w zainteresowaniu do ww. pliku mozesz uruchomic program\n"
          "z opcja \"1\". Zostanie wyenerowany raport dla wszystkich wydarzen z poprzedniego pliku")
    print("W trkcie jego pracy nic nie rob. Ignoruj wszystkie wyskakujace okna. Cierpliwie czekaj na zakonczenie\n"
          "jego działania.")
    print("W efekcie w pliku o nazwie; \"raport.txt\" zostanie wygenerowany raport dla wszystkich wydarzen.\n")
    print("Program jest w fazie beta wiec po zakonczeniu jego działania koniecznie zweryfikuj czy wszystkie pola\n"
          "sa poprawie wypelnione\n\n")
    print("Jezeli chcesz wygenerowac raport dla pojedynczego wydarzenia wybierz opcje \"2\". program poprosi\n"
          "o wklejenie linku do wydarzenia w okno konsoli. Nastepnie wygeneruje raport w tym samym pliku.")
    print("UWAGA!!! Aplikacja nadpisze poprzedni raport!!!")

def aboutIrritator():
    print("Program Irritator powstal w celu wsparcia pracy funkcjonariuszy Wydzialu dw. z Cyberprzestepczoscia.")
    print("Jego dzialanie pozwala na skrocenie czasu oraz zmudnosci trwania bialych wywiadow.")
    print("Jezeli chcesz sie skontaktowac z jego autorem w celu zgloszenia bledow lub masz pomysl jak usprawnic\n"
              "program pisz na adres mailowy zaurish@vp.pl")
    print("W przyszlosci planowane jest wdrozenie nowych funkcji. W nastepnej wersji powinny pojawic sie dane\n"
              "miejsca, gdzie szukac bedzie mozna najnowszych jego wydan.\n"
              "Zycze bezproblemowej pracy z programem.")
    print("mł. asp. Kamil Kolodziejczyk")