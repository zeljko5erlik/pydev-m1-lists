#input_word = input('Unesite rijec: ')

numbers = []

for number in range(21):
    numbers.append(number)

list_exclusion = [2, 4, 13, 5]

#letter_list = []

#letter_list = list(input_word)

#print(numbers)
numbers_revised = numbers.copy()
print(numbers_revised)
for number in sorted(list_exclusion, reverse=True):
    numbers_revised.remove(numbers_revised[number])
    
print(numbers)
print()
print(numbers_revised)