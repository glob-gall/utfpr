from knn import getSortedItemFromFile,getrandomPercentNumbers



numbers = getSortedItemFromFile('professor/treinamento.txt')

numbers = getrandomPercentNumbers(numbers,3)

numbers.sort(key = lambda x : x.name)


for n in numbers:
    print(n.name)
    print(n.xys)