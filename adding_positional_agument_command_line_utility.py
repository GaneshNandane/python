# Importing the argparse module to create command-line interfaces.
# Creating an ArgumentParser object to define and parse command-line arguments.

import argparse
parser = argparse.ArgumentParser()

# Adding a required positional command-line argument.
parser.add_argument(
    "Positional",
    help="Description of the positional argument."
)

# Parsing the command-line arguments provided by the user.
args = parser.parse_args()

# Printing the value of the positional argument.
print(args.Positional)
