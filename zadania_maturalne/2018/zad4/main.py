# 4.2
with open("./data/sygnaly.txt", "r") as f:
  dane = f.read().split("\n")
  najw = 0
  najdl = ""
  for linia in dane: 
    ilosc = len(set(linia))
    if not najw:
      najw = ilosc
    else:
      if ilosc > najw:
        najw = ilosc
        najdl = linia
  print(f"{najdl} - {najw}")


# 4.1
with open("./data/sygnaly.txt", "r") as f:
  dane = f.read().split("\n")
  rozwiazanie = []
  for linijka in range(0,len(dane),40):
    try:
      literka = dane[linijka-1][9]
      rozwiazanie.append(literka)
    except:
      pass
  print("".join(rozwiazanie))