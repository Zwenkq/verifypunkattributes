import json
import random
import sys

import name_generator

with open('attributes.json') as f:
    attributes_db = json.load(f)

def get_type(character):
    types = ['Alien', 'Vampire', 'Ape', 'Skeleton', 'Orc', 'Mummy', 'Zombie', 'Demon', 'Robot', 'Clown', 'Human']
    character['attributes']['type'] = (random.choices(types, weights=(0.03, 0.03, 0.1, 0.03, 0.03, 0.03, 0.3, 0.03, 0.05, 0.5, 85), k=1))[0]


def get_gender(character):
    genderes = ['Male', 'Female']
    character['attributes']['gender'] = (random.choices(genderes, weights=(60, 40), k=1))[0]


def get_body(character):
    if character['attributes']['type'] == 'Human':
        bodies = [item for item, attribute in attributes_db['body'].items() if attribute['variants'].get(character['attributes']['gender'].lower(), False) and item.startswith('Human')]
        character['attributes']['full_type'] = random.choice(bodies)
    else:
        character['attributes']['full_type'] = character['attributes']['type']

    character['images']['body'] = attributes_db['body'][character['attributes']['full_type']]['variants'][character['attributes']['gender'].lower()]


def get_hair(character):
    random_number = random.uniform(0, 100)
    if random_number > 0.75:
        hairs = [item for item, attribute in attributes_db['hair'].items() if attribute['variants'].get(character['attributes']['gender'].lower(), False) and not attribute.get('rare', False) ]
    else:
        hairs = [item for item, attribute in attributes_db['hair'].items() if attribute['variants'].get(character['attributes']['gender'].lower(), False) and attribute.get('rare', False) ]

    character['attributes']['hair'] = random.choice(hairs)

    character['images']['hair'] = attributes_db['hair'][character['attributes']['hair']]['variants'][character['attributes']['gender'].lower()]


def get_eyes(character):
    random_number = random.uniform(0, 100)
    if random_number > 0.3:
        eyes = [item for item, attribute in attributes_db['eyes'].items() if attribute['variants'].get(character['attributes']['gender'].lower(), False) and not attribute.get('rare', False) ]
    else:
        eyes = [item for item, attribute in attributes_db['eyes'].items() if attribute['variants'].get(character['attributes']['gender'].lower(), False) and attribute.get('rare', False) ]
    
    character['attributes']['eyes'] = random.choice(eyes)

    character['images']['eyes'] = attributes_db['eyes'][character['attributes']['eyes']]['variants'][character['attributes']['gender'].lower()]


def get_facial_hair(character):
    facial_hair = list(attributes_db['facial_hair'].keys())

    if character['attributes']['gender'] == 'Male':
        character['attributes']['facial_hair'] = random.choice(list(facial_hair))


    if character['attributes']['gender'] == 'Female':
        roll = random.uniform(0,100)
        if roll <= 0.5:
            character['attributes']['facial_hair'] = random.choice(list(facial_hair))
        else:
            return -1

    character['images']['facial_hair'] = attributes_db['facial_hair'][character['attributes']['facial_hair']]['variants'][character['attributes']['gender'].lower()]


def get_ears(character):
    ears = list(attributes_db['ear'].keys())
    character['attributes']['ear'] = random.choice(ears)

    character['images']['ear'] = attributes_db['ear'][character['attributes']['ear']]['variants'][character['attributes']['gender'].lower()]


def get_neck(character):
    random_number = random.uniform(0, 100)
    if random_number > 5:
        return -1

    necks = [item for item, attribute in attributes_db['neck'].items() if attribute['variants'].get(character['attributes']['gender'].lower(), False)]
    character['attributes']['neck'] = random.choice(necks)

    character['images']['neck'] = attributes_db['neck'][character['attributes']['neck']]['variants'][character['attributes']['gender'].lower()]


