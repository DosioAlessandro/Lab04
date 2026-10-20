class Stand:
    def __init__(self, codice, superficie, padiglione, prezzo_base):
        self.__codice = codice
        self.__superficie = superficie
        self.__padiglione = padiglione
        self.__prezzo_finale = float(prezzo_base)
        self.__espositore = None

    @property
    def codice(self):
        return self.__codice

    @property
    def espositore(self):
        return self.__espositore

    @espositore.setter
    def espositore(self, espositore):
        self.__espositore = espositore

    @property
    def prezzo_finale(self):
        return self.__prezzo_finale

    @prezzo_finale.setter
    def prezzo_finale(self, prezzo):
        self.__prezzo_finale = prezzo

    def libero_o_no(self):
        if self.__espositore is None:
            esp = "- Disponibile"
        else:
            esp = f"- Assegnato a: {self.__espositore}"
        return esp

    def descrizione_base(self):
        return f" | {self.__superficie} mq - Padiglione {self.__padiglione} - Prezzo"

    def __str__(self):
        return f"{self.__codice}: Standard {self.descrizione_base()} {self.__prezzo_finale} {self.libero_o_no()}"

class StandConPreseAggiuntive(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo_base, n_prese):
        super().__init__(codice, superficie, padiglione, prezzo_base)
        self.prezzo_finale = round(float(prezzo_base) * (1 + (0.07 * int(n_prese))), 2)
        self.__n_prese = n_prese

    def __str__(self):
        return f"{self.codice}: Prese extra {self.descrizione_base()} {self.prezzo_finale} - Prese aggiuntive: {self.__n_prese} {self.libero_o_no()}"


class StandPremium(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo_base, posizione):
        super().__init__(codice, superficie, padiglione, prezzo_base)
        self.prezzo_finale = round(float(prezzo_base) * 1.3, 2)
        self.__posizione = posizione

    def __str__(self):
        return f"{self.codice}: Premium {self.descrizione_base()} {self.prezzo_finale} - Posizione: {self.__posizione} {self.libero_o_no()}"

lista_stand = []