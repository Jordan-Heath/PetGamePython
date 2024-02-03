import random
import tkinter as tk
from tkinter import Button, Label, Entry

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.happiness = 100
        self.energy = 100

    def feed(self):
        self.hunger = max(0, self.hunger - 20)
        self.update_status()

    def play(self):
        self.happiness = min(100, self.happiness + 20)
        self.energy = max(0, self.energy - 10)
        self.update_status()

    def sleep(self):
        self.energy = min(100, self.energy + 30)
        self.update_status()

    def update_status(self):
        status_table.config(text=f"{self.name}'s status:\nHunger: {self.hunger}\nHappiness: {self.happiness}\nEnergy: {self.energy}")

class Game:
    def __init__(self):
        self.pet = None

    def start_game(self, pet_name):
        self.pet = Pet(pet_name)
        start_frame.destroy()
        main_frame.pack()

    def on_feed_button_click(self):
        self.pet.feed()

    def on_play_button_click(self):
        self.pet.play()

    def on_sleep_button_click(self):
        self.pet.sleep()

    def on_quit_button_click(self):
        root.destroy()

game = Game()

root = tk.Tk()
root.title("Pet Care Game")
root.geometry("500x400")

start_frame = tk.Frame(root)
start_frame.pack(expand=True)

pet_image = tk.PhotoImage(file="pet_sprite.png")  # Replace "pet_sprite.png" with your own image file
pet_label = Label(start_frame, image=pet_image)
pet_label.pack(pady=10)

name_label = Label(start_frame, text="Enter your pet's name:")
name_label.pack()

name_entry = Entry(start_frame)
name_entry.pack()

start_button = Button(start_frame, text="Start", command=lambda: game.start_game(name_entry.get()))
start_button.pack(pady=10)

main_frame = tk.Frame(root)
main_frame.pack(expand=True)

status_table = Label(main_frame, text="", justify="right")
status_table.grid(row=0, column=1, pady=10, sticky="ne")

feed_button = Button(main_frame, text="Feed", command=game.on_feed_button_click)
feed_button.grid(row=1, column=0, padx=5, pady=10)

play_button = Button(main_frame, text="Play", command=game.on_play_button_click)
play_button.grid(row=1, column=1, padx=5, pady=10)

sleep_button = Button(main_frame, text="Sleep", command=game.on_sleep_button_click)
sleep_button.grid(row=1, column=2, padx=5, pady=10)

quit_button = Button(main_frame, text="Quit", command=game.on_quit_button_click)
quit_button.grid(row=2, column=1, pady=10)

root.mainloop()
