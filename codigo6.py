import copy

numbers = [1,2,3,4,5]

copia = copy.deepcopy(numbers)

copia [0] = 99

print("Copia: ", copia)
print("Original: ", numbers)