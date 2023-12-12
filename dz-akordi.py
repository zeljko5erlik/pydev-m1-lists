chord_list = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'H']

base_tone = input('Unesite bazni ton: ')
base_tone = base_tone.upper()

base_tone_index = chord_list.index(base_tone)

chord_list[base_tone_index]
chord_list[(base_tone_index + 2) % len(chord_list)]
chord_list[(base_tone_index + 6) % len(chord_list)]

print(f'Trazeni molski akord je: {chord_list[base_tone_index]}-{chord_list[(base_tone_index + 2)%len(chord_list)]}-{chord_list[(base_tone_index + 6) % len(chord_list)]}')
print(f'Trazeni molski akord je: {chord_list[base_tone_index]}-{chord_list[(base_tone_index + 3)%len(chord_list)]}-{chord_list[(base_tone_index + 6) % len(chord_list)]}')

print(f'Durski akord {base_tone} tona cine: ', end='\n')
print(f'\t {base_tone} kao prvi ton,', end='\n')
print(f'\t {chord_list[(base_tone_index + 2)%len(chord_list)]} kao drugi ton, te', end='\n')
print(f'\t {chord_list[(base_tone_index + 6)%len(chord_list)]} kao treci ton.', end='\n')
print(f'\t Simbol akorda je: {base_tone} ili {base_tone} dur.', end='\n')