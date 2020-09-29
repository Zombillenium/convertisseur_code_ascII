mot = input("trouver le code ASCII : ")
x = len(mot)
liste = []
i = 0
while i < x :
  liste.append(ord(mot[i]))
  i+=1
print(liste)
