def main():

  def variant(spis, N):
    rasn = 2**(N - 1) // 2
    spispl, spismn = ["+" for p in range((2**(N - 1)) // 2)
                      ], ["-" for m in range((2**(N - 1)) // 2)]
    for b in range(N - 2):
      flag = True
      r = 0
      rasn //= 2
      nom = -1
      for ro in range(2**(N - 1) // 2):
        nom += 1
        if flag == True:
          r += 1
          spispl[nom] += "+"
          spismn[nom] += "+"
        if flag == False:
          r -= 1
          spispl[nom] += "-"
          spismn[nom] += "-"
        if r == rasn:
          flag = False
        if r == 0:
          flag = True

    vce = spispl + spismn
    return (vce)

  file = open('lab1.txt', 'r+')
  spis = [int(symv) for symv in file.read().split()]
  N, S = spis.pop(0), spis.pop(-1)
  vce = variant(spis, N)
  st = str(spis[0])
  for v in range(len(vce)):
    n = 1
    summa = spis[0]
    for v1 in range(len(vce[v])):
      if vce[v][v1] == "+":
        summa += spis[n]
      else:
        summa -= spis[n]
      n += 1
    if summa == S:
      for b in range(1, N):
        st = st + vce[v][b - 1] + str(spis[b])
      st = st + "=" + str(S)
      print(st)
      file.write('\n' + st)
      break
  if st == str(spis[0]):
    print("No solution")
    file.write('\n' + "No solution")
if __name__ == "__main__":
  main()