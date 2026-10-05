import tkinter as tk
from tkinter import messagebox, ttk
from ticket import Ticket
from database import crea_database, inserisci_ticket, salva_ticket, leggi_ticket

crea_database()

root = tk.Tk() #Crea l'oggetto root della classe tk (finestra vuota grigia)

root.title("Ticket Manager by Emanuele Allocchio") #Inserisce il titolo in alto nella finestra

root.geometry("800x500") #Stabilisce le dimensioni della finestra

def apri_finestra_ticket():

    
    def salva_ticket():
            titolo = titolo_entry.get()
            descrizione = descrizione_entry.get()
            priorita = priorita_var.get()
            categoria = categoria_var.get()
            stato_aperto = stato_var.get()

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
                stato_aperto            
        )
            messagebox.showinfo(
                  "Corretto",
                  "Inserito nel database"
            )
            titolo_entry.delete(0, tk.END)
            descrizione_entry.delete(0, tk.END)
            priorita_var.set("Scegli")
            categoria_var.set("Scegli")
            stato_var.set(True)

  

    finestra_ticket = tk.Toplevel(root)



    finestra_ticket.title("Crea Ticket")
    finestra_ticket.geometry("500x600")

    titolo_label = tk.Label(finestra_ticket, text="Titolo")
    titolo_label.pack(pady=(20, 5))

    titolo_entry = tk.Entry(finestra_ticket, width=40)
    titolo_entry.pack()

    descrizione_label = tk.Label(finestra_ticket, text="Descrizione")
    descrizione_label.pack(pady=(15, 5))

    descrizione_entry = tk.Entry(finestra_ticket, width=40)
    descrizione_entry.pack()

    priorità_label = tk.Label(finestra_ticket, text="Priorità")
    priorità_label.pack(pady=(15, 5))

    priorita_var = tk.StringVar()
    priorita_var.set("Scegli")

    priorita = [
        "Alta",
        "Normale",
        "Bassa"
    ]

    priorita_menu = tk.OptionMenu(
        finestra_ticket, 
        priorita_var,
        *priorita
    )

    priorita_menu.pack()

    #Definizione delle categorie selezionabili dentro il menu a tendina

    categorie = [
        "Hardware",
        "Software",
        "Rete",
        "Account/Accessi",
        "Altro"

    ]

    categoria_label = tk.Label(finestra_ticket, text="Categoria")
    categoria_label.pack(pady=(15, 5))

    #Creazione della stringa per la categoria scelta e la si imposta ad un valore di default

    categoria_var = tk.StringVar()
    categoria_var.set("Scegli")

    #Creazione del menu a tendina della categoria

    categoria_menu = tk.OptionMenu(
        finestra_ticket,
        categoria_var,
        *categorie
    )

    categoria_menu.pack()

    stato_var = tk.BooleanVar(value=True)

    stato_check = tk.Checkbutton(
        finestra_ticket,
        text="Ticket aperto",
        variable = stato_var
    )

    stato_check.pack(pady=(15, 5))

    create_ticket = tk.Button(
        finestra_ticket,
        text="Crea",
        font=("Arial", 14),
        width=20,
        command=salva_ticket
    )

    create_ticket.pack(pady=10)

def apri_finestra_visualizza_ticket():
      finestra_visualizza = tk.Toplevel(root)

      finestra_visualizza.geometry("1000x500")

      colonne = (
            "id",
            "titolo",
            "descrizione",
            "priorita",
            "categoria",
            "stato"
      )

      tabella = ttk.Treeview(
            finestra_visualizza,
            columns=  colonne,
            show="headings"
      )

      tabella.heading("id", text="ID")
      tabella.heading("titolo", text="Titolo")
      tabella.heading("descrizione", text="Descrizione")
      tabella.heading("priorita", text="Priorità")
      tabella.heading("categoria", text="Categoria")
      tabella.heading("stato", text="Stato")

      tabella.column("id", width=50, anchor="center")
      tabella.column("titolo", width=150)

      tabella.tag_configure("aperto", background="lightgreen")
      tabella.tag_configure("chiuso", background="lightcoral")



      tabella.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20

      )

      tickets = leggi_ticket()

      for ticket in tickets:
            if ticket[5]:
                  stato="Aperto"
                  tag_stato="aperto"
            else:
                  stato="Chiuso"
                  tag_stato="chiuso"

            tabella.insert(
                  "",
                  tk.END,
                  values=(
                        ticket[0],  #ID
                        ticket[1],  #Titolo
                        ticket[2],  #Descrizione
                        ticket[3],  #Priorità
                        ticket[4],  #Categoria
                        stato
                  ),
                  tags=(tag_stato,)
            )





#Crea l'oggeto title_lable dalla classe tk.Label (testo)

title_label = tk.Label( 
    root,
    text="Ticket Manager",
    font=("Arial", 22, "bold")
)

title_label.pack(pady=30) #La rende visibile e assegna l'interlinea sopra e sotto

#Crea l'oggeto create_ticket_button dalla classe tk.Label (testo)

create_ticket_button = tk.Button( 
    root,
    text="Crea Ticket",
    font=("Arial", 14),
    width=20,
    command=apri_finestra_ticket
)

create_ticket_button.pack(pady=10)

view_tickets_button = tk.Button(
    root,
    text="Visualizza Ticket",
    font=("Arial", 14),
    width=20,
    command=apri_finestra_visualizza_ticket
)

view_tickets_button.pack(pady=10)

root.mainloop() #Mantiene il programma attivo
