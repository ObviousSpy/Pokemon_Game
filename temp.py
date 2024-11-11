from tkinter import CENTER, Tk, Label, Button
from PIL import Image, ImageTk
import random

root = Tk()
root.title("Pokemon Card Game")

root.geometry("800x800")
root.configure(background = 'lightblue1')

pikachu = ImageTk.PhotoImage(Image.open("pikachu.jpg"))
abra = ImageTk.PhotoImage(Image.open("abra.jpg"))
bulbasour = ImageTk.PhotoImage(Image.open("bulbasour.jpg"))
charmender = ImageTk.PhotoImage(Image.open("charmender.jpg")) 
Ivyasour = ImageTk.PhotoImage(Image.open("Iyvasour.jpg")) 
jigglypuff = ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))
kadabra = ImageTk.PhotoImage(Image.open("kadabra.jpg")) 
meowth = ImageTk.PhotoImage(Image.open("meowth.jpg")) 
nidoking = ImageTk.PhotoImage(Image.open("nidoking.jpg"))
paras = ImageTk.PhotoImage(Image.open("paras.jpg"))
persion = ImageTk.PhotoImage(Image.open("persion.jpg"))
ratata = ImageTk.PhotoImage(Image.open("ratata.jpg"))
squirtle = ImageTk.PhotoImage(Image.open("squirtle.jpg"))


Label1 = Label(root, text="player 1", bg="orange", fg="yellow")
Label1.place(relx = 0.1, rely = 0.3, anchor=CENTER)
Label2 = Label(root, text="player 2", bg="white", fg = "black")
Label2.place(relx = 0.9, rely = 0.3, anchor=CENTER)
Label3 = Label(root, bg="orange", fg = "yellow")
Label3.place(relx = 0.1, rely = 0.4, anchor=CENTER)
Label4 = Label(root, bg="white", fg = "black")
Label4.place(relx = 0.9, rely = 0.4, anchor=CENTER)
Label5 = Label(root, bg="blue", fg = "blue")
Label5.place(relx = 0.5, rely = 0.5, anchor=CENTER)
label_image = Label(root, bg="lightblue1")
label_image.place(relx=0.5, rely=0.5, anchor=CENTER)

pokemon_list = [pikachu, bulbasour, charmender, Ivyasour, jigglypuff, kadabra, meowth, paras, nidoking, abra, persion, ratata, squirtle]
Power_pokemon = [200, 60, 50, 100, 70, 70, 60, 40, 90, 30, 70, 40, 50]

player1Score = 0

def player1():
    global player1Score
    random_length = random.randint(0, 12)
    random_pokemon = pokemon_list[random_length]
    label_image.config(image=random_pokemon)
    label_image.image = random_pokemon
    random_power_list = Power_pokemon[random_length]
    player1Score = player1Score + random_power_list
    Label3.config(text=player1Score)

player2Score = 0

def player2():
    global player2Score
    random_length2 = random.randint(0, 12)
    random_pokemon2 = pokemon_list[random_length2]
    label_image.config(image=random_pokemon2)
    label_image.image = random_pokemon2
    random_power_list2 = Power_pokemon[random_length2]
    player2Score = player2Score + random_power_list2
    Label4.config(text=player2Score)
    

Button1 = Button(root, text = "player 1 button", command=player1)
Button1.place(relx = 0.1, rely = 0.5, anchor=CENTER)


Button2 = Button(root, text = "player 2 button", command=player2)
Button2.place(relx = 0.9, rely = 0.5, anchor=CENTER)

root.mainloop() 