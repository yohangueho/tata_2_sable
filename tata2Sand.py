#########################################
# GROUPE 7
# Yohan GUÉHO
# Yanis TAIBI
# Mariam TROADEC-SAMOUR
# https://github.com/uvsq-info/l1-python
# change this
#########################################


### MODULES ###

from tkinter import *
import random as rd
import time


### VARIABLES ###

height = 500
width = 500


### PROGRAMME ###

root = Tk()
root.title("tata 2 sable")
root.geometry('{}x{}'.format(height,width))
canvas = Canvas(root, height=height, width=width)
label = Label(root, text="Reconfiguration")
bouton = Button(root, text="Go!")

label.grid(row=0)
bouton.grid(row=1)

root.mainloop()