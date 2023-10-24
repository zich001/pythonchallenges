MyArray = ["Linhao", "Zicheng", "Jerry"]

def LinearSerach(Item):
  for i in range(len(MyArray)):
    if MyArray[i] == Item:
      return i
  return -1
  
print(LinearSerach("Alex"))

#AS05
#Zicheng ZHANG
#205327
 
