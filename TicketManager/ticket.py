class Ticket:
    ultimo_id = 0

    def __init__(self, titolo, descrizione, priorita, categoria, stato_aperto=True):
        Ticket.ultimo_id += 1

        self.id = Ticket.ultimo_id
        self.titolo = titolo
        self. descrizione = descrizione
        self.priorita = priorita
        self.categoria = categoria
        self.stato_aperto = stato_aperto