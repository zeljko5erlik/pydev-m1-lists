# Napisite program koji zbraja brojeve od 1 do nekog broja.
# Neka korisnik definira do kojeg broja zeli da bude zbrajanje
# Ispisite zbroj te ispisite srednju vrijednost (zbroj/broj elemenata

numbers = []

sum_limit = int(input('Unesite broj do kojeg zelite zbrajati: '))

number_sum = 0
for number in range(sum_limit + 1):  #ovdje je dodani i pocetni element na predavanju
    number_sum += number
    numbers.append(number)



print(f'Zbroj brojeva od 1 do {sum_limit} je: {number_sum}')
print(f'Prosjek brojeva od 1 do {sum_limit} je: {number_sum / len(numbers)}')

print(number_sum)