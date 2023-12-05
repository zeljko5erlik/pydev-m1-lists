contacts = []


# upisite u listu 4 kontakta koji imaju ime, prezime, broj telefona
# ali tako da vrijednosti unosi korisnik


for i in range(2):
    first_name = input(f'Upisite ime {i + 1}. kontakta: ')
    last_name = input(f'Upisite prezime {i + 1}. kontakta: ')
    phone_number = input(f'Upisite broj {i + 1}. kontakta: ')
    
    contacts.append(first_name)
    contacts.append(last_name)
    contacts.append(phone_number)

# for i in range(1, 3):
#     first_name = input(f'Upisite ime {i}. kontakta: ')
#     last_name = input(f'Upisite prezime {i}. kontakta: ')
#     phone_number = input(f'Upisite broj {i}. kontakta: ')
    
#     contacts.append(first_name)
#     contacts.append(last_name)
#     contacts.append(phone_number)


for contact in contacts:
    print(contact, end=' ')