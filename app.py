cities = ['Москва', 'Париж', 'Лондон']

users = [{'name': 'Иван', 'age': 35},
         {'name': 'Мария', 'age': 22},
         {'name': 'Соня', 'age': 20}]

tourists = [{'user': users[0], 'city': cities[2]},
            {'user': users[1], 'city': cities[0]},
            {'user': users[2], 'city': cities[1]}]

city = input('Введите город: ')

if city.title() == cities[0]:
    tourists_name = tourists[1]['user']
    tourists_city = tourists[1]['city']
    print(f"Турист {tourists_name['name']} возраст {tourists_name['age']}. Посетил город {tourists_city}")
elif city.title() == cities[1]:
    tourists_name = tourists[2]['user']
    tourists_city = tourists[2]['city']
    print(f"Турист {tourists_name['name']} возраст {tourists_name['age']}. Посетил город {tourists_city}")
elif city.title() == cities[2]:
    tourists_name = tourists[0]['user']
    tourists_city = tourists[0]['city']
    print(f"Турист {tourists_name['name']} возраст {tourists_name['age']}. Посетил город {tourists_city}")
else:
    print("Такого города нет!")