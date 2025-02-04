import math
import random
K_NEIGHBORS = [1,3,5,7,9,11,13,15,17,19]

class Number:
  name:str
  xys=[]
  
  def __init__(self,name,blacks_whites) -> None:
    self.name = name
    self.xys = blacks_whites
 
def euclidianDistance(el1, el2):
  n=0
  for i in range(len(el2)):
    n+=(float(el2[i]) - float(el1[i])) * (float(el2[i]) - float(el1[i]))
  return math.sqrt((n))
  
def getNumberFromFile(lines):
  numbers=[]
  for l in lines:
    items = l.split(' ')
    # items.pop()
    name = items.pop()
      
    number = Number(name=name,blacks_whites=items)
    numbers.append(number)
  return numbers

def getDistances(num:Number, numbers:list()):
  
  items=[]
  for n in numbers:
    item={}
    item['name'] = n.name
    item['dist'] = euclidianDistance(num.xys,n.xys)
    items.append(item)
  return items

def getNRandomItemsFromList(l:list,qnt:int):
  newList = []
  for i in range(qnt):
    item = random.choice(l)
    newList.append(item)
    l.remove(item)
  return newList

def getkNeighbors(distancias,k):
  return distancias[1:1+k]
  
def getallItensFromFile(path):
  f = open(path)
  lines = f.readlines()
  numbers = getNumberFromFile(lines)
  return numbers

def getSortedItemFromFile(path):
  numbers = getallItensFromFile(path)
  randomSelectedNumbers = getNRandomItemsFromList(numbers,1000)
  return randomSelectedNumbers


def getrandomPercentNumbers(numbers,nEachClass):
  listAllClasses=[]
  classes = []

  found=False
  for n in numbers:
    for c in classes:
      if c['name'] == n.name:
       found=True
       if c['count'] < nEachClass:
         listAllClasses.append(n)
       c['count'] +=1
    if not found:  
      classes.append({'name':n.name, 'count':1})
      listAllClasses.append(n)
    found=False
  return listAllClasses
  
def calculateAllDistances(selected,k):
  treinamentos = getSortedItemFromFile('professor/treinamento.txt')
  # 25 para 25%, 50 para 50% e 100 para 100%
  treinamentos = getrandomPercentNumbers(treinamentos,100)

  distancias = getDistances(selected,treinamentos)
  sortedDists = sorted(distancias, key=lambda i: i['dist'],reverse=False)
  count = 0
  nn = getkNeighbors(sortedDists,k)
  for n in nn:
    if n['name'] == selected.name:
      count+=1
  return (count/k)


def main():
  testes = getallItensFromFile('professor/teste.txt')

  for k in K_NEIGHBORS:
    print(f'K = {k}')
    sumResult=0
    for teste in testes:
      sumResult+= calculateAllDistances(selected=teste,k=k)
    print(f'result: {sumResult/1000}')


if __name__ == "__main__":
   main()