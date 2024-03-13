import tkinter
from tkinter import ttk
import random
from PIL import Image, ImageTk
#"PIL" steht für das Modul "Pillow" - mit "pip install Pillow" zu installieren.

main_window = tkinter.Tk()
main_window.title("Würfel App")
main_window.geometry("650x380")

würfel_typen=["W4", "W6", "W8", "W10", "W12", "W20", "W100"]
würfel_anzahl  = ["1", "2", "3"]


würfel_auswahl_label_frame = tkinter.LabelFrame(main_window, text="Wähle deine/n Würfel")
würfel_auswahl_label_frame.grid(row=0, column=0, padx=25, pady=15)

würfel_anzahl_label_frame = tkinter.LabelFrame(main_window, text="Wähle die Anzahl deiner Würfel")
würfel_anzahl_label_frame.grid(row=2, column=0,padx=25, pady=25)

img = ImageTk.PhotoImage(Image.open("else.png").resize((50,50)))

def update_image(*args): # die Funktion wird immer aufgerufen, wenn sich der Wert, der Combobox ändert. das "*args" ist ein Plathhalter für beliebiige Argumente die wir theoretisch übergeben können. Das brauchen wir für die "trace" Methode
    global img # Definiert innerhalb der Funktion eine global abrufbare Variable
    auswahl = würfel_var.get() # Holt den aktuellen Wertt von "würfel_var" und speichert diesen in einer Variable
    if auswahl == würfel_typen[0]:
        img = ImageTk.PhotoImage(Image.open("W4.png").resize((50,50))) # Ich muss im Zweifel den relativen Pfad angeben ;) Mit der Variable habe ich das BIld geladen.
    elif auswahl == würfel_typen[1]:
        img = ImageTk.PhotoImage(Image.open("W6.png").resize((50,50)))
    elif auswahl == würfel_typen[2]:
        img = ImageTk.PhotoImage(Image.open("W8.png").resize((50,50)))
    elif auswahl == würfel_typen[3]:
        img = ImageTk.PhotoImage(Image.open("W10.png").resize((50,50)))
    elif auswahl == würfel_typen[4]:
        img = ImageTk.PhotoImage(Image.open("W12.png").resize((50,50)))
    elif auswahl == würfel_typen[5]:
        img = ImageTk.PhotoImage(Image.open("W20.png").resize((50,50)))
    elif auswahl == würfel_typen[6]:
        img = ImageTk.PhotoImage(Image.open("W100.png").resize((50,50)))
    würfel_button.config(image=img) # Durch den ".config()" Befehl wird das Bild schlussendlich aktualisiert

würfel_var = tkinter.StringVar() # Erstellt eine String Variable und speichert diese in einer Variable
würfel_var.trace('w', update_image) # Mit der "trace" Methode hat man die Möglichkeit Funktionen aufzurufen, sobald sich der Wert einer TKinter Variable ändert. Das "w" steht für "wrtie" was bedeutet, dass die Funktion aufgerufen wird, wenn der Wert der Variable geschrieben, also geändert wird. 

würfel_auswahl = ttk.Combobox(
    würfel_auswahl_label_frame,
    cursor="hand2",
    state="readonly",
    width=30,
    values=würfel_typen,
    textvariable=würfel_var # Binden Sie die StringVar-Variable an die Combobox
)
würfel_auswahl.pack(padx="5", pady="5")

würfel_anzahl_combobox = ttk.Combobox(
    würfel_anzahl_label_frame,
    cursor="hand2",
    state="readonly",
    width=30,
    values=würfel_anzahl
)

würfel_anzahl_combobox.pack(padx="5", pady="5")
# Mit dieser Funktion wird der Wert der Combobox bei Start auf 1, basierend auf der Liste "würfel_anzahl", gesetzt.
würfel_anzahl_combobox.current(0)

