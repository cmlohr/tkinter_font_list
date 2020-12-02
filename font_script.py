from tkinter import Tk
import tkinter.font
import pandas

Tk()
font_list = [name for name in sorted(tkinter.font.families())]
data = pandas.DataFrame(font_list)
data.to_csv("tkinter_fonts.csv")