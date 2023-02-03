navnet = input('skriv noget i retning af dit navn: ')
print('din lort', navnet)

try:
    etTal = int(input('Giv mig et bogstav, mener tal: '))
except:
    print("Er ikke den fødte programmør")
    exit('Fejlkode: Du dum du')

Givettalmere = int(input('Giv mig et andet tal: '))

summen = etTal+Givettalmere
print('Det giver: ', summen, ',', navnet, '.. Du sku have skruet hjernen ordenlig på')

print()