wirf_die_den_Würfel = tkinter.LabelFrame(main_window, text="Wirf die/den Würfel")
wirf_die_den_Würfel.grid(row=1, column=1, padx=20)


def aktueller_würfel():
    if würfel_anzahl_combobox.current() == 0: # Hier greift die "if" Abfrage vereinfacht auf den Index der Combobox bzw. der Liste von der Combobox zu
        if würfel_auswahl.get() == würfel_typen[0]:
            würfel_ergebnis = random.randint(1,4)
        elif würfel_auswahl.get() == würfel_typen[1]:
            würfel_ergebnis = random.randint(1,6)
        elif würfel_auswahl.get() == würfel_typen[2]:
            würfel_ergebnis = random.randint(1,8)
        elif würfel_auswahl.get() == würfel_typen[3]:
            würfel_ergebnis = random.randint(1,10)
        elif würfel_auswahl.get() == würfel_typen[4]:
            würfel_ergebnis = random.randint(1,12)
        elif würfel_auswahl.get() == würfel_typen[5]:
            würfel_ergebnis = random.randint(1,20)
        elif würfel_auswahl.get() == würfel_typen[6]:
            würfel_ergebnis = random.randint(1,100)
        anzeige_würfelaugen_ergebnis_1.config(text=würfel_ergebnis) # Ändert den Text des Textlabels "anzeige_würfelaugen_ergebnis", auf den Inhalt der Variable "würfel_ergebnis"
        anzeige_würfelaugen_ergebnis_2.config(text="Ändere deine Einstellung!")
        anzeige_würfelaugen_ergebnis_3.config(text="Ändere deine Einstellung!")

    if würfel_anzahl_combobox.current() == 1:
        if würfel_auswahl.get() == würfel_typen[0]:
            würfel_ergebnis = random.randint(1,4)
        elif würfel_auswahl.get() == würfel_typen[1]:
            würfel_ergebnis = random.randint(1,6)
        elif würfel_auswahl.get() == würfel_typen[2]:
            würfel_ergebnis = random.randint(1,8)
        elif würfel_auswahl.get() == würfel_typen[3]:
            würfel_ergebnis = random.randint(1,10)
        elif würfel_auswahl.get() == würfel_typen[4]:
            würfel_ergebnis = random.randint(1,12)
        elif würfel_auswahl.get() == würfel_typen[5]:
            würfel_ergebnis = random.randint(1,20)
        elif würfel_auswahl.get() == würfel_typen[6]:
            würfel_ergebnis = random.randint(1,100)
        anzeige_würfelaugen_ergebnis_1.config(text=würfel_ergebnis)
        if würfel_auswahl.get() == würfel_typen[0]:
            würfel_ergebnis = random.randint(1,4)
        elif würfel_auswahl.get() == würfel_typen[1]:
            würfel_ergebnis = random.randint(1,6)
        elif würfel_auswahl.get() == würfel_typen[2]:
            würfel_ergebnis = random.randint(1,8)
        elif würfel_auswahl.get() == würfel_typen[3]:
            würfel_ergebnis = random.randint(1,10)
        elif würfel_auswahl.get() == würfel_typen[4]:
            würfel_ergebnis = random.randint(1,12)
        elif würfel_auswahl.get() == würfel_typen[5]:
            würfel_ergebnis = random.randint(1,20)
        elif würfel_auswahl.get() == würfel_typen[6]:
            würfel_ergebnis = random.randint(1,100)
        anzeige_würfelaugen_ergebnis_2.config(text=würfel_ergebnis)
        anzeige_würfelaugen_ergebnis_3.config(text="Ändere deine Einstellung!")

    if würfel_anzahl_combobox.current() == 2:
        if würfel_auswahl.get() == würfel_typen[0]:
            würfel_ergebnis = random.randint(1,4)
        elif würfel_auswahl.get() == würfel_typen[1]:
            würfel_ergebnis = random.randint(1,6)
        elif würfel_auswahl.get() == würfel_typen[2]:
            würfel_ergebnis = random.randint(1,8)
        elif würfel_auswahl.get() == würfel_typen[3]:
            würfel_ergebnis = random.randint(1,10)
        elif würfel_auswahl.get() == würfel_typen[4]:
            würfel_ergebnis = random.randint(1,12)
        elif würfel_auswahl.get() == würfel_typen[5]:
            würfel_ergebnis = random.randint(1,20)
        elif würfel_auswahl.get() == würfel_typen[6]:
            würfel_ergebnis = random.randint(1,100)
        anzeige_würfelaugen_ergebnis_1.config(text=würfel_ergebnis)       
        if würfel_auswahl.get() == würfel_typen[0]:
            würfel_ergebnis = random.randint(1,4)
        elif würfel_auswahl.get() == würfel_typen[1]:
            würfel_ergebnis = random.randint(1,6)
        elif würfel_auswahl.get() == würfel_typen[2]:
            würfel_ergebnis = random.randint(1,8)
        elif würfel_auswahl.get() == würfel_typen[3]:
            würfel_ergebnis = random.randint(1,10)
        elif würfel_auswahl.get() == würfel_typen[4]:
            würfel_ergebnis = random.randint(1,12)
        elif würfel_auswahl.get() == würfel_typen[5]:
            würfel_ergebnis = random.randint(1,20)
        elif würfel_auswahl.get() == würfel_typen[6]:
            würfel_ergebnis = random.randint(1,100)
        anzeige_würfelaugen_ergebnis_2.config(text=würfel_ergebnis)
        if würfel_auswahl.get() == würfel_typen[0]:
            würfel_ergebnis = random.randint(1,4)
        elif würfel_auswahl.get() == würfel_typen[1]:
            würfel_ergebnis = random.randint(1,6)
        elif würfel_auswahl.get() == würfel_typen[2]:
            würfel_ergebnis = random.randint(1,8)
        elif würfel_auswahl.get() == würfel_typen[3]:
            würfel_ergebnis = random.randint(1,10)
        elif würfel_auswahl.get() == würfel_typen[4]:
            würfel_ergebnis = random.randint(1,12)
        elif würfel_auswahl.get() == würfel_typen[5]:
            würfel_ergebnis = random.randint(1,20)
        elif würfel_auswahl.get() == würfel_typen[6]:
            würfel_ergebnis = random.randint(1,100)
        anzeige_würfelaugen_ergebnis_3.config(text=würfel_ergebnis)

