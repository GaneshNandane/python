# this is the example of the multiple image downloader using multiprocessing 

# Import the ThreadPoolExecutor class to perform tasks concurrently using threads
import concurrent.futures

# Import the requests module to download data from the internet
import requests

# Import the os module to create directories and work with the operating system
import os

# Function to download an image from the given URL
def downloadFile(URL, name):
    # Display a message when the download starts
    print(f"Started Downloading {name}")

    # Send an HTTP GET request to the given URL
    response = requests.get(URL)

    # Open a file in binary write mode ('wb')
    # The downloaded image will be saved inside the "files" folder
    with open(f"files/file{name}.jpg", "wb") as f:
        # Write the downloaded image data into the file
        f.write(response.content)

    # Display a message after the download is complete
    print(f"Finished Downloading {name}")

    # Return a confirmation message
    return f"Downloaded file{name}"

# This block runs only when this file is executed directly
if __name__ == '__main__':

    # Create a folder named "files" if it does not already exist
    os.makedirs("files", exist_ok=True)

    # URL that generates a random image every time it is requested
    URL = "https://picsum.photos/2000/3000"

    # Create a list containing the same URL 10 times
    # Each thread will use one URL from this list
    l1 = [URL for _ in range(10)]

    # Create a list of numbers from 0 to 9
    # These numbers will be used as file names
    l2 = list(range(10))

    # Create a ThreadPoolExecutor to execute multiple downloads simultaneously
    with concurrent.futures.ThreadPoolExecutor() as executor:

        # Map the downloadFile() function to the two lists
        # downloadFile(l1[0], l2[0])
        # downloadFile(l1[1], l2[1])
        # ...
        # downloadFile(l1[9], l2[9])
        results = executor.map(downloadFile, l1, l2)

        # Print the return value of each completed download
        for r in results:
            print(r)
