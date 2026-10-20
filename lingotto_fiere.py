import csv
import espositori
import stand
from operator import attrgetter

espositori_stand = {}

class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        with open(file_path, "r") as file:
            file_dati = csv.reader(file)
            for i in file_dati:
                if i[0][0] == "E":
                    e = espositori.Espositori(i[0], i[1], i[2])
                    espositori.lista_espositori.append(e)
                elif i[0][0] == "S":
                    try:
                        if i[4].isdigit():
                            s = stand.StandConPreseAggiuntive(i[0], i[1], i[2], i[3], i[4])
                        elif not i[4].isdigit():
                            s = stand.StandPremium(i[0], i[1], i[2], i[3], i[4])
                    except IndexError:
                        s = stand.Stand(i[0], i[1], i[2], i[3])
                    stand.lista_stand.append(s)

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        stand_trovato = False
        for i in stand.lista_stand:
            if i.codice == codice_stand:
                stand_trovato = True
                s = i
        if not stand_trovato:
            print("Non esiste uno stand con questo codice")
            raise Exception
        espositore_trovato = False
        for i in espositori.lista_espositori:
            if i.codice == codice_espositore:
                espositore_trovato = True
        if not espositore_trovato:
            print("Non esiste un espositore con questo codice")
            raise Exception
        for i in espositori_stand:
            if i == codice_espositore or espositori_stand[i] == codice_stand:
                raise Exception
        espositori_stand[codice_espositore] = codice_stand
        s.espositore = codice_espositore

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        for i in espositori.lista_espositori:
            print(f"\n{i}", end="")
            if i.codice in espositori_stand:
                print(f"| stand: {espositori_stand[i.codice]}", end="")
        print()

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        stand_ordinati = sorted(stand.lista_stand, key=attrgetter("prezzo_finale"))
        return stand_ordinati
