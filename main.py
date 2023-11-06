import pandas as pd
import tkinter as tk
from tkinter import *
import matplotlib as plt
import seaborn as sns

df = sns.load_dataset('iris')

window = tk.Tk()

label = tk.Label(window, text="Hello, Tkinter")
label.pack()

b = Button(text = "Simple")
b.pack()

window.mainloop()

def species(df):
    df[1].value_counts().plot(kind='bar')
    plt.show()