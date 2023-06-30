from tkinter import *
#import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from file_reader import FileReader
from nodes import SensorNodeIntegral
from sensored_signal import SensoredSignal

class MainApp(Tk):

    def __init__(self):
        super().__init__(className='Event-driven Sampling')

        self.file_reader = FileReader(self)

        methods = [
            "LC",
            "ILC"
            ]
        
        signal = SensoredSignal("Second-order underdamped system")
        
        selected_signal = StringVar(value = signal.test_signals[0])
        selected_method = StringVar(value = methods[0])

        Label(self, text = "Select type of signal:").pack()
        dropdown_signal = OptionMenu(self, selected_signal, *signal.test_signals)
        dropdown_signal.pack()
        Label(self, text = "Select an event-based sampling method:").pack()
        dropdown_methods = OptionMenu(self, selected_method, *methods)
        dropdown_methods.pack()

        ## Plots
        figure = plt.Figure(figsize=(15,3), dpi=100)
        ax1 = figure.add_subplot(111)
        ax1.set_title('Sampled signal')
        chart_type = FigureCanvasTkAgg(figure, self)
        chart_type.get_tk_widget().pack()

        self.sensor_node = SensorNodeIntegral(ax1, signal, 0.5, 0.01, 1000)



        open_file_button = ttk.Button(self, text = "Open file", command = self.file_reader.openfile)
        open_file_button.pack()

        start_button = ttk.Button(self, text = "Start", command = self.start_sensor)
        start_button.pack()


        super().mainloop()

    def start_sensor(self):
        self.sensor_node.sample(100)

