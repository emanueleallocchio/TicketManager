import sqlite3
from tkinter import messagebox
import tkinter as tk

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


def leggi_ticket():
    conn = sqlite3.connect("ticket_manager.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, titolo, descrizione, priorita, categoria, stato_aperto
        FROM tickets
     """)

    tickets=cursor.fetchall()

    conn.close()

    return tickets




def salva_ticket(titolo, descrizione, priorita, categoria, stato):
            

            if (
                  titolo.strip() == ""
                  or descrizione.strip() == ""
                  or priorita=="Scegli"
                  or categoria=="Scegli"
            ):
                  
                  messagebox.showerror(
                        "Errore",
                        "Compila tutti i campi per inserire il ticket"
                  )
                  return
                             
            inserisci_ticket(
                titolo, 
                descrizione, 
                priorita, 
                categoria, 
                stato            
        )
            messagebox.showinfo(
                  "Corretto",
                  "Inserito nel database"
            )
            titolo.delete(0, tk.END)
            descrizione.delete(0, tk.END)
            priorita.set("Scegli")
            categoria.set("Scegli")
            stato.set(True)

    