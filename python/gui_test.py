import tkinter as tk

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # self.pack()
        self.create_widgets()

    def create_widgets(self):
        fig = Figure(figsize=(5, 4), dpi=100)
        t = np.arange(0, 3, .01)
        fig.add_subplot().plot(t, 2 * np.sin(2 * np.pi * t))

        canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
        canvas.draw()

        canvas.mpl_connect(
            "key_press_event", lambda event: print(f"you pressed {event.key}"))
        canvas.mpl_connect("key_press_event", key_press_handler)

        # canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        canvas.get_tk_widget().grid(column=0, row=0, columnspan=3, ipadx=40, ipady=20)

        self.front = tk.Button(root, text='正面', command=self.collect_front_data)
        self.front.grid(column=0, row=1)

        self.tail = tk.Button(root, text='反面', command=self.collect_tail_data)
        self.tail.grid(column=1, row=1)

        self.start = tk.Button(root, text='识别', command=self.identify)
        self.start.grid(column=2, row=1)

        self.result = tk.Label(root, text='识别结果……')
        self.result.grid(column=0, row=2, columnspan=3)
        # self.hi_there = tk.Button(self)
        # self.hi_there["text"] = "Hello World\n(click me)"
        # self.hi_there["command"] = self.say_hi
        # self.hi_there.pack(side="top")
        #
        # self.quit = tk.Button(self, text="QUIT", fg="red",
        #                       command=self.master.destroy)
        # self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

    def collect_front_data(self):
        print("collect front data~")

    def collect_tail_data(self):
        print("collect tail data~")

    def identify(self):
        print("identify: ")


root = tk.Tk()
root.wm_title("液体识别")
app = Application(master=root)
app.mainloop()