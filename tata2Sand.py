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

height = 500
width = 500


### PROGRAMME ###

def close():
    root.destroy()

def ecoulement():
    for _ in range (0,10):
        ecoulement = tk.Label(root, text="grain")
        ecoulement.pack()
        time.sleep(1)

root = tk.Tk()
canvas = tk.Canvas(root, height=height, width=width)
root.title("tata 2 sable")
root.geometry('{}x{}'.format(height,width))

label = tk.Label(root, text="TATA 2 SABLE")
label.pack(anchor=tk.CENTER)

bouton = tk.Button(root, text="Go!")
bouton.pack(anchor=tk.CENTER, side=tk.BOTTOM)

Bclose = tk.Button(root, text="Close", command=close)
Bclose.pack(anchor=tk.CENTER, side=tk.BOTTOM)

ecoulement()
root.mainloop()
