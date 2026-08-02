import concurrent.futures
import requests
import os

def downloadFile(URL, name):
    print(f"Started Downloading {name}")
    response = requests.get(URL)
    with open(f"files/file{name}.jpg", "wb") as f:
        f.write(response.content)
    print(f"Finished Downloading {name}")
    return f"Downloaded file{name}"

if __name__ == '__main__':
    os.makedirs("files", exist_ok=True)

    URL = "https://picsum.photos/2000/3000"
    l1 = [URL for _ in range(10)]
    l2 = list(range(10))

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(downloadFile, l1, l2)
        for r in results:
            print(r)
