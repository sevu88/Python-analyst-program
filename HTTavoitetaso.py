######################################################################
# Tekijä: Severi Salonen
######################################################################
# Tehtävä HTavoitetaso.py

import HTTavoiteKirjasto
import numpy

def Valikko():
    print("Mitä haluat tehdä:")
    print("1) Lue tiedosto")
    print("2) Analysoi palautukset")
    print("3) Tallenna tulokset")
    print("4) Analysoi opiskelijoiden palautusmäärät")
    print("5) Analysoi tuntikohtaiset palautukset")
    print("6) Analysoi aikavälien palautukset")
    print("0) Lopeta")
    Valinta = int(input("Valintasi: "))
    return Valinta

def paaohjelma():
    ListaLue = []
    ListaTulos = []
    matriisi1 = numpy.zeros((15,25), int)
    matriisi2 = numpy.zeros((14,7), int)

    while (True):

        Valinta = Valikko()

        if (Valinta == 1):
            TiedostoLue = input("Anna luettavan tiedoston nimi: ") # "palautukset15.txt"
            ListaTiedot = HTTavoiteKirjasto.LueTiedosto(TiedostoLue, ListaLue)
            
        elif (Valinta == 2):
            if len(ListaLue) == 0:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")
            else:
                ListaLuvut = HTTavoiteKirjasto.Analyysi(ListaLue, ListaTulos)
                ListaVastaukset = HTTavoiteKirjasto.Tilastot(ListaLuvut)
            
        elif (Valinta == 3):
            if len(ListaTulos) == 0:
                print("Ei tietoja tallennettavaksi, analysoi tiedot ennen tallennusta.")
            else:
                TiedostoKirjoita = input("Anna kirjoitettavan tiedoston nimi: ") # "tulos15.txt"
                HTTavoiteKirjasto.KirjoitaTiedosto(TiedostoKirjoita, ListaVastaukset, ListaLuvut)

        elif (Valinta == 4):
            if len(ListaLue) == 0:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")
            else:
                pisteet = HTTavoiteKirjasto.PistemaaraAnalyysi(ListaLue)
                TiedostoLue1 = input("Anna kirjoitettavan tiedoston nimi: ") # "tulos15_pisteet.txt"
                HTTavoiteKirjasto.PistemaaraTallennus(TiedostoLue1, pisteet)

        elif (Valinta == 5):
            if len(ListaLue) == 0:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")
            else:
                tunnit = HTTavoiteKirjasto.TuntiAnalyysi(ListaLue, matriisi1)
                TiedostoLue2 = input("Anna kirjoitettavan tiedoston nimi: ") # "tulos15_tunnit.txt"
                HTTavoiteKirjasto.Matriisi1Tallennus(TiedostoLue2, tunnit)
                matriisi1 = numpy.zeros((15,25), int)

        elif (Valinta == 6):
            if len(ListaLue) == 0:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")
            else:
                vali = HTTavoiteKirjasto.AikavaliAnalyysi(ListaLue, matriisi2)
                TiedostoLue3 = input("Anna kirjoitettavan tiedoston nimi: ") # "tulos15_aikavalit.txt"
                HTTavoiteKirjasto.Matriisi2Tallennus(TiedostoLue3, vali)
                matriisi2 = numpy.zeros((14,7), int)

        elif (Valinta == 0):
            ListaLue.clear()
            ListaTulos.clear()
            matriisi1 = numpy.delete(matriisi1, numpy.s_[:], None)
            matriisi2 = numpy.delete(matriisi2, numpy.s_[:], None)
            print("Kiitos ohjelman käytöstä.")
            break
        
        else:
            print("Tuntematon valinta, yritä uudestaan.")
            
        print()
        print("Anna uusi valinta.")
        
    return None

paaohjelma()
#eof

# eof
