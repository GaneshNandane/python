# Downloading files from the web using the requests and argparse modules.

# This program defines a function named download_file() that downloads a file from a given URL. If no output filename is provided, the program extracts
# the filename from the URL by splitting the URL using the '/' separator and selecting the last element using the index [-1].

# The requests.get() function sends an HTTP GET request to the specified URL. The parameter stream=True downloads the file in small chunks instead of
# loading the entire file into memory at once. Each chunk (8 KB in this case) is written to the output file in binary mode ('wb').

# The argparse module is used to create a command-line interface (CLI), allowing the user to specify the URL of the file and an optional output filename when
# running the program from the terminal.
import argparse
import requests

def download_file(url, local_filename=None):
    if local_filename is None:
        local_filename = url.split('/')[-1]  # Use last part of URL as filename

    with requests.get(url, stream=True) as r:  # Start the request
        r.raise_for_status()  # Raise an error if the request fails
        with open(local_filename, 'wb') as f:  # Open file for writing
            for chunk in r.iter_content(chunk_size=8192):  # Read in chunks
                f.write(chunk)
    
    return local_filename

# Argument Parsing
parser = argparse.ArgumentParser()
parser.add_argument("url", help="URL of the file to download")
parser.add_argument("-o", "--output", help="Name of the file", default=None)

args = parser.parse_args()

print("Downloading:", args.url)
print("Saving as:", args.output if args.output else "Using default filename")

download_file(args.url, args.output)
