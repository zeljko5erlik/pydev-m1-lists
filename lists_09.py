numbers = []
for number in range(21):
    numbers.append(number)



# #brisanje svih elemenata liste
# numbers.clear() 


# # kopiranje svih elemenata liste
# numbers_copy = number.copy()
# ptint('Ispis liste nakon copy()')
# for i in numbers:
#     print(i, end=' ')

#region 


#endregion

#prebropjavanje koliko se puta neki broj pojavljuje u listi
# numbers[3] = 15
# element = 15
# number_count = numbers.count(element)
# print(f'Element {element} se pojavljuje u listi {number_count} puta.')
# print(numbers)

print()
print('Ispis CIJELE LISTE')
for i in numbers:
    print(i, end=' ')
print('\n')

#ispis sortirane liste
numbers.sort(reverse=True)
print('Ispis CIJELE LISTE')
for i in numbers:
    print(i, end=' ')
print('\n')


