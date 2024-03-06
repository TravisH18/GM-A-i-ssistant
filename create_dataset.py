import requests
from bs4 import BeautifulSoup
import os
from datasets import load_dataset, Image
import pandas as pd

def make_prompt(data):
  prompt = f"The {data['name']} is a {data['size']} {data['alignment']} {data['type']} with the following characteristics:\n"

  # Add basic information
  # prompt += f"**Attributes**:\n"
  prompt += f"- Armor Class: {data['armor_class'][0]['value']} "
  prompt += f"- Hit Points: {data['hit_points']} "
  prompt += f"- Speed: {data['speed']} "

  # Add ability scores
  # prompt += f"\n**Ability Scores**:\n"
  prompt += f"- Strength: {data['strength']} "
  prompt += f"- Dexterity: {data['dexterity']} "
  prompt += f"- Constitution: {data['constitution']} "
  prompt += f"- Intelligence: {data['intelligence']} "
  prompt += f"- Wisdom: {data['wisdom']} "
  prompt += f"- Charisma: {data['charisma']} "

  # Add special abilities
  #prompt += f"\n**Special Abilities**:\n"
  prompt += f"The {data['name']} has the following special abilities:\n"
  for ability in data['special_abilities']:
      prompt += f"- {ability['name']}: {ability['desc']}\n"

  # Add actions
  # prompt += f"\n**Actions**:\n"
  prompt += f"The {data['name']} can take the following actions:\n"
  for action in data['actions']:
      prompt += f"- {action['name']}: {action['desc']}\n"

  # if legendary_action in data['legendary_actions']: 
  return prompt

def get_monster_image(img_div, save_directory, row_id, page):
  anchor_tag = img_div.find('a')
  if anchor_tag and 'href' in anchor_tag.attrs:
    # Construct the image URL
    image_url = anchor_tag['href']

    # Download the image
    image_response = requests.get(image_url)
    if image_response.status_code == 200:
        # Save the image with the row_id as the filename
        image_filename = f'{save_directory}/{row_id}.jpg'
        with open(image_filename, 'wb') as image_file:
            image_file.write(image_response.content)
        print(f"Image for row_id {row_id} on page {page} downloaded successfully.")
    else:
        print(f"Failed to download image for row_id {row_id} on page {page}.")
  else:
      print(f"No 'a' tag found for row_id {row_id} on page {page}.")

def compile_dataset(base_url, push_to_hub):
  df = pd.DataFrame()
  total_pages = 156
  rows_per_page = 20

  # Specify the directory where you want to save the images
  save_directory = 'data'
  os.makedirs(save_directory, exist_ok=True)

  for page in range(1, total_pages + 1):

    # Construct the URL for each page
    url = f'{base_url}?page={page}'
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
      soup = BeautifulSoup(response.text, 'html.parser')

      # Find all rows with the specified class
      rows = soup.find_all('div', class_='info')

      for row in rows:
        # Extract the data-slug attribute
        row_id = row['data-slug']

        # Find the first child div with class 'monster-icon'
        # Get Monster Image
        monster_icon_div = row.find('div', class_='monster-icon')
        
        if monster_icon_div:
          anchor_tag = monster_icon_div.find('a')

          if anchor_tag and 'href' in anchor_tag.attrs:
            # Construct the image URL
            image_url = anchor_tag['href']

            # Download the image
            image_response = requests.get(image_url)
            if image_response.status_code == 200:
                # Save the image with the row_id as the filename
                image_filename = f'{save_directory}/{row_id}.jpg'
                with open(image_filename, 'wb') as image_file:
                    image_file.write(image_response.content)
                print(f"Image for row_id {row_id} on page {page} downloaded successfully.")
            else:
                print(f"Failed to download image for row_id {row_id} on page {page}.")
          else:
              print(f"No 'a' tag found for row_id {row_id} on page {page}.")
          # if we made it here we have successfully downloaded the image
          # next we contruct the prompt by pinging rest api and passing data dict to function
          # define pandas dataframe with two columns 
          # cols = [filename, prompt]
          # df[row_id] = prompt

        
        
    # Commented out block
    # Following block will get individual monster page + info text from their unique page  
    #        # Construct the individual page URL using row_id  
    #     individual_page_url = f'{base_url}/{row_id}'
    #     individual_page_response = requests.get(individual_page_url)

    #     if individual_page_response.status_code == 200:
    #       # OR
    #       # Get image and the monsters name (index) and look up the remaining info on the Rest API
    #       individual_page_soup = BeautifulSoup(individual_page_response.text, 'html.parser')

    #       # Find the desired information in the specified div
    #       description_block_content = individual_page_soup.find('div', class_='mon-details__description-block-content')

    #       if description_block_content:
    #         # Extract and print the information
    #         #
    #         # This is all the information on one monster
    #         #
    #         information_text = description_block_content.get_text(strip=True)
    #         print(f"Information for row_id {row_id} on page {page}:\n{information_text}\n")

    #         # You can save the information to a file or process it as needed
    #       else:
    #           print(f"No 'mon-details__description-block-content' div found for row_id {row_id} on page {page}.")
    #     else:
    #       print(f"Failed to retrieve the individual page for row_id {row_id} on page {page}. Status code: {individual_page_response.status_code}")
    # else:
    #   print(f"Failed to retrieve the webpage for page {page}. Status code: {response.status_code}")
  if push_to_hub:
    dataset = load_dataset("imagefolder", data_dir="/data")
    dataset.push_to_hub("TravisHudson/DND-Monster-Diffusion")


if __name__ == "__main__":
  base_url = 'https://www.dndbeyond.com/monsters'
  # or use this
  # "https://github.com/alexandregpereira/Monster-Compendium-Content/blob/main/json/monster-images.json"

  compile_dataset(base_url, push_to_hub=False)
