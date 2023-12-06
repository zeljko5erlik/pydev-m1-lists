word_for_counting = input('Unesite riječ za računanje zbroja slova:')

letters = list(word_for_counting)
print(f'Ispis liste slova u Vašoj riječi: {letters}')

print()

letter_sum = 0

for letter in letters:
    number = ord(letter)
    letter_sum += number
    print(f'Broj koji odgovara {letters.index(letter) + 1}. slovu je: {number}')

print()

print(f'Zbroj slova u Vašoj riječi je: {letter_sum}')