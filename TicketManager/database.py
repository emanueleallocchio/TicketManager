import sqlite3

def crea_database():
    conn = sqlite3.connect("ticket_manager.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titolo TEXT NOT NULL,
            descrizione TEXT,
            priorita TEXT,
            categoria TEXT,
            stato_aperto INTEGER
        
        )
    """)
    conn.commit()
    conn.close()

def inserisci_ticket(titolo, descrizione, priorita, categoria, stato_aperto):
    conn = sqlite3.connect("ticket_manager.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO tickets (
        titolo,
        descrizione,
        priorita,
        categoria,
        stato_aperto
        )
        VALUES(?, ?, ?, ?, ?)
    """, (
        titolo,
        descrizione,
        priorita,
        categoria,
        stato_aperto

    ))
    conn.commit()
    conn.close()
    