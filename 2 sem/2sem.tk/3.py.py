from tkinter import *

class Selecting_figures:
  def __init__(self, master):
    self.master=master
    master.title("Выбор фигуры")
    figure=["Прямоугольник", "Круг", "Треугольник"]
    for number in range(len(figure)):
      Button(master, text=figure[number], width=25, command=lambda number=number: self.data_input(number)).grid(row=number, column=0, padx=5, pady=5)

  def data_input(self, number):
    additional_window=Toplevel()
    additional_window.title("Ввод данных")
    options=[["Длина", "Ширина"], ["Радиус"], ["Длина стороны A", "Высота треугольника"]]
    Label(additional_window, text=options[number][0]).grid(row=0, column=0)
    self.input=Entry(additional_window, width=25)
    self.input.grid(row=1, column=0)
    if str(number) in "02":
      Label(additional_window, text=options[number][1]).grid(row=0, column=1)
      self.input_2=Entry(additional_window, width=25)
      self.input_2.grid(row=1, column=1)

    if number==0:
      Button(additional_window, text="Нарисовать", command=lambda: Rectangle(self.input.get(), self.input_2.get())).grid(row=1, column=2)
    elif number==1:
       Button(additional_window, text="Нарисовать", command=lambda: Circle(self.input.get())).grid(row=1, column=2)
    else:
      Button(additional_window, text="Нарисовать", command=lambda: Triangle(self.input.get(), self.input_2.get())).grid(row=1, column=2)

class Rectangle:
  def __init__(self, datas_1, datas_2):
    self.datas_1=datas_1
    self.datas_2=datas_2
    self.window_2=Toplevel()
    self.window_2.title("Результат")
    self.area_the_figure=int(self.datas_1)*int(self.datas_2)
    self.draw()

  def draw(self):
      rectangle=Canvas(self.window_2, bg="white", width=400, height=400)
      rectangle.grid(row=0, column=0)
      rectangle.create_rectangle(200, 200, self.datas_2, self.datas_1, fill='grey', outline="black")
      frame_b=Frame(self.window_2, width=10, height=10)
      Label(master=frame_b, text=f"Площадь прямоугольника равна {self.area_the_figure}").grid(row=1, column=0)
      frame_b.grid(row=1, column=0)

class Circle:
  def __init__(self, datas):
    self.datas=datas
    self.window_2=Toplevel()
    self.window_2.title("Результат")
    self.area_the_figure=3.14*(int(self.datas))**2
    self.draw()

  def draw(self):
    rectangle=Canvas(self.window_2, bg="white", width=400, height=400)
    rectangle.grid(row=0, column=0)
    rectangle.create_oval(200 - int(self.datas), 200 - int(self.datas), 200 + int(self.datas), 200 + int(self.datas), fill='grey', outline="black")
    frame_b=Frame(self.window_2, width=10, height=10)
    Label(master=frame_b, text=f"Площадь круга равна {self.area_the_figure}").grid(row=1, column=0)
    frame_b.grid(row=1, column=0)

class Triangle:
  def __init__(self, datas_1, datas_2):
      self.datas_1=datas_1
      self.datas_2=datas_2
      self.window_2=Toplevel()
      self.window_2.title("Результат")
      self.area_the_figure=int(self.datas_1)*int(self.datas_2)/2
      self.draw()
  def draw(self):
    rectangle=Canvas(self.window_2, bg="white", width=400, height=400)
    rectangle.grid(row=0, column=0)
    rectangle.create_polygon(200, 200, int(self.datas_1)+200, 200, 200-int(self.datas_2), (int(self.datas_1)+200)/2,  fill='grey', outline="black")
    frame_b=Frame(self.window_2, width=10, height=10)
    Label(master=frame_b, text=f"Площадь треугольника равна {self.area_the_figure}").grid(row=1, column=0)
    frame_b.grid(row=1, column=0)

r=Tk()
window=Selecting_figures(r)
r.mainloop()
