import requests
import os
from datasets import load_dataset
import pandas as pd
import pandas as pd
from models.Monster import Monster

def get_lore_data(lore_data, monster_row):
  lore = ''
  for source in lore_data:
    for row in source:
        if row["index"] == monster_row["index"]:
          for entry in row["entries"]:
            if "title" in entry.keys():
                lore += entry["title"] + ": "
            lore += entry["description"] + "\n"
  return lore
            
def compile_dataset(push_to_hub):
  data = []
  save_dir = "data"
  img_row_data = requests.get("https://raw.githubusercontent.com/alexandregpereira/Monster-Compendium-Content/main/json/monster-images.json").json()
  # monster_data = requests.get("https://raw.githubusercontent.com/alexandregpereira/Monster-Compendium-Content/main/json/monsters.json").json()
  lore_data = requests.get("https://raw.githubusercontent.com/alexandregpereira/Monster-Compendium-Content/main/json/en-us/monster-lore.json").json()
  # monsters_saved = dict()
  for row in img_row_data:
    if row["image_url"].find("default") == -1:
      # Download the image
      image_response = requests.get(row["image_url"])
      if image_response.status_code == 200:
          # Save the image with the row_id as the filename
          image_filename = f'{save_dir}/{row["monster_index"]}.png'
          image_path = os.path.join(os.getcwd(), save_dir, f"{row["monster_index"]}.png") # maybe add PATH class to interior string
          api_url = 'https://www.dnd5eapi.co'
          monster_data = requests.get(api_url + "/api/monsters").json()
          
          for m in monster_data["results"]:
           
            monster_url = api_url + m.get("url")
            monster_row = requests.get(monster_url).json()
            monster_lore = get_lore_data(lore_data, m)
            monster = Monster(monster_data=monster_row, lore_data=monster_lore)
            # print(monster)
            with open(image_path, 'wb') as image_file:
                image_file.write(image_response.content)
                data.append({'index': monster.index, 'file_name': image_filename, 'prompt': monster.__str__()}) 
                #monsters_saved.update({row["monster_index"]: image_filename}) 

  # api_url = 'https://www.dnd5eapi.co'
  # monster_data = requests.get(api_url + "/api/monsters").json()
  # for m in monster_data["results"]:
  #   if m["index"] in monsters_saved.keys():
  #     monster_url = api_url + m.get("url")
  #     monster_row = requests.get(monster_url).json()
  #     monster_lore = get_lore_data(lore_data, m)
  #     monster = Monster(monster_data=monster_row, lore_data=monster_lore)
      #  print(monster)
      # data.append({'index': monster.index, 'file_name': image_filename, 'prompt': monster.__str__()}) 
  
  if push_to_hub:
    df = pd.DataFrame.from_records(data=data)
    df.to_csv(os.path.join(save_dir, 'metadata.csv'))
    dataset = load_dataset("imagefolder", data_dir=save_dir)
    dataset.push_to_hub("TravisHudson/DND-Monster-Diffusion")

def compile_dataset(api_url, image_json_url):
  image_json_response = requests.get(image_json_url)
  if image_json_response.status_code == 200:
     image_data = image_json_response.content
     for i in image_data:
        # use json index to get image and ping api for data
        monster_response = requests.get(api_url + i["index"])
        monster_data = monster_response.content
        new_monster = Monster(monster_data)
   

if __name__ == "__main__":
  compile_dataset(push_to_hub=True)
