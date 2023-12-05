contacts = []


# upisite u listu onoliko kontakta koliko korisnik to zeli
# svaki kontakt ima: ime, prezime, broj telefona
# ali tako da vrijednosti unosi korisnik

number_of_contacts = int(input('Unesite zeljeni broj kontakata: '))

for i in range(0, number_of_contacts):
    first_name = input(f'Upisite ime {i + 1}. kontakta: ')
    last_name = input(f'Upisite prezime {i + 1}. kontakta: ')
    phone_number = input(f'Upisite broj {i + 1}. kontakta: ')
    
    contacts.append(first_name)
    contacts.append(last_name)
    contacts.append(phone_number)


# for i in range(0, number_of_contacts):
#     first_name = input(f'Upisite ime {i}. kontakta: ')
#     last_name = input(f'Upisite prezime {i}. kontakta: ')
#     phone_number = input(f'Upisite broj {i}. kontakta: ')
    
#     contacts.append(first_name)
#     contacts.append(last_name)
#     contacts.append(phone_number)


# for contact in contacts:
#     print(contact, end=' ')

counter = 0

for i in range(number_of_contacts):
    print(contacts[counter], end=' ')
    print(contacts[counter + 1], end=', ')
    print(contacts[counter + 1])

    counter = counter + 3
