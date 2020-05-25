from modules import modules
listaKontaktow = []


def sendRaportWhatsApp():
    #browser.get("https://web.whatsapp.com/")
    modules.pobierzDaneZPliku(listaKontaktow)

    #msg = modules.pobierzCalaZawartoscPliku('raport.txt')
    for odbiorca in listaKontaktow:
        print(odbiorca)
        # user = browser.find_element_by_xpath('//span[@title = "{}"]'.format(odbiorca))
        # print("Wybrałem " + odbiorca)
        # user.click()
        # msg_box = browser.find_element_by_css_selector('._3u328')
        # msg_box.click()
        # msg_box.send_keys(msg)
        # button = browser.find_element_by_css_selector('._3M-N-')
        # button.click()
        # print("Zakończyłem wysyłanie")
