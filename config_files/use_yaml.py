import argparse
import yaml

parser = argparse.ArgumentParser()

parser.add_argument('--config', type=str, required=True)
args = parser.parse_args()

f = open(args.config, 'r')
config = yaml.load(f, Loader=yaml.FullLoader)
f.close()

print(config['a'], config['b'], config['c'])
