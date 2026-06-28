# Importing the argparse module to create command-line interfaces.
# Creating an ArgumentParser object to define and parse command-line arguments.

import argparse
parser = argparse.ArgumentParser()

# Defining an optional command-line argument.
parser.add_argument("-o", "--optional",
                    help="Description of the optional argument.",
                    default="default_value")

# Parsing the command-line arguments.
args = parser.parse_args()

# Displaying the value of the optional argument.
print(args.optional)
