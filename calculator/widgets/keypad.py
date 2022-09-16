import tkinter as tk

from widgets import KeyButton


class KeyPad(tk.Frame):
    def __init__(self, parent, entry, entry_value, history_value, **kwargs):
        super().__init__(parent, **kwargs)

        self.entry = entry
        self.entry_value = entry_value
        self.history_value = history_value
        self.result_list = []

        # keypad numbers
        btn_numbers = []
        btn_tmp = 1
        for i in range(10):
            btn_numbers.append(tk.Button(
                self,
                width=4,
                height=2,
                text=str(i),
                font="times 15 bold",
                bd=5,
                command=lambda x=i: self.enter_number(x)
            ))

        for i in range(0, 3):
            for j in range(0, 3):
                # btn_numbers[btn_tmp].place(x=25+j*90, y=70+i*70)
                btn_numbers[btn_tmp].grid(row=i, column=j, padx=5, pady=5)
                btn_tmp += 1

        # keypad operators
        self.btn_operators = []
        for i in range(4):
            self.btn_operators.append(tk.Button(
                self,
                width=4,
                height=2,
                text=str(i),
                font="times 15 bold",
                bd=5,
                command=lambda x=i: self.enter_operator(x)
            ))
        self.btn_operators[0]["text"] = "+"
        self.btn_operators[1]["text"] = "-"
        self.btn_operators[2]["text"] = "*"
        self.btn_operators[3]["text"] = "/"

        for i in range(4):
            self.btn_operators[i].grid(row=i, column=4)

        # keypad other buttons
        btn_zero = KeyButton(self, text="0", command=lambda x=0: self.enter_number(x))
        btn_zero.grid(row=3, column=0)

        btn_clear = KeyButton(self, text="C", command=self.clear)
        btn_clear.grid(row=3, column=2)

        btn_dot = KeyButton(self, text=".", command=lambda x=".": self.enter_number(x))
        btn_dot.grid(row=3, column=1)

        btn_equal = btn_dot = KeyButton(self, text="=", command=self.calculate)
        btn_equal.grid(row=4, column=0, columnspan=4, sticky="ew")

    def enter_number(self, x):
        print(x)
        if self.entry_value.get() == "0":
            self.entry.delete(0, "end")
            self.entry_value.set(str(x))
            self.entry.insert(0, self.entry_value.get())
        else:
            length = len(self.entry.get())
            self.entry.insert(length, str(x))

    def enter_operator(self, x):
        if self.entry.get() != "0":
            length = len(self.entry.get())
            self.entry.insert(length, self.btn_operators[x]["text"])

    def clear(self):
        self.entry.delete(0, "end")
        self.entry_value.set("0")
        self.entry.insert(0, "0")

    def calculate(self):
        content = self.entry.get()
        result = eval(content)
        self.entry.delete(0, "end")
        self.entry.insert(0, str(result))
        self.entry_value.set(str(result))

        self.result_list.append(content)
        self.history_value.set("History: " + "|".join(self.result_list))
