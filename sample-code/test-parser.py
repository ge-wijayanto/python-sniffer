import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-x', type=int)
parser.add_argument('-y', type=int)

args = parser.parse_args()

sum = args.x + args.y
print(sum)