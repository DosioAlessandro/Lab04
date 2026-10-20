class Espositori:
    def __init__(self, codice, nome, cognome):
        self.__codice = codice
        self.__nome = nome
        self.__cognome = cognome

    @property
    def codice(self):
        return self.__codice

    def __str__(self):
        return f"{self.__nome} {self.__cognome} ({self.__codice})"

lista_espositori = []