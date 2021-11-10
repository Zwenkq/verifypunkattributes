import random

female_names = open('./names/female.txt', 'r').read().splitlines()
male_names = open('./names/male.txt', 'r').read().splitlines()
last_names = open('./names/last.txt', 'r').read().splitlines()

def generate_name(gender):
    if gender.lower() == 'male':
        return f"{random.choice(male_names)} {random.choice(last_names)}"
    else:
        return f"{random.choice(female_names)} {random.choice(last_names)}"
