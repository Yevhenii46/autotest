import random

from data.data import Person
from faker import Faker

faker_en = Faker('En')

def generated_person():
    return Person(
    first_name = faker_en.first_name(),
    last_name = faker_en.last_name(),
    email = faker_en.email(),
    mobile = faker_en.first_name(),
    current_address = faker_en.msisdn(),
    subject = 'English'
    )

def generated_file():
    path = rf'C:\Users\007\PycharmProjects\autotest\venv\test{random.randint(10, 100)}.txt'
    file = open(path, 'w')
    file.write(f'Hello World{random.randint(25, 100)}')
    file.close()
    return path

