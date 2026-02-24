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

class allievo(persona):
    def __init__(self, nome, cognome):
        super().__init__(nome, cognome)
        self._corso= None
        self._orePresenza = 0

class tutor(persona):
    def __init__(self, nome, cognome, corso):
        super().__init__(nome, cognome)
        self._corso = corso
        self._registro = []
    def appendToRegistro(self, allievo):
        self._registro.append(allievo)

class corso:
    def __init__(self, dicitura, edizione, dataInizio):
        self._dicitura = dicitura
        self._edizione = edizione
        self._dataInizio = dataInizio

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
    print(f"Corso: {program._dicitura}, edizione: {program._edizione}, data inizio: {program._dataInizio}")
    print(f"Insegnante: {insegnante._nome} {insegnante._cognome}, materia: {insegnante._materia}, titolo: {insegnante._titolo}")
    print(f"tutor: {tu._nome} {tu._cognome}")
    print(f"\n--- STUDENTI ISCRITTI ({len(tu._registro)} in totale) ---")
    for i,s in enumerate(tu._registro, 1):
        print (f"{i}. {s._nome} {s._cognome}")
        
if __name__ == "__main__":    main()








