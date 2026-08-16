import argparse
parser = argparse.ArgumentParser()
parser.add_argument("arg1", help = "description of argument 1")
parser.add_argument("arg2", help = "description of argument 2")
args = parser.parse_args(["hello", "world"])
print(args.arg1)
print(args.arg2)