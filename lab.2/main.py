
def main():

  def print_board(board):
    for i in range(len(board)):
      print(board[i])

  def mark_hit(board, i, j):
    if (i - 3 >= 0):
      if (j - 1 >= 0):
        board[i - 3][j - 1] = ("*")
      if (j + 1 < N):
        board[i - 3][j + 1] = ("*")

    if (i - 1 >= 0):
      if (j - 3 >= 0):
        board[i - 1][j - 3] = ("*")
      if (j + 3 < N):
        board[i - 1][j + 3] = ("*")

    if (i + 1 < N):
      if (j - 3 >= 0):
        board[i + 1][j - 3] = ("*")
      if (j + 3 < N):
        board[i + 1][j + 3] = ("*")

    if (i + 3 < N):
      if (j - 1 >= 0):
        board[i + 3][j - 1] = ("*")
      if (j + 1 < N):
        board[i + 3][j + 1] = ("*")

  def build_board(N, prev_dots):
    board = [['0' for i in range(N)] for j in range(N)]
    for coord_buf in prev_dots:
      x, y = coord_buf[0], coord_buf[1]
      board[x][y] = "#"
    for i in prev_dots:
      mark_hit(board, i[0], i[1])
    return board

  def options(coordinates, N, L, one_coordinate, output_file):
    
    global no_solutions
    
    if L==0:
      no_solutions=False
      for mass in coordinates:
        output_file.write(str(tuple(mass)))
      output_file.write("\n")
      
    for x in range(one_coordinate[0], N):
      if x==one_coordinate[0]:
        start=one_coordinate[1]
      else:
        start=0
      for y in range(start, N):
        if build_board(N, coordinates)[x][y]=="0":
          coordinates.append([x, y])
          options(coordinates, N, L-1, [x, y], output_file)
          del coordinates[-1]
 
  input_file = open("input", "r")
  output_file = open("outputs2", "r+")

  char_input = input_file.readline().split()
  buffer = [int(sym) for sym in char_input]

  N, L, K = buffer[0], buffer[1], buffer[2]

  pre_figures = []
  for i in range(K):
    pre_figures.append(
      [int(coord_buf) for coord_buf in input_file.readline().split()])

  base_board = build_board(N, pre_figures)
  print_board(base_board)
  input_file.close()

  def all_options(L, base_board, pre_figures, output_file):
    g=True
    L-=1
    for x in range(N):
      for y in range(N):
        if base_board[x][y]=="0":
          pre_figures.append([x, y])
          options(pre_figures, N, L, [x, y], output_file)
          if no_solutions==False:
            g=False
          del pre_figures[-1]
    if g==True:
       output_file.write("no solutions")
  
  all_options(L, base_board, pre_figures, output_file)
  output_file.close()
  
if __name__ == "__main__":
  main()

no_solutions=True
