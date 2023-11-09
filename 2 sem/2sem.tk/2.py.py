from tkinter import Tk, Button, Entry, Label
import tkinter

class List_interface:
  def __init__(self, master):
    self.master = master
    master.title("Обработка динамического списка")
    buttons, index=["Создание списка", "Вывод списка в консоль", "Запись списка в файл", "Количество элементов в списке", "Добавление элемента в список", "Поиск элемента в списке", "Удаление элемента из списка", "Выход"], 0
    for column in range(2):
      for row in range(4):
        Button(master, text=buttons[index], width=25, command=lambda index=index: self.fuctions(index, buttons)).grid(row=row, column=column, padx=4, pady=4)
        index+=1


  def fuctions(self, number, buttons):
    if str(number) in "03456":
      additional_window=tkinter.Toplevel()
      additional_window.title(buttons[number])
      if str(number) in "0456":
        inscriptions=["Сохранить", "", "", "", "Добавить", "Найти", "Удалить"]
        self.widget_entry=Entry(master=additional_window, width=50)
        self.widget_entry.grid(row=0, column=0)
        Button(master=additional_window, text=inscriptions[number], command=lambda number=number: self.subfunctions(number,self.widget_entry.get())).grid(row=0, column=1)
      elif str(number) in "3":
        Label(master=additional_window, text=len(self.list), width=50).grid(row=0, column=0)
    if str(number) in "1":
      print(self.list)
    if str(number) in "2":
      file=open("file.txt", "w")
      file.write(",".join(self.list))
      file.close()
    if str(number) in "7":
      self.master.destroy()
  
    
  def subfunctions(self, number, data):
    if str(number)=="0":
      self.list=data.split()
      return  self.list
    if str(number)=="4":
      self.list.append(data)
      return self.list
    if str(number)=="5":
      if data in self.list:
        print(f"элемент {data} найден")
        return
      print(f"элемент {data} не найден")
      return
    if str(number)=="6":
      if data in self.list:
        self.list.remove(data)
        print(f"элемент {data}  найден и удален")
        return self.list
      print(f"элемент {data} не найден")
      return
      

window=Tk()
interface= List_interface(window)
window.mainloop()
        