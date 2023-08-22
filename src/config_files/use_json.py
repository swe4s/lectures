import argparse
import json

parser = argparse.ArgumentParser()

parser.add_argument('--config', type=str, required=True)
args = parser.parse_args()

f = open(args.config, 'r')
config = json.load(f)
f.close()

print(config['a'], config['b'], config['c'])
