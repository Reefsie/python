firstname = 'Arif'
surname = 'Rahman'
age = 22
firstname2 = 'Oguzcan'
surname2 = 'Dogan'
age2 = 22
ar_list=[firstname, surname, age]
od_list=[firstname2, surname2, age2]

def get_age(list_of_persons_details):
    return 2022 - list_of_persons_details[2]

print(type(get_age))