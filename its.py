class persona:
    def __init__(self, nome, cognome):
        self._nome = nome
        self._cognome = cognome

class docente(persona):
    def __init__(self, nome, cognome, materia, titolo):
        super().__init__(nome, cognome)
        self._materia = materia
        self._titolo= titolo
        self._corsi= []
    def __repr__(self):
        return f"Insegnante: {self._nome} {self._cognome}, materia: {self._materia}, titolo: {self._titolo}"
    

class allievo(persona):
    def __init__(self, nome, cognome):
        super().__init__(nome, cognome)
        self._corso= None
        self._orePresenza = 0
    def __repr__(self):
        return f"{self._cognome} {self._nome}"

class tutor(persona):
    def __init__(self, nome, cognome, corso):
        super().__init__(nome, cognome)
        self._corso = corso
        self._registro = []
    def appendToRegistro(self, allievo):
        self._registro.append(allievo)
    def __repr__(self):
        return f"{self._cognome} {self._nome}"

class corso:
    def __init__(self, dicitura, edizione, dataInizio):
        self._dicitura = dicitura
        self._edizione = edizione
        self._dataInizio = dataInizio
    def __repr__(self):
        return f"Corso: {self._dicitura}, edizione: {self._edizione}, data inizio: {self._dataInizio}"

def main():

    program = corso('Cyber Defence & System Administrator', '2025-2027', '24/11/2025')
    insegnante = docente('Andrea', 'Ribuoli', 'Basi Programmazione', 'ingegnere informatico')
    tu = tutor('Cecilia', 'Giacchella', program)
    dati_allievi = [
    ("Giovanni", "Artibani"), ("Marco", "Betti"), ("Tommaso", "Bravi"),
    ("Giampaolo", "Buzzi"), ("Maxim", "Cognigni"), ("Serena", "Di Gianvito"),
    ("Mirko", "Fabbrizi"), ("Monica", "Fiocchi"), ("Daniele", "Gagliardi"),
    ("Matteo", "Galeazzi"), ("Alessio", "Gennari"), ("Dulnath Nethdula", "Jayawardana"),
    ("Adam", "Madih"), ("Federico", "Perotti"),
    ("Giacomo Maria", "Piersantini"), ("Federico", "Pruccoli"), ("Alessandro", "Rastelli"),
    ("Tomas", "Santi"), ("Gianluca", "Taddei"), ("Raffaele", "Tesei"),
    ("Nicola", "Verdini"), ("Ayoub", "Ben Hassen"), ("Emanuele", "Senesi")]
    for nome, cognome in dati_allievi:
        nuovo_allievo = allievo(nome, cognome)
        tu.appendToRegistro(nuovo_allievo)

    print("--- RIEPILOGO CORSO ---")
    print(program)
    print(insegnante)
    print(f"tutor: {tu}")
    print(f"\n--- STUDENTI ISCRITTI ({len(tu._registro)} in totale) ---")

    formato = "%2d %-15s %-15s"
    print(formato % (0, "COGNOME", "NOME"))
    print("-" * 45)

    for i,s in enumerate(tu._registro, 1):
        print (formato % (i, s._cognome, s._nome))

if __name__ == "__main__":    main()








