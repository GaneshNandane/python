import argparse
parcer = argparse.ArgumentParser()
parcer.add_argument("-o", "--optional", help = "description of optional argument", default = "default_value")
args = parcer.parse_args()
print(args.optional)