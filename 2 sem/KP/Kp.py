import time
import pygame as pg
import tkinter as tk
import sys
import customtkinter

class TheFirstWindow(tk.Tk):
    """Класс, создающий окно для ввода N, L, K и проверяющий правильность введенных данных"""
    __slots__ = ["start_time", "n", "l", "k"]
    def __init__(self):
        super().__init__()
        names, entry_spis=("Размер доски(N)", "Кол-во требуемых фигур(L)", "Кол-во размещенных фигур(K)", "Запустить"), []
        check_reg, num_2=self.register(self.check), 0
        for num in range(3):
            tk.Label(text=names[num]).grid(row=num_2, column=0)
            entry=tk.Entry(validate="key", validatecommand=(check_reg, "%P", num_2), width=10)
            entry_spis.append(entry)
            entry.grid(row=num_2+1, column=0)
            num_2+=2
        self.n, self.l, self.k=entry_spis[0], entry_spis[1], entry_spis[2]
        tk.Button(text=names[3], command=lambda: self.create_new()).grid(row=7, column=0, pady=5)
 
    def check(self, input, number):
        """Метод для проверки корректности введенных данных"""
        if not input:
            return True
        if not input.isdigit():
            return False
        if (int(number)==0) and not (1<=int(input)<=20):
            return False         
        if (int(number)==2 or int(number)==4):
            if (str(self.n.get())==""):
                return False
            if (int(input)>(int(self.n.get()))**2):
                return False
        return True

    def create_new(self):
        """Метод кнопки для вызова окна для введения координат"""
        TheSecondWindow(int(self.n.get()), int(self.l.get()), int(self.k.get()))

class TheSecondWindow(tk.Tk):
    """Класс, создающий окно для введения координат"""
    __slots__ = ["start_time", "n", "l", "k", "entry_spis_2", "entry_spis"]
    def __init__(self, n, l, k):
        super().__init__()
        if k>3:
          frame_main = customtkinter.CTkScrollableFrame(master=self, width=130, height=200)
          frame_main.grid(row=0, column=1, sticky="ns")
        else:
          frame_main=self
        self.n, self.l, self.k, self.entry_spis_2=n, l, k, ()
        check_reg, self.entry_spis, num_2=self.register(self.check_2), [], 1
        tk.Label(frame_main, text="Введите координаты").grid(row=0, column=0)
        for prom_k in range(1, self.k+1):
            tk.Label(frame_main, text=f"№{prom_k}").grid(row=num_2, column=0)
            entry=tk.Entry(frame_main, validate="key", validatecommand=(check_reg, "%P"), width=10)
            self.entry_spis.append(entry)
            entry.grid(row=num_2+1, column=0)
            num_2+=2
        tk.Button(frame_main, text="Создать", command=lambda: self.create_the_apis()).grid(row=num_2+2, column=0, pady=5)
      
    def check_2(self, input):
        """Метод, проверяющий правильность введенных значений"""
        spis=input.split()
        if not input:
            return True
        if (input.count(" ")>1):
            return False    
        if not(spis!=[] and spis[-1].isdigit() and 0<=int(spis[-1])<self.n):
            return False
        return True

    def create_the_apis(self):
        """Метод, вызывающий класс для проверки координат"""
        self.entry_spis_2=tuple((int((input.get()).split()[0]), int((input.get()).split()[1])) for input in self.entry_spis)
        CheckCoords(self.entry_spis_2, self.n, self.l, self.k)
          
            
class CheckCoords(tk.Toplevel):
  """Класс для проверки на совпадение координат и расположение фигур под боем друг у друга"""
  __slots__ = ["start_time", "N", "entry_spis", "text"]
  def __init__(self, entry_spis_2, n, l, k):
        self.entry_spis=entry_spis_2
        self.N=n
        self.text=""
        self.hit_coords()
        if self.text!="":
          self.error_window(self.text)
        else:
          Board(self.entry_spis, self.N, l, k)

  def hit_coords(self):
      """Метод для перебора координат фигур и создания пояснения к ошибке, если таковая имеется"""
      for num_cor in range(len(self.entry_spis)-1):
        for num_cor_2 in range(num_cor+1, len(self.entry_spis)):
          self.num_cor_2=num_cor_2
          if self.entry_spis[num_cor]==self.entry_spis[num_cor_2]:
             self.text=f"Координаты фигуры {num_cor+1} и фигуры {num_cor_2+1} одинаковые!"
             break
          if self.mark_hit(self.entry_spis[num_cor][0], self.entry_spis[num_cor][1], True)==False:
            self.text=f"Фигуры {num_cor+1} и {num_cor+num_cor_2+1} находятся под боем друг у друга!"
            break
        if self.text!="":
          break

  def mark_hit(self, i, j, flag):
      """Метод, проверяющий, находится ли фигура под боем другой, или расставляющий на доске места, куда фигура может походить"""
      variants_i=(i-3, i+3, i+1, i-1)
      variants_j=((j-1, j+1), (j-3, j+3))

      for one_cor in range(len(variants_i)):
        if 0<=variants_i[one_cor]<self.N:
          if one_cor<2:
            num=0
          else:
            num=1
          for two_cor in range(2):
            if 0<=variants_j[num][two_cor]<self.N:
              if flag==True:
                if [(variants_i[one_cor]), (variants_j[num][two_cor])]==self.entry_spis[self.num_cor_2]:
                  return False
                else:
                  continue
              elif flag==False:
                  self.board[variants_i[one_cor]][variants_j[num][two_cor]] = "*"
              else:
                  if self.board[variants_i[one_cor]][variants_j[num][two_cor]] =="#":
                    return False

  @staticmethod
  def error_window(text):
      """Метод для создания окна с пояснением к ошибке"""
      toplevel=tk.Toplevel()
      toplevel.title("Ошибка!")
      tk.Label(master=toplevel, text=text).pack()

