from tkinter import *
#import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from file_reader import FileReader

class MainApp(Tk):

    def __init__(self):
        super().__init__(className='Event-driven Sampling')

        self.file_reader = FileReader(self)

        methods = [
            "LC",
            "ILC"
            ]
        selected_method = StringVar(value = methods[0])
        figure = plt.Figure(figsize=(15,3), dpi=100)
        Label(self, text = "Select a sampling method:").pack()
        dropdown_methods = OptionMenu(self, selected_method, *methods)
        dropdown_methods.pack()
        chart_type = FigureCanvasTkAgg(figure, self)
        chart_type.get_tk_widget().pack()
        open_file_button = ttk.Button(self, text = "Open file", command = self.file_reader.openfile)
        open_file_button.pack()
        super().mainloop()

