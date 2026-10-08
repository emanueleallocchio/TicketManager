import tkinter as tk
from tkinter import messagebox, ttk
from database import crea_database, inserisci_ticket, salva_ticket, leggi_ticket, leggi_ticket_filtrati, modifica_ticket

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

    finestra_ticket.transient(root)
    
    finestra_ticket.grab_set()
    
    
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

      finestra_visualizza.geometry("1300x500")

      finestra_visualizza.title("Visualizza Ticket")
      
      finestra_visualizza.transient(root)
      
      finestra_visualizza.grab_set()

      filtri_visibili = False

      frame_filtri = tk.Frame(finestra_visualizza)
      
      def mostra_filtri():
                        nonlocal filtri_visibili
            
                        if filtri_visibili:
                              frame_filtri.pack_forget()
                              filtri_visibili = False
                              mostra_filtri_button.config(text = "Mostra Filtri")
      
                        else:
                               frame_filtri.pack(pady=10, before= tabella, anchor="w")
                               filtri_visibili = True
                               mostra_filtri_button.config(text= "Nascondi Filtri")
                               
                        

      
      mostra_filtri_button = tk.Button(finestra_visualizza, text = "Mostra Filtri", command = mostra_filtri)

      mostra_filtri_button.pack(pady=10, anchor="w",padx=20, fill="x")



   

      


      filtra_label_titolo = tk.Label(
             
            frame_filtri,
            text="Titolo",
            font=("Arial", 10)
                  
                        )

      filtra_label_titolo.grid(
            row=0,
            column=0,
            padx=5,
            pady=5
      )

      titolo_filtro_entry = tk.Entry(frame_filtri, width=30)
      
      titolo_filtro_entry.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
             
      )

      priorita_filtro_var = tk.StringVar(value= "Tutte")

      filtra_label_priorita = tk.Label(
            frame_filtri,
            text="Priorità",
            font=("Arial", 10)
            
                  )
      filtra_label_priorita.grid(
             row=0,
             column=2,
             padx=5,
             pady=5
      )
      
      priorita_filtro_menu = tk.OptionMenu(
            frame_filtri,
            priorita_filtro_var,
            "Tutte",
            "Alta",
            "Media",
            "Bassa"
      )

      priorita_filtro_menu.grid(
             row=0,
             column=3,
             padx=5,
             pady=5
      )

      stato_filtro_var = tk.StringVar(value= "Tutti")

      filtra_label_stato = tk.Label(
            frame_filtri,
            text="Stato",
            font=("Arial", 10)
            
                  )
      
      filtra_label_stato.grid(
             row=0,
             column=4,
             padx=5,
             pady=5
      )

      stato_filtro_menu = tk.OptionMenu(
            frame_filtri,
            stato_filtro_var,
            "Tutti",
            "Aperto",
            "Chiuso"
      )

      stato_filtro_menu.grid(
             row=0,
             column=5,
             padx=5,
             pady=5
      )

      def applica_filtri():
            titolo = titolo_filtro_entry.get()
            priorita = priorita_filtro_var.get()
            stato = stato_filtro_var.get()

            tickets = leggi_ticket_filtrati(titolo, priorita, stato)

            for riga in tabella.get_children():
                  tabella.delete(riga)

            for ticket in tickets:
                  if ticket[5]:
                        stato_testo = "Aperto"
                        tag_stato = "aperto"
                  else:
                        stato_testo = "Chiuso"
                        tag_stato = "chiuso"

                  tabella.insert(
                        "",
                        tk.END,
                        values=(
                              ticket[0],
                              ticket[1],
                              ticket[2],
                              ticket[3],
                              ticket[4],
                              stato_testo,
                              "🖉"

                        ),
                        tags = (tag_stato,)
                  )
      
      
      

      filtra_button = tk.Button(
            frame_filtri,
            text="Filtra",
            command= applica_filtri
      )

      

      filtra_button.grid(
             row=0,
             column=7,
             padx=30,
             pady=10             
      )



      colonne = (
            "id",
            "titolo",
            "descrizione",
            "priorita",
            "categoria",
            "stato",
            "modifica"
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
      tabella.heading("modifica", text="")

      tabella.column("id", width=50, anchor="center")
      tabella.column("titolo", width=150)
      tabella.column("modifica", width=50, anchor="center")
      

      tabella.tag_configure("aperto", background="lightgreen")
      tabella.tag_configure("chiuso", background="lightcoral")



      tabella.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20

      )

      
      def stampa_ticket():
            for riga in tabella.get_children():
                    tabella.delete(riga)
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
                              stato,
                              "🖉"
                        
                        ),
                        tags=(tag_stato,)
            )
      stampa_ticket()

            

      def click_tabella(event):                       #Creiamo una funzione che verra chiamata da tabella.bind
             colonna = tabella.identify_column(event.x)
             riga = tabella.identify_row(event.y)
             dati = tabella.item(riga, "values")

             if colonna == "#7" and riga:
                  dati = tabella.item(riga, "values")
                  id = dati[0]
                  titolo = dati[1]
                  descrizione = dati[2]
                  priorita = dati[3]
                  categoria = dati[4]
                  stato = dati[5]
                          
                  finestra_modifica = tk.Toplevel(finestra_visualizza)
                  finestra_modifica.title("Modifica Ticket")
                  finestra_modifica.geometry("500x600")
                  finestra_modifica.transient(finestra_visualizza)
                  finestra_modifica.grab_set()

                  titolo_label = tk.Label(finestra_modifica, text="Titolo")
                  titolo_label.pack(pady=(20, 5))
                          
                  titolo_entry = tk.Entry(finestra_modifica, width=40)
                  titolo_entry.pack()
                          
                  descrizione_label = tk.Label(finestra_modifica, text="Descrizione")
                  descrizione_label.pack(pady=(15, 5))
                          
                  descrizione_entry = tk.Entry(finestra_modifica, width=40)
                  descrizione_entry.pack()
                          
                  priorità_label = tk.Label(finestra_modifica, text="Priorità")
                  priorità_label.pack(pady=(15, 5))
                          
                  priorita_var = tk.StringVar()
                  priorita_var.set(priorita)
                          
                  priorita_opzioni = [
                                  "Alta",
                                  "Normale",
                                  "Bassa"
                              ]
                          
                  priorita_menu = tk.OptionMenu(
                                  finestra_modifica, 
                                  priorita_var,
                                  *priorita_opzioni
                              )
                          
                  priorita_menu.pack()
                          
                              
                  categorie_opzioni = [
                                  "Hardware",
                                  "Software",
                                  "Rete",
                                  "Account/Accessi",
                                  "Altro"
                          
                              ]
                          
                  categoria_label = tk.Label(finestra_modifica, text="Categoria")
                              
                  categoria_label.pack(pady=(15, 5))
                          
                          
                          
                  categoria_var = tk.StringVar()
                  categoria_var.set(categoria)
                          
                          
                          
                  categoria_menu = tk.OptionMenu(
                                  finestra_modifica,
                                  categoria_var,
                                  *categorie_opzioni
                              )
                          
                  categoria_menu.pack()

                  stato_var = tk.BooleanVar(
                                 master=finestra_modifica,
                                 value=(stato == "Aperto")
                              )

                  finestra_modifica.stato_var = stato_var

                  stato_check = tk.Checkbutton(
                                    finestra_modifica,
                                    text="Ticket aperto",
                                    variable = finestra_modifica.stato_var
                              )

                                                    
                  if stato == "Aperto":
                              stato_var.set(True)
                  else:
                              stato_var.set(False)
                              
                          
                          
                          
                  stato_check.pack(pady=(15, 5))

                  titolo_entry.insert(0, titolo)
                  descrizione_entry.insert(0, descrizione)

                  

                  def salva_modifiche():
                          nuovo_titolo = titolo_entry.get()
                          nuova_descrizione = descrizione_entry.get()
                          nuova_priorita = priorita_var.get()
                          nuova_categoria = categoria_var.get()
                          nuovo_stato = finestra_modifica.stato_var.get()

                          

                          modifica_ticket(
                                  id,                                    
                                  nuovo_titolo,
                                  nuova_descrizione,
                                  nuova_priorita,
                                  nuova_categoria,
                                  nuovo_stato
                              
                          )
                          stampa_ticket(),
                          finestra_modifica.destroy()

                  salva_modifiche_button = tk.Button(
                          finestra_modifica,
                          text="Salva Modifiche",
                          command=salva_modifiche
                  )

                  salva_modifiche_button.pack(pady=10)





      def cambia_cursore(event):
                   
            colonna=tabella.identify_column(event.x)
            riga=tabella.identify_row(event.y)

            if colonna == "#7" and riga:
                          tabella.config(cursor="hand2")
            else:
                          tabella.config(cursor="")                  
      



      tabella.bind("<Button-1>", click_tabella) #tabella.bind crea un evento e.g. evento = Event() con tutte le informazioni dell'evento del click
                                                      #e poi esegue click_tabelle(evento)

      tabella.bind("<Motion>", cambia_cursore)


      





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
