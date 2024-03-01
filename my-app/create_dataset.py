import requests
import pandas as pd
# Loop through each creature in the rest api
# Create DF for all attributes add "image column"
# Write to parquet files.

baseURL = "https://www.dnd5eapi.co"


payload = {}
headers = {
  'Accept': 'application/json'
}

# get all monster indicies
response = requests.request("GET", baseURL + "/api/monsters", headers=headers, data=payload)

print(response.text)

for i in response.text["results"]:
    # turn each monster into a row

    # first use index to get new request

    monsterURL = baseURL + "api/monsters"

    # convert image from url into numpy array or PIL image

    # save to parquet

    # upload to hugging face
