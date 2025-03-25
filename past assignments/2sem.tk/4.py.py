from random import randint
from tkinter import *

class Interface:

  def __init__(self, master):
    self.interface=master
    self.interface.title("4")
    self.number, self.attempts=randint(1, 100), 0
    self.label_1=Label(self.interface, text="Введите число от 1 до 100:")
    self.label_1.grid(row=0, columnspan=2, sticky="w")
    self.entry=Entry(self.interface, width=10)
    self.entry.grid(row=0, column=1)
    self.label_2=Label(self.interface, text="")
    self.label_2.grid(row=1, columnspan=3, sticky="w")
    names=["Ввод значения", "Начать заново", "Kоличество попыток"]
    for button in range(3):
      Button(self.interface, text=names[button], width=20, command=lambda number=button: self.functions_numbers(number)).grid(row=3, column=button)

    self.interface.mainloop()

  def functions_numbers(self, number):
    if number==0:
      self.check(self.entry.get())
    if number==1:
      self.number, self.attempts=randint(1, 100), 0
      self.label_2.config(text="")
      self.label_1.config(text="Введите число от 1 до 100:")
      return self.number, self.attempts, self.label_2, self.label_1
    if number==2:
      self.label_2.config(text=f"Количество попыток: {self.attempts}")
      return self.label_2
  
  def check(self, value):
    label_text=""
    if value.isdigit():
      if 1<=value<=100:
        if value<self.number:
            label_text="Введенное число меньше заданного"
        if value==self.number:
            label_text="Правильный ответ!"
        if value>self.number:
            label_text="Введенное число больше заданного"
        self.label_1.config(text=label_text)
        self.attempts+=1
      else:
         self.label_2.config(text="Ошибка: Введенное число не входит в диапазон значений от 1 до 100!")
    else:
      self.label_2.config(text="Ошибка: Введенное значение не является целым числом!")
        
window_2=Interface(Tk())
