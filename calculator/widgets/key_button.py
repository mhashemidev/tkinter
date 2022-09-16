import tkinter as tk


class KeyButton(tk.Button):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self["width"] = 4,
        self["height"] = 2,
        self["font"] = "times 15 bold",
        self["bd"] = 5,
