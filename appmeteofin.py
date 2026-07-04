import requests
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap


#funzione per ottenere i dati
def info(city) :
    key = 'acafc1eda3db81af6ed497887b59aad9'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"
    res = requests.get(url)
    
    if res.status_code == 404:
        messagebox.showerror("Errore","Città insesitente o non trovata")
        return None
    situazione = res.json()
    icona_ID = situazione['weather'][0]['icon']
    temp = round(situazione['main']['temp'] - 270)
    meteo = situazione['weather'][0]['description']
    city = situazione['name']

    icona_url = f"http://openweathermap.org/img/wn/{icona_ID}@2x.png"
    return (icona_url, temp, meteo, city )




#funzione di ricerca
def search():
    city = inputcitta.get()
    risultato = info(city)
    if risultato is None:
        return
    #unpack delle informazioni
    icona_url, temp, meteo, city = risultato
    città_label.configure(text=f"{city}")
    
    immagine = Image.open(requests.get(icona_url, stream=True).raw)
    icon = ImageTk.PhotoImage(immagine)
    icona_label.configure(image=icon)
    icona_label.image = icon

    temp_label.configure(text=f"Temperatura {temp}°C")
    situazione_label.configure(text=f"{meteo}")


#Finestra principale
root = ttkbootstrap.Window(themename="morph")
root.title("Meteo")
root.geometry("400x400")



#Rettangolo per insierire le città
inputcitta = ttkbootstrap.Entry(root, font="Raleway, 18")
inputcitta.pack(pady=20)

#Bottone di ricerca
Ricerca = ttkbootstrap.Button(root, text="Cerca", command=search, bootstyle="warning")
Ricerca.pack(pady=20)

#mostrare la città
città_label = tk.Label(root, font ="Raleway, 26")
città_label.pack()

#Descrizione meterologica
situazione_label = tk.Label(root, font = "Raleway, 20")
situazione_label.pack()

#widget icone
icona_label = tk.Label(root)
icona_label.pack()

#temperatura label
temp_label = tk.Label(root, font = "Raleway, 20")
temp_label.pack()



root.mainloop()