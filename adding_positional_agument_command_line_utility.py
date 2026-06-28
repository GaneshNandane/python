import argparse
parser = argparse.ArgumentParser()
parser.add_argument("Positional", help = "description of positional  argument")
args = parser.parse_args()
print(args.Positional )