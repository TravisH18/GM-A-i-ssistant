# models/monster.py

class Monster:
    def __init__(self, name, size, type, alignment, armor_class, hit_points, speed, strength, dexterity, constitution, intelligence, wisdom, charisma, abilities, skills, senses, actions, languages, challenge, legendary_actions, description, image=None):
        self.name = name
        self.size = size
        self.alignment = alignment 
        self.type = type
        self.armor_class = armor_class
        self.hit_points = hit_points
        self.speed = speed
        self.str = strength
        self.dex = dexterity
        self.con = constitution
        self.int = intelligence
        self.wis = wisdom
        self.cha = charisma
        self.special_abilities = abilities
        self.skills = skills
        self.senses = senses
        self.action = actions
        self.languages = languages
        self.challenge = challenge
        self.description = description
        self.legendary_actions = legendary_actions
        self.image = image

    def __str__(self): # Monster Prompt
        prompt = f"The {self.name} is a {self.size} {self.alignment} {self.type} with the following characteristics:\n"

        # Add basic information
        prompt += f"{self.description}\n. This creatures statististics are as follows:\n"
        # prompt += f"**Attributes**:\n"
        prompt += f"- Armor Class: {self.armor_class[0]['value']} "
        prompt += f"- Hit Points: {self.hit_points} "
        prompt += f"- Speed: {self.speed} "

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
