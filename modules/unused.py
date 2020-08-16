#Własne wyjątki:


# class ErrorLoginFbException(Exception):
#     """Obsługa błędu logowania do profilu fb"""
#     def __init__(self):
#         super().__init__("Błąd: Wystąpio niepowodzenie ładowania portalu facebook.com")
#         print("Błąd: Wystąpio niepowodzenie ładowania portalu facebook.com")
# class ErrorLoginOrPassFbException(Exception):
#     """Obsługa niepoprawnego loginu lub hasła do profilu fb"""
#     def __init__(self):
#         super().__init__("Błąd: Login lub hasło do profilu są błędne. Sprawdź dane logowania")
#         print("Błąd: Login lub hasło do profilu są błędne. Sprawdź dane logowania")
#
# #Funkcje
#
# def pobierzDaneLogowania(credential):
#     cred = []
#     if os.path.isfile('config\\credentials.txt'):
#         with open('config\\credentials.txt', 'r', encoding= "utf-8") as zawartosc:
#             for linia in zawartosc:
#                 linia = linia.replace("\n", "")
#                 linia = linia.replace("\r", "")
#                 cred.append(linia)
#     else:
#         print("Plik z danymi logowania nie istnieje!!!")
#         print("\nW folerze o nazwie \"config\" powinien się znajdowac plik txt o nazwie \"credentials.txt\",")
#         print("\nz zawartoscia twojego loginu i hasla do konta facebook.")
#         terminate()
#     if len(cred) < 2:
#         print("W pliku credentials.txt brak jest danych logowania do portalu fb, lub sa niepoprawnie wpisane.")
#         terminate()
#     if credential == 'login':
#         return cred[0]
#     elif credential == 'password':
#         return cred[1]
#
# def logowanieDoProfilu(browser, timesleep = 8):
#     try:
#         browser.get('https://pl-pl.facebook.com/')
#         title = browser.title
#         if "Facebook – zaloguj się lub zarejestruj" != title:
#             raise ErrorLoginFbException
#         elif "Zaloguj się do Facebooka | Facebook" == title:
#             raise ErrorLoginOrPassFbException
#         emailElem = browser.find_element_by_id('email')
#         emailElem.send_keys(pobierzDaneLogowania(credential='login'))
#         passElem = browser.find_element_by_id('pass')
#         passElem.send_keys(pobierzDaneLogowania(credential='password'))
#         emailElem.submit()
#         time.sleep(timesleep)
#     except ErrorLoginFbException:
#         terminate(browser)
#     except ErrorLoginOrPassFbException:
#         terminate(browser)
#     except WebDriverException:
#         print("Błąd: Wystąpio niepowodzenie ładowania strony facebook.com. Probem może tkwić w połączeniu z Internetem.\n"
#               "Sprawdz polaczenie lub sprobuj za chwile")
#         terminate(browser)
#     except Exception as e:
#         print("Wystąpil blad: ", e)
#         terminate(browser)
#     else:
#         print("Poprawnie zalogowano do profilu\nPracuje...\n")
