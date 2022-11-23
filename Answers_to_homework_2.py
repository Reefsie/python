list_of_fruits = ['apple', 'banana', 'pear', 'kiwi', 'passionfruit']
for fruit in list_of_fruits:
    if fruit == 'apple':
        print(fruit)

list_of_brands_without_letter_p = ['Google', 'Microsoft', 'North Face', 'Logitech', 'Corsair']
def does_it_have_p(list):
    for brand in list:
        if 'p' in brand:
            print(bool(brand))
        else:
            print('False')
does_it_have_p(list_of_brands_without_letter_p)

