# Importing the argparse module to create command-line interfaces.
# Creating an ArgumentParser object to define and parse command-line arguments.

import argparse
parser = argparse.ArgumentParser()

# Adding a required integer command-line argument.
parser.add_argument(
    "-n",
    type=int,
    help="Description of the integer argument.",
    required=True
)

# Parsing the command-line arguments.
args = parser.parse_args()

# Printing the value of the integer argument.
print(args.n)