def get_mouth(character):
    random_number = random.uniform(0, 100)
    if random_number > 50 and character['attributes']['gender'].lower() == 'male' :
        return -1

    mouths = [item for item, attribute in attributes_db['mouth'].items() if attribute['variants'].get(character['attributes']['gender'].lower(), False)]
    character['attributes']['mouth'] = random.choice(mouths)

    character['images']['mouth'] = attributes_db['mouth'][character['attributes']['mouth']]['variants'][character['attributes']['gender'].lower()]


def get_mouth_prop(character):
    random_number = random.uniform(0, 100)
    if random_number > 15 and character['attributes']['gender'].lower() == 'male':
        return -1
    elif random_number > 5 and character['attributes']['gender'].lower() == 'female':
        return -1

    random_number = random.uniform(0, 100)
    if random_number > 2:
        mouth_props = [item for item, attribute in attributes_db['mouth_prop'].items() if attribute['variants'].get(character['attributes']['gender'].lower(), False) and not attribute.get('rare', False) ]
    else:
        mouth_props = [item for item, attribute in attributes_db['mouth_prop'].items() if attribute['variants'].get(character['attributes']['gender'].lower(), False) and attribute.get('rare', False) ]

    character['attributes']['mouth_prop'] = random.choice(mouth_props)

    character['images']['mouth_prop'] = attributes_db['mouth_prop'][character['attributes']['mouth_prop']]['variants'][character['attributes']['gender'].lower()]


def get_blemish(character):
    random_number = random.uniform(0, 100)
    if random_number > 30:
        return -1

    blemishes = [item for item, attribute in attributes_db['blemish'].items() if attribute['variants'].get(character['attributes']['gender'].lower(), False)]
    character['attributes']['blemish'] = random.choice(blemishes)

    character['images']['blemish'] = attributes_db['blemish'][character['attributes']['blemish']]['variants'][character['attributes']['gender'].lower()]


def get_nose(character):
    random_number = random.uniform(0, 100)
    if random_number > 4:
        return -1

    character['attributes']['nose'] = 'Clown Nose'
    character['images']['nose'] = attributes_db['nose'][character['attributes']['nose']]['variants'][character['attributes']['gender'].lower()]


def get_profession(character):
    random_number = random.uniform(0,100)

    if random_number < 0.1:
        rare_professions = ['Reward Pool Farmer', 'Hand Model', 'Stripper', 'Pornography Historian']
        character['attributes']['Profession'] = random.choice(rare_professions)

    lines = open('professions.txt').read().splitlines()
    character['attributes']['profession'] = random.choice(lines)


def get_border(character):
    hive_red = '#E31337'
    borders = ['lightsteelblue', hive_red ]
    character['attributes']['border'] = random.choices(borders, weights=(99, 10000), k=1)[0]


def get_name(character):
    character['attributes']['name'] = name_generator.generate_name(character['attributes']['gender'])


def get_accessories(character):
    accessories_quantity = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    accessories_count = (random.choices(accessories_quantity, weights=(0.05, 2, 35, 45, 15, 4, 1, 0.05, 0.02), k=1))[0]

    accessories_list = [get_facial_hair, get_hair, get_eyes, get_mouth, get_mouth_prop, get_nose, get_ears, get_neck, get_blemish]
    random.shuffle(accessories_list)

    for accessory in accessories_list:
        if accessories_count == 0:
            break

        if accessory(character) != -1:
            accessories_count -= 1

    character['attributes']['accessory_count'] = len(character['attributes']) - 4 # non-accessory attributes


def create_punk(border):
    character = {}
    character['images'] = {}
    character['attributes'] = {}

    get_type(character)
    get_gender(character)
    get_body(character)
    get_name(character)
    get_accessories(character)
    get_profession(character)

    if border:
        get_border(character)

    return character


def generate(border=None):
    return create_punk(border)


def main():
    random.seed(sys.argv[1])
    print(generate())


if __name__ == "__main__":
    main()