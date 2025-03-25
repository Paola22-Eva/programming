from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E
class Calculator:

    def __init__(self, master:'Tk'):
        self.master = master
        master.title("Calculator")
        self.total = 0
        self.entered_number = 0
        self.total_label_text = IntVar()
        self.total_label_text.set(self.total)
        self.total_label = Label(master, textvariable=self.total_label_text)
        self.label = Label(master, text="Total:")
        vcmd = master.register(self.validate)
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P')) # validate='key' - валидация при каждом вводе нового символа. validatecommand говорит, что валидировать ввод будет команда "check". Второй элемент - подстановка "%P" представляет новое значение, которое передается в функцию валидации. Собственно саму валидацию выполняет функция is_valid(). Она принимает один параметр - текущее значение Entry, которое надо валидировать. Она возвращает True, если значение прошло валидацию, и False, если не прошло. Сама логика валидации представляет проверку строки на регулярное выражение "^\+\d*$". Если новое значение соответствует этому выражению, и в нем не больше 12 символов, то оно прошло валидацию.
        self.add_button = Button(master, text="+", command=lambda: self.update("add"))
        self.subtract_button = Button(master, text="-", command=lambda: self.update("subtract"))
        self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))
        self.multiplication_button = Button(master, text="*", command=lambda: self.update("multiplication"))
        self.division_button = Button(master, text="/", command=lambda: self.update("division"))

        self.label.grid(row=0, column=0, sticky=W)
        self.total_label.grid(row=0, column=1, columnspan=2, sticky=E)
        self.entry.grid(row=1, column=0, columnspan=3, sticky=W+E)
        self.add_button.grid(row=2, column=0, sticky=W)
        self.subtract_button.grid(row=2, column=1, sticky=W)
        self.multiplication_button.grid(row=2, column=2, sticky=W)
        self.division_button.grid(row=2, column=3, sticky=W)
        self.reset_button.grid(row=1, column=4, sticky=W+E)

    def validate(self, new_text: str):
        if not new_text: # the field is being cleared
            self.entered_number = 0
            return True
        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False
    def update(self, method):
        if method == "add":
            self.total += self.entered_number
        elif method == "subtract":
            self.total -= self.entered_number
        elif method=="multiplication":
          self.total *= self.entered_number 
        elif method== "division":
          self.total /= self.entered_number
        else: # reset
            self.total = 0
        self.total_label_text.set(self.total)
        self.entry.delete(0, END)

root = Tk()
my_gui = Calculator(root)
root.mainloop()