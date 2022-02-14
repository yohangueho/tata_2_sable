#########################################
# GROUPE 7
# Yohan GUÉHO
# Yanis TAIBI
# Mariam TROADEC-SAMOUR
# https://github.com/uvsq-info/l1-python
#########################################


### MODULES ###

import tkinter as tk
import random as rd
import time


### VARIABLES ###

height = 400
width = 400


### PROGRAMME ###

root = tk.Tk()
root.title("tata 2 sable")
canvas = tk.Canvas(root, height=height, width=width)
label = tk.Label(root, text="Hello World!")
bouton = tk.Button(root, text="hello")


canvas.pack()
label.pack()
bouton.pack()

root.mainloop()