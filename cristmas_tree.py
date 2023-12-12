tree_hight = int(input('Unesite visinu bozicnog drvceta: '))
print()
print()


star_counter = 1
space_counter = 0 
for number in range(tree_hight):
    print(' ' * (tree_hight - space_counter), end=' ')
    print('*' * star_counter, end='\n')
    star_counter += 2
    space_counter += 1

for i in range(2):
    print(' ' * (tree_hight - 1), '| |')
    
