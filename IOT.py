import time
import pandas.plotting as pdplt
import matplotlib.pylab as plt
import seaborn as sns
import subprocess
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from tkinter import *
import tkinter as tk

df = pd.read_csv("test_file2.csv", names=['humidity', 'temp', 'moisture', 'LDR', 'output'])
class EnterInterface:
    def __init__(self, master):
        self.master = master
        master.title("Smart Agriculture Data Analyzer")
        master.minsize(width=1000, height=550)

        f1 = Frame(master, height=100, width=175)
        f1.pack_propagate(0)  # don't shrink
        f1.pack()
        f1.place(x=425, y=60)
        
    
        self.greet_button = Button(f1, text="Explore Data", command=self.graph_menu)
        self.greet_button.config(activebackground='Green', relief='raised')
        self.greet_button.pack(fill=BOTH, expand=1)


        f3 = Frame(master, height=50, width=175)
        f3.pack_propagate(0)  # don't shrink
        f3.pack()
        f3.place(x=425, y=200)

        self.close_button = Button(f3, text="Close", command=root.destroy)
        self.close_button.config(activebackground='Red')
        self.close_button.pack(fill=BOTH, expand=1)

    def graph_menu(self):
        menubar = Menu(root)
        menubar.add_command(label="Andrews Graph", activebackground='Light Green', command=self.display_andrews_graph)
        menubar.add_command(label="Regression Graph", activebackground='Light Green', command=self.regression_graph)
        menubar.add_command(label="Temperature Gradient", activebackground='Light Green', command=self.temp)
        menubar.add_command(label="FaceGrid", activebackground='Light Green', command=self.face)
        menubar.add_command(label="Humidity Gradient", activebackground='Light Green', command=self.humidity)
        menubar.add_command(label="Quit", activebackground='Light Green', command=root.quit)
        # display the menu
        root.config(menu=menubar)

    def display_andrews_graph(self):
        pdplt.andrews_curves(df, "output", ax=None)
        plt.show()

    def regression_graph(self):
        df = pd.read_csv("test_file2.csv", names=['humidity', 'temp', 'moisture', 'LDR', 'output'])
        sns.jointplot(x="moisture", y="humidity",kind='reg', data=df)

    def temp(self):
        df = pd.read_csv("test_file2.csv", names=['humidity', 'temp', 'moisture', 'LDR', 'output'])
        g = sns.FacetGrid(df, col="output")
        g.map(sns.histplot, "temp")
        plt.show()

    def humidity(self):
        df = pd.read_csv("test_file2.csv", names=['humidity', 'temp', 'moisture', 'LDR', 'output'])
        g = sns.FacetGrid(df, col="output")
        g.map(sns.histplot, "humidity")
        plt.show()

    def face(self):
        df = pd.read_csv("test_file2.csv", names=['humidity', 'temp', 'moisture', 'LDR', 'output'])
        g = sns.FacetGrid(df, col="output")
        g.map(sns.regplot, "humidity", "temp")
        plt.xlim(0, 100)
        plt.ylim(0, 35)
        plt.show()


root = tk.Toplevel()
background_image = tk.PhotoImage(file="fill.png")
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
my_gui = EnterInterface(root)
# root["bg"] = 'white'
root.mainloop()


