def main():

  #signs_base = ["+", "-"]
  file = open('lab1.txt', 'r+')
  a = [int(symv) for symv in file.read().split()]
  N, b = a.pop(0), a.pop(-1)
  
  def seq_generator(number_of_seq, length):
      signs_sequence = ["" for i in range(length)]
      for i in range(length):
          if number_of_seq%2 == 1:
              signs_sequence[i] = "+"
          else:
              signs_sequence[i] = "-"
          number_of_seq = number_of_seq//2
      return signs_sequence
  
  def check_the_seq(a,b,signs):
      res = a[0]
      for i in range(len(a)-1):
          if signs[i] == "+":
              res += a[i+1]
          else:
              res -= a[i+1]
      if res == b:
          #print("Yep")
          return(True)
      else:
          return(False)

  def find_the_right(a,b,number,n_max):
      flag = 0
      signs = seq_generator(number, len(a)-1)
      res_string = str(a[0])
      if check_the_seq(a,b,signs):
          for i in range(len(a)-1):
              res_string += signs[i]+str(a[i+1])
          res_string += "="+str(b)
          flag = 1
          return res_string
      elif number == (2**(len(a)-1)):
          return "no solution"
      elif number == n_max:  
          return "ret_1"
      else:
          return find_the_right(a,b,number+1, n_max)
  
      
  
  
  #check_the_seq(a,b,signs_generated)
  
  number_of_cluster = 0
  limit_max = 500 * (number_of_cluster + 1) 
  limit_min = 500 * number_of_cluster
  count = 2**len(a)//limit_max+1
  seeker = ""
  while seeker != str(a[0]):
      boba = find_the_right(a,b,limit_min, limit_max)
      if boba == "ret_1":
          number_of_cluster += 1
          limit_max = 500 * (number_of_cluster + 1) 
          limit_min = 500 * number_of_cluster
      elif boba=="no solution":
          break
      else:
          print(boba)
          print(boba[:len(str(a[0]))])
          print(str(a[0]))
          seeker = boba[:len(str(a[0]))]
          print("seeker: ", seeker)
  
  print(boba)
  file.write('\n' + boba)
  file.close()

if __name__=="__main__":
  main()

