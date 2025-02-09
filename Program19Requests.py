# First program of Requests.

import requests

def main():
    response = requests.get("https://api.artic.edu/api/v1/artworks/search")

    print (response)

main()


#response 200 means the program is running as it should be !