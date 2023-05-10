######################################################################
# Tekijä: Severi Salonen
######################################################################
# Tehtävä HarjoitusTyö.py
# HTTavoiteKirjasto.py
########################################### kirjastot, erotin ja luokat
import sys
import datetime
import numpy

EROTIN = ";"

class TIEDOT:
    aikaleima = ""
    opiskelija = ""
    nro = ""

class LUVUT:
    nimi = ""
    lkm = 0

class TULOS:
    keskiarvo = 0
    Plkm = 0
    Tlkm = 0
    Ppienin = 0
    Psuurin = 0
    Npienin = ""
    Nsuurin = ""
########################################################## tiedoston "palautukset15.txt" luku
def LueTiedosto(Nimi, Lista):
    Lista.clear()
    try:
        Tiedosto = open(Nimi, "r")
        Rivi = Tiedosto.readline()
        while (True):
            Rivi = Tiedosto.readline()
            if (len(Rivi) == 0):
                break
            sarake = Rivi[:-1].split(EROTIN)
            tehtava = TIEDOT()
            tehtava.aikaleima = sarake[0]
            tehtava.opiskelija = sarake[1]
            tehtava.nro = sarake[2]
            Lista.append(tehtava)
        Tiedosto.close()
    except Exception:
        print(f"Tiedoston '{Nimi}' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    print(f"Tiedostosta '{Nimi}' luettiin listaan {len(Lista)} datarivin tiedot.")
    return Lista
########################################################## perustason analyysi ja tallennus
def Analyysi(Lista, Lista2):
    Lista2.clear()
    for alkio in Lista:
        tehtavat = alkio.nro
        Lista2.append(tehtavat)
    edellinen = Lista2[0]
    lkm = 0
    ListaLuvut = [] 
    for alkio in Lista2:
        if alkio == edellinen:
            lkm += 1
        else:
            tieto = LUVUT()
            tieto.lkm = int(lkm)
            tieto.nimi = edellinen
            ListaLuvut.append(tieto)
            lkm = 1
            edellinen = alkio
    tieto = LUVUT()
    tieto.lkm = int(lkm)
    tieto.nimi = edellinen
    ListaLuvut.append(tieto)
    return ListaLuvut

def Tilastot(Lista):
    palautuslkm = 0
    tehtavalkm = 0
    nimiSuurin = Lista[0].nimi
    nimiPienin = Lista[0].nimi
    palautusSuurin = int(Lista[0].lkm)
    palautusPienin = int(Lista[0].lkm)
    for alkio in Lista:
        
        x = int(alkio.lkm)
        palautuslkm += x
        tehtavalkm += 1
        
        if alkio.lkm < palautusPienin:
            palautusPienin = alkio.lkm
            nimiPienin = alkio.nimi
            
        if alkio.lkm > palautusSuurin:
            palautusSuurin = alkio.lkm
            nimiSuurin = alkio.nimi
            
    keskiarvo = int(palautuslkm/tehtavalkm)
    ListaVastaukset = []
    x = TULOS()
    x.keskiarvo = int(keskiarvo)
    x.Plkm = int(palautuslkm)
    x.Tlkm = int(tehtavalkm)
    x.Ppienin = int(palautusPienin)
    x.Psuurin = int(palautusSuurin)
    x.Npienin = nimiPienin
    x.Nsuurin = nimiSuurin
    ListaVastaukset.append(x)    
      
    print(f"Analysoitu {palautuslkm} palautusta {tehtavalkm} eri tehtävään.")
    print("Tilastotiedot analysoitu.")
    return ListaVastaukset
########################################################## tiedostoon kirjoittaminen
def KirjoitaTiedosto(Nimi, vastaukset, Lista):
    try:
        Tiedosto = open(Nimi, "w", encoding="utf-8")
        for olio in vastaukset:
            Tiedosto.write(f"Palautuksia tuli yhteensä {str(olio.Plkm)}, {str(olio.Tlkm)} eri tehtävään."+"\n")
            Tiedosto.write(f"Viikkotehtäviin tuli keskimäärin {olio.keskiarvo} palautusta."+"\n")
            Tiedosto.write(f"Eniten palautuksia, {str(olio.Psuurin)}, tuli viikkotehtävään {str(olio.Nsuurin)}."+"\n")
            Tiedosto.write(f"Vähiten palautuksia, {str(olio.Ppienin)}, tuli viikkotehtävään {str(olio.Npienin)}."+"\n")
        Tiedosto.write("\n")
        Tiedosto.write("Tehtävä;Lukumäärä"+"\n")
        for alkio in Lista:
            Tiedosto.write(f"{alkio.nimi};{alkio.lkm}"+"\n")
        Tiedosto.close()
        Tiedosto = open(Nimi, "r", encoding="utf-8")
        while (True):
            Rivi = Tiedosto.readline()
            if (len(Rivi) == 0):
                break
            Rivi = Rivi[:-1]
            print(Rivi)
        Tiedosto.close()
    except Exception:
        print(f"Tiedoston '{Nimi}' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    print("Tulokset tallennettu tiedostoon", "'"+Nimi+"'.")
    return None
################################################################ pistemaaran analyysi ja tallennnus
def PistemaaraAnalyysi(Lista):
    ListaOpis = []
    for alkio in Lista:
        ListaOpis.append(alkio.opiskelija)
    ListaOpis.sort()
    edellinen = ListaOpis[0]
    lkm = 0
    pisteet = {} 
    for alkio in ListaOpis:
        if alkio == edellinen:
            lkm += 1
        else:
            Opiskelija = edellinen
            maara = int(lkm)
            pisteet[Opiskelija] = maara
            lkm = 1
            edellinen = alkio
    Opiskelija = edellinen
    maara = int(lkm)
    pisteet[Opiskelija] = maara

    lkm1 = 0
    vastaukset = {}
    for k in range(0,61):
        for i in pisteet:
            if pisteet[i] == k:
                lkm1 += 1
        vastaukset[k] = lkm1
        lkm1 = 0
    print("Tehtäväkohtaiset pisteet analysoitu.")
    return vastaukset

def PistemaaraTallennus(Nimi, sanakirja):
    try:
        Tiedosto = open(Nimi, "w", encoding="utf-8")
        Tiedosto.write("Pistemäärä;Opiskelijoita"+"\n")
        for alkio in sanakirja:
            Tiedosto.write(f"{alkio};{sanakirja[alkio]}" + "\n")
        Tiedosto.close()
    except Exception:
        print(f"Tiedoston '{Nimi}' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)  
    print(f"Tulokset tallennettu tiedostoon '{Nimi}'.")
    return None
################################################################## matriisi1 analyysi ja tallennnus
def TuntiAnalyysi(Lista, matriisi):   
    for alkio in Lista:
        tunti = datetime.datetime.strptime(alkio.aikaleima, "%d-%m-%Y %H:%M:%S")
        tunti = int(tunti.hour)
        viikko = int((alkio.nro[1:3]))
        matriisi[viikko][tunti] += 1
    print("Tuntikohtaiset palautukset analysoitu.")
    return matriisi

def Matriisi1Tallennus(Nimi, matriisi):
    try:
        Tiedosto = open(Nimi, "w", encoding="utf-8")
        e = 0
        x=""
        teksti = 'Tunti'
        for hour in range(24):
            teksti += ";" + str(hour)
        Tiedosto.write(str(teksti)+ "\n")
        
        for alkio in range(1,15):
            e = alkio
            for alkio in range(24):
                x += ";" +str(matriisi[e][alkio])
            Tiedosto.write("Vko " + str(e) +str(x)+"\n")
            x = ""
        Tiedosto.close()
    except Exception:
        print(f"Tiedoston '{Nimi}' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    print(f"Tulokset tallennettu tiedostoon '{Nimi}'.")
    return None
#################################################################### matriisi2 analyysi ja tallennnus
def AikavaliAnalyysi(Lista, matriisi):
    palautusaika1 = datetime.datetime.strptime("1.9.2020 06:00", "%d.%m.%Y %H:%M")
    palautusaika7 = palautusaika1 + datetime.timedelta(weeks=+6)
    for alkio in Lista:
        viikko = int((alkio.nro[1:3]))
        paivat = datetime.datetime.strptime(alkio.aikaleima, "%d-%m-%Y %H:%M:%S")
        if viikko == 7:
            erotus = paivat - palautusaika7
            ero = int(erotus.days / 2)
        else:  
            erotus = paivat - palautusaika1
            ero = erotus.days % 7
        matriisi[viikko-1][ero] += 1
    print("Aikavälikohtaiset palautukset analysoitu.")
    return matriisi

def Matriisi2Tallennus(Nimi, matriisi):
    try:
        Tiedosto = open(Nimi, "w", encoding="utf-8")
        e = 0
        x=""
        palautusaika1 = datetime.datetime.strptime("1.9.2020 06:00", "%d.%m.%Y %H:%M")
        teksti = 'Aikaväli'
        for vali in range(7):
            nextdate = palautusaika1 + datetime.timedelta(days=+vali)
            teksti += ";" + str(nextdate.strftime("%a %H:%M"))
        Tiedosto.write(str(teksti)+"\n")
        
        for alkio in range(14):
            e = alkio
            for alkio in range(7):
                x += ";" +str(matriisi[e][alkio])
            Tiedosto.write("Vko " + str(e+1) + str(x)+"\n")
            x = ""
        Tiedosto.close()
    except Exception:
        print(f"Tiedoston '{Nimi}' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    print(f"Tulokset tallennettu tiedostoon '{Nimi}'.")
    return None
#eof
