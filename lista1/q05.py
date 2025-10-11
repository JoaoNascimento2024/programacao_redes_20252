
portas_comuns = [80, 443, 22, 21]
porta = int(input("Digite uma porta TCP"))
if porta in portas_comuns:
  print(f"{porta} é uma porta comum")
else:
  print(f"{porta} não é uma porta comum")
#============================================
porta_comum = False
if porta == 80:
  porta_comum = True
elif porta == 443:
  porta_comum = True
elif porta == 22:
  porta_comum = True
elif porta == 21:
  porta_comum = True
if porta_comum:
  print("Porta comum")
else:
  print("Porta não comum")





