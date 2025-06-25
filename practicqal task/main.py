# csv და faker მოდულების გამოყენებით გააკეთეთ შემდეგი დავალება:
# persons.csv ფაილში ჩაწერეთ 50 პიროვნება შემდეგი ფორმატით:
#
# ID, first_name, last_name, age
# 1, john, smith, 25
# 2, Bob, white, 35
# ...
#
# და ასე შემდეგ. რათქმაუნდა ხელით არ უნდა ჩამოწეროთ აიდები, სახელი-გვარები და ასაკი.
# ასაკს რაც შეეხება, უნდა იყოს 20 დან 80 შუალედში.
# აუცილებლად გამოიყენეთ DictWriter!


import csv
import random
import faker
fake = faker.Faker()

person_data = ['ID', 'first_name', 'last_name', 'age']

with open('persons.csv', 'w', newline='') as file:

    writer = csv.DictWriter(file, fieldnames=person_data)

    writer.writeheader()
    # writer.writerows(person_data)

    for i in range(1, 51):
        writer.writerow({
            'ID': i,
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'age': random.randint(20, 80)
    })

print(i, fake.first_name(), fake.last_name())





