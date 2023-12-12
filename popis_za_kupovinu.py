list_number = int(input('Unesite broj namirnica koje zelite dodati u popis za kupovinu: '))
print( )

shoping_list = []

for number in range(list_number):
    shoping_list.append(input(f'Unesite {number + 1}. namirnicu u popis: '))
print()

print('Lista za kupovinu: ', end='\n')
for number in range(list_number):
    print(f'{number + 1}. {shoping_list[number]}')
print()

for number in range(80):
    print('*', end='')
print()

shoping_prices = []

for number in range(list_number):
    shoping_prices.append(int(input(f'Koliko ste platili za {shoping_list[number]}? (Unesite 0 ako nije kupljeno) ')))
print()

print('Lista namirnica sa cijenama: ')
for number in range(list_number):
    print(f'{number + 1}. {shoping_list[number]} - {shoping_prices[number]} €.', end='\n')
print()

print(f'Ukupan iznos za sve namirnice: {sum(shoping_prices)} €.')