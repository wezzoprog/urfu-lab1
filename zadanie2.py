import datetime
year = datetime.datetime.today().year

def born_year(age):
    return year - age

name = str(input('Введите имя: '))
age = int(input('Введите возраст: '))
city = str(input('Введите город: '))
country = str(input('Введите страну: '))

print(f'Уважаемый {name}! \nНа сегодняшний день Вы проживаете в стране {country}, в городе {city}, и вы родились в {born_year(age)}')
