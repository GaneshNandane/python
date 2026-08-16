# simple program to demonstrate the use of command line arguments
import argparse

# Create an ArgumentParser object to handle command-line arguments
parser = argparse.ArgumentParser()

# Define the first positional argument and provide a description for it
parser.add_argument("arg1", help="description of argument 1")

# Define the second positional argument and provide a description for it
parser.add_argument("arg2", help="description of argument 2")

# Parse the given arguments and store them in the args object
args = parser.parse_args(["hello", "world"])

# Print the value of the first argument
print(args.arg1)

# Print the value of the second argument
print(args.arg2)
