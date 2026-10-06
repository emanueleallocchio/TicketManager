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


def leggi_ticket_filtrati(titolo, priorita, stato):
      conn=sqlite3.connect("ticket_manager.db")
      cursor = conn.cursor()

      query = """
        SELECT id, titolo, descrizione, priorita, categoria, stato_aperto
        FROM tickets
        WHERE 1=1
        """

      parametri = []

      if titolo.strip() != "":
           query += "AND titolo = ?"
           parametri.append(titolo)

      if priorita != "Tutte":
            query += "AND priorita = ?"
            parametri.append(priorita)

      
      if stato != "Tutti":

        query += "AND stato_aperto = ?"
        
        if stato == "Aperto":             
             parametri.append(1)
        else:
             parametri.append(0)

      cursor.execute(query, parametri)
      
      tickets = cursor.fetchall()
      
      conn.close()
      
      return tickets






      

    