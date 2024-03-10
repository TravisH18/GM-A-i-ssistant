# models/monster.py

class Monster:
    def __init__(self, monster_data, lore_data):
        self.index = monster_data.get('index')
        self.name = monster_data.get('name')
        self.size = monster_data.get('size')
        self.alignment = monster_data.get('alignment')
        self.type = monster_data.get('type')
        self.armor_class = monster_data.get('armor_class')
        self.hit_points = monster_data.get('hit_points')
        self.speed = monster_data.get('speed')
        self.str = monster_data['strength'] # monster_data['ability_scores'][0]['value']
        self.dex = monster_data['dexterity'] # monster_data['ability_scores'][1]['value']
        self.con = monster_data['constitution'] # monster_data['ability_scores'][2]['value']
        self.int = monster_data['intelligence'] # monster_data['ability_scores'][3]['value']
        self.wis = monster_data['wisdom'] # monster_data['ability_scores'][4]['value']
        self.cha = monster_data['charisma'] # monster_data['ability_scores'][5]['value']
        self.special_abilities = monster_data.get('special_abilities')
        self.skills = monster_data.get('skills')
        self.senses = monster_data.get('senses')
        self.actions = monster_data.get('actions')
        self.languages = monster_data.get('languages')
        self.challenge = monster_data.get('challenge_rating')
        self.legendary_actions = monster_data.get('legendary_actions')
        #self.image = monster_data['image']
        self.description = lore_data

    def __str__(self): # Monster Prompt
        prompt = f"The {self.name} is a {self.size} {self.alignment} {self.type} with the following characteristics:\n"

        # Add basic information
        prompt += f"{self.description}\n. This creatures statististics are as follows:\n"
        # prompt += f"**Attributes**:\n"
        prompt += f"- Armor Class: {self.armor_class[0]["value"]} ({self.armor_class[0]["type"]}) "
        prompt += f"- Hit Points: {self.hit_points} "
        prompt += f"- Movement Speed: "
        for key, value in self.speed.items():
            prompt += f"{key.capitalize()} {value} "

        # Add ability scores
        # prompt += f"\n**Ability Scores**:\n"
        prompt += f"- Strength: {self.str} "
        prompt += f"- Dexterity: {self.dex} "
        prompt += f"- Constitution: {self.con} "
        prompt += f"- Intelligence: {self.int} "
        prompt += f"- Wisdom: {self.wis} "
        prompt += f"- Charisma: {self.cha} "

        # Add special abilities
        #prompt += f"\n**Special Abilities**:\n"
        prompt += f"The {self.name} has the following special abilities:\n"
        for ability in self.special_abilities:
            prompt += f"- {ability['name']}: {ability['desc']}\n"

        # Add actions
        # prompt += f"\n**Actions**:\n"
        prompt += f"The {self.name} can take the following actions:\n"
        for action in self.actions:
            prompt += f"- {action['name']}: {action['desc']}\n"

        if self.legendary_actions is not None:
            prompt += f"The {self.name} is a legendary creature and can take the following legendary actions:\n"
            for l_a in self.legendary_actions:
                prompt += f"- {l_a['name']}: {l_a['desc']}\n"

        return prompt