würfel_button = ttk.Button(wirf_die_den_Würfel, image=img, cursor="hand2", command=aktueller_würfel)
würfel_button.pack(padx="5", pady="5")

#Mit dem Befehl "image=img" weise dem Button das Bild zu. Mit dem Befehl "cursor="hand2" verändert man den Mauszeiger im Bereich des Buttons

würfelaugen_ergebnis_label_frame = tkinter.LabelFrame(main_window, text="Dein Würfelergebnis!")
würfelaugen_ergebnis_label_frame.grid(row=1, column=2, pady=25)

anzeige_würfelaugen_ergebnis_1 = ttk.Label(würfelaugen_ergebnis_label_frame, background="#BDBDBD", text="Hier kommt dein Würfelergebnis!", width=30)
anzeige_würfelaugen_ergebnis_1.pack(padx="5", pady="5")
anzeige_würfelaugen_ergebnis_2 = ttk.Label(würfelaugen_ergebnis_label_frame, background="#BDBDBD", text="Ändere deine Einstellung!", width=30)
anzeige_würfelaugen_ergebnis_2.pack(padx="5", pady="5")
anzeige_würfelaugen_ergebnis_3 = ttk.Label(würfelaugen_ergebnis_label_frame, background="#BDBDBD", text="Ändere deine EInstellung!", width=30)
anzeige_würfelaugen_ergebnis_3.pack(padx="5", pady="5")

main_window.mainloop()