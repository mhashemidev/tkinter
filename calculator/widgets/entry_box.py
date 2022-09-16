import tkinter as tk


class EntryBox(tk.Entry):
    def __init__(self, parent, entry_value, **kwargs):
        super().__init__(parent, **kwargs)

        self["font"] = "verdana 12 bold"
        self["width"] = 22
        self["bd"] = 5
        self["justify"] = "right"
        self["bg"] = "#e6e6fa"
        self["textvariable"] = entry_value.get()

        self.insert(0, "0")