class Board:
    """Класс для поиска всех вариантов расстановки фигур и создания матрицы в виде доски для дальнейшей ее отрисовки в pygame"""
    __slots__ = ["start_time", "N", "L", "K", "prev_dots", "first_coords", "all_coords", "board"]
    def __init__(self, prev_dots, n, l, k):
        self.N, self.K=n, k
        self.prev_dots=tuple(prev_dots)
        self.first_coords, self.all_coords=(), []
        self.board=self.build_board(prev_dots, True)
        self.start_time=time.time()
        self.all_options(l, (0, 0))
        print("--- %s seconds ---" % (time.time() - self.start_time))
        if self.first_coords==():
          CheckCoords.error_window("Нет решений!")
        else:
          self.board=self.build_board(self.first_coords, False)
          Draw_the_Board(self.N, self.board, self.all_coords)
    
    def build_board(self, prev_dots, flag):
      """Метод создает доску для поиска новых решений или для ее отрисовки"""
      if flag==True:
        self.board = [['0' for _ in range(self.N)] for _ in range(self.N)]
        for coord_buf in prev_dots:
          self.board[int(coord_buf[0])][int(coord_buf[1])] = "#"
      elif flag==False:
        for coord_buf in range(0, len(self.first_coords)):
          if self.first_coords[coord_buf] not in self.prev_dots:
            self.board[int(prev_dots[coord_buf][0])][int(prev_dots[coord_buf][1])] = "%"
      for i in prev_dots:
          CheckCoords.mark_hit(self, int(i[0]), int(i[1]), False)
      return self.board
    
    def all_options(self, L, board):
      """Метод, ищущий места для постановки фигур и записывающий в массив все варианты координат фигур на доске"""
      if L==0:
        pod_mass=tuple((i, j) for i in range(len(self.board)) for j in range(len(self.board[i])) if self.board[i][j]=="#")
        if self.first_coords==():
          self.first_coords=tuple(p for p in pod_mass)
        self.all_coords.append(pod_mass)
        
      for x in range(board[0], len(self.board)):
        if x==board[0]:
          start=board[1]
        else:
          start=0
        for y in range(start, len(self.board[x])):
          if self.board[x][y]=="0" and CheckCoords.mark_hit(self, x, y, None)==None:
            self.board[x][y]="#"
            self.all_options(L-1, (x, y))
            self.board[x][y]="0"

 
class Draw_the_Board:
  """Класс для создания окна в pygame с графическим представлением доски и кнопки для записи всех решений в файл"""
  __slots__ = ["start_time", "N", "window", "button", "time", "FPS", "all_coords", "board"]
  def __init__(self, N, board, all_coords):
    pg.init()
    self.N, self.board=N, board
    self.all_coords=all_coords
    
    self.window=pg.display.set_mode((750, 500))
    pg.display.set_caption("Chess")
    self.window.fill((139, 69, 19))
    
    board_2=pg.Surface((300, 500))
    self.window.fill((255, 228, 116))
    self.window.blit(board_2, (570, 500))
    
    font = pg.font.Font(None, 35)
    text = font.render('Записать', True, (0, 0, 0), None)
    self.button=pg.draw.rect(self.window, (255, 255, 255), (570, 280, 130, 40))
    self.button=pg.draw.rect(self.window, (0, 0, 0), (570, 280, 130, 40), width=2)
    self.window.blit(text, (578, 284))
    
    self.time, self.FPS = pg.time.Clock(), 60
    
    pg.display.update()
    self.draw_the_final_board()
  
  def draw_the_final_board(self):
    """Метод для отрисовки доски в pygame и отслеживания события нажатия на кнопку 'Записать' """
    cell=(500/self.N)
    
    for x in range(self.N):
      for y in range(self.N):
        
        if self.board[y][x]=="#":

          pg.draw.rect(self.window, (144, 53, 59), (cell * x, cell*y, cell, cell))    
          
        elif self.board[y][x]=="%":
          pg.draw.rect(self.window, (127, 255, 0), (cell * x, cell*y, cell, cell))   
          
        elif self.board[y][x]=="*":
          pg.draw.rect(self.window, (224, 224, 224), (cell * x, cell*y, cell, cell))   
        
        elif self.board[y][x]=="0":
          pg.draw.rect(self.window, (205, 102, 29), (cell * x, cell*y, cell, cell))
          
        pg.draw.rect(self.window, (139, 69, 19), (cell * x, cell*y, cell, cell), width=5)   
        
      pg.display.update()
      
    while True:
      for event in pg.event.get():
        if event.type == pg.QUIT:
          sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and self.button.collidepoint(event.pos):
            self.output()
      self.time.tick(self.FPS)
              
  def output(self):
    """Метод для записи всех вариантов расстановки фигур в файл"""
    file_output=open('Все варианты расстановки', 'w+', encoding='utf-8')
    for var in self.all_coords:
      for number in var:
        file_output.write(f"{number} ")
      file_output.write("\n")
    file_output.close()
    print("Все решения записаны в файл!")
    
if __name__=="__main__":
  TheFirstWindow().mainloop()
