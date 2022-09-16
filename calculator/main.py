import tkinter as tk
from tkinter import ttk
from widgets import EntryBox, KeyButton, KeyPad


class Calculator(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Calculator")
        # self.geometry("380x550+580+200")

        # -- props --
        self.entry_value = tk.StringVar(value="0")
        self.history_value = tk.StringVar(value="History: ")

        self.entry = EntryBox(self, self.entry_value)
        self.entry.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

        keypad = KeyPad(self, self.entry, self.entry_value, self.history_value)
        keypad.grid(row=1, column=0, pady=20, padx=20)

        statusbar = tk.Label(
            self,
            height=3,
            textvariable=self.history_value,
            relief="sunken",
            anchor="w",
            font="verdana 11 bold"
        )
        statusbar.grid(row=2, column=0, sticky="ew")


root = Calculator()
root.mainloop()
