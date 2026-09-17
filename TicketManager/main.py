import tkinter as tk
from ticket import Ticket
from database import crea_database, inserisci_ticket

crea_database()

root = tk.Tk() #Crea l'oggetto root della classe tk (finestra vuota grigia)

root.title("Ticket Manager by Lele") #Inserisce il titolo in alto nella finestra

root.geometry("800x500") #Stabilisce le dimensioni della finestra

def apri_finestra_ticket():

    def salva_ticket():
            titolo = titolo_entry.get()
            descrizione = descrizione_entry.get()
            priorita = priorita_var.get()
            categoria = categoria_var.get()
            stato_aperto = stato_var.get()
            inserisci_ticket(
                titolo, 
                descrizione, 
                priorita, 
                categoria, 
                stato_aperto            
        )
            print("Salvato nel database")

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
    width=20
)

view_tickets_button.pack(pady=10)

root.mainloop() #Mantiene il programma attivo
