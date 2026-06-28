import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-n", type = int, help = "descripton of integer argument", required=True)
args = parser. parse_args()
print(args.n)