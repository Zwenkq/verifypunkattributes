import pprint
import random
import requests
import sys

import attributegenerator

pp = pprint.PrettyPrinter(indent=4)

if len(sys.argv) == 3:
    txid = sys.argv[1]
    quantity = sys.argv[2]

if len(sys.argv) == 2:
    txid = sys.argv[1]
    quantity = "1"

block_num = requests.get(f'https://api.ausbit.dev/tx/{txid}').json()['block_num']
block_data = requests.get(f'https://api.ausbit.dev/block/{block_num}').json()

for _ in range(int(quantity)):
    random_seed = block_data['block_id'] + block_data['previous'] + txid + '-' + str(_)
    random.seed(random_seed)
    pp.pprint(attributegenerator.generate(random_seed)['attributes'])