#tabbed interface for monsters, traps, hazards
import gradio as gr
from diffusers import DiffusionPipeline, EulerDiscreteScheduler

def save_creature(name_tb, type_tb, size_tb, cr_tb, ac_tb, passive_perception_tb,
        num_hit_dice, type_hit_dice, hp_bonus, average_hp, str_score, dex_score, int_score,
        con_score, wis_score, cha_score, special_abilities_tb, actions_tb,
        bonus_actions_tb, reactions_tb, legendary_actions_tb, lair_actions_tb,
        description_tb):
    return "Saved!"

def image_generator(name_tb, type_tb, size_tb, cr_tb, ac_tb, passive_perception_tb,
        num_hit_dice, type_hit_dice, hp_bonus, average_hp, str_score, dex_score, int_score,
        con_score, wis_score, cha_score, special_abilities_tb, actions_tb,
        bonus_actions_tb, reactions_tb, legendary_actions_tb, lair_actions_tb,
        description_tb):
    model_id = "0xJustin/Dungeons-and-Diffusion"
    scheduler = EulerDiscreteScheduler.from_pretrained(model_id, subfolder="scheduler")
    pipe = DiffusionPipeline.from_pretrained(model_id, scheduler=scheduler, use_safetensors=True).to("cuda")
    # https://huggingface.co/docs/diffusers/tutorials/basic_training
    additional_info = [
        name_tb, type_tb, size_tb, cr_tb, ac_tb, passive_perception_tb,
        num_hit_dice, type_hit_dice, hp_bonus, average_hp, str_score, dex_score, int_score,
        con_score, wis_score, cha_score, special_abilities_tb, actions_tb,
        bonus_actions_tb, reactions_tb, legendary_actions_tb, lair_actions_tb,
        description_tb
    ]
    end_prompt = ' '.join([str(elem) for elem in additional_info])
    prompt = "A dungeons and dragons monster." + end_prompt
    image = pipe(prompt, num_inference_steps=25).images[0]
    return image

with gr.Blocks(title="Homebrew Monster Modal") as creature_modal:
    with gr.Row(equal_height=True): # Row 1
        name_tb = gr.Textbox(label="Monster Name", placeholder="Enter name") # show_label=True
        type_tb = gr.Textbox(label="Monster Type", placeholder="beast, abberation, dragon, etc.")
        size_tb = gr.Dropdown(label="Size", choices=["small", "medium", "large", "huge", "gargantuan"])
        cr_tb = gr.Dropdown(label="Challenge Rating", choices=[x for x in range(1, 31)])
    with gr.Row(equal_height=True): # Row 2
        with gr.Column(scale=1): # Row 2 Col 1
            ac_tb = gr.Textbox(label="Armor Class", placeholder="#")
            passive_perception_tb = gr.Textbox(label="Passive Perception", placeholder="#")
            num_hit_dice = gr.Textbox(label="Hit Dice", placeholder="#") #dropdown select to automate average hp
            type_hit_dice = gr.Dropdown(label="Type of hitdice", choices=["d4", "d6", "d8", "d10", "d12", "d20", "d100"])
            hp_bonus = gr.Textbox(label="HP Bonus", placeholder="Equal to number of hit dice * con modifier") # put ability scores first so we can automate this
            average_hp = gr.Textbox(label="Average HP", placeholder="Avg of hit dice * hp bonus")
        with gr.Column(scale=1): # Row 2 Col 2
            str_score = gr.Textbox(label="STR Score", placeholder="#")
            dex_score = gr.Textbox(label="DEX Score", placeholder="#")
            con_score = gr.Textbox(label="CON Score", placeholder="#")
            int_score = gr.Textbox(label="INT Score", placeholder="#")
            wis_score = gr.Textbox(label="WIS Score", placeholder="#")
            cha_score = gr.Textbox(label="CHA Score", placeholder="#")
    with gr.Row(equal_height=True): # Row 3
        with gr.Column(scale=2): # Row 3 Col 1
            special_abilities_tb = gr.Textbox(label="Special Traits", placeholder="Enter name of ability and its description ", lines=5)
        with gr.Column(scale=2): # Row 3 Col 2
            actions_tb = gr.Textbox(label="Actions", placeholder="Enter name of action and its description ", lines=5)
    with gr.Row(equal_height=True): # Row 4
        with gr.Column(scale=2): # Row 4 Col 1
            bonus_actions_tb = gr.Textbox(label="Bonus Actions", placeholder="Enter name of the bonus action and its description ", lines=3)
        with gr.Column(scale=2): # Row 4 Col 2
            reactions_tb = gr.Textbox(label="Reactions", placeholder="Enter name of the reaction and its description ", lines=3)
    with gr.Row(equal_height=True): # Row 5
        with gr.Column(scale=2): # Row 5 Col 1
            legendary_actions_tb = gr.Textbox(label="Legendary Actions", placeholder="Enter name of the legendary action and its description ", lines=3)
        with gr.Column(scale=2): # Row 5 Col 2
            lair_actions_tb = gr.Textbox(label="Lair Actions", placeholder="Enter name of the lair action and its description ", lines=3)
    with gr.Row(equal_height=True): # Row 6
        description_tb = gr.Textbox(label="Monster Description", placeholder="Describe the monster here. Be as detailed as possible.")
    input_components = [
        name_tb, type_tb, size_tb, cr_tb, ac_tb, passive_perception_tb,
        num_hit_dice, type_hit_dice, hp_bonus, average_hp, str_score, dex_score, int_score,
        con_score, wis_score, cha_score, special_abilities_tb, actions_tb,
        bonus_actions_tb, reactions_tb, legendary_actions_tb, lair_actions_tb,
        description_tb
    ]
    gen_art_btn = gr.Button("Generate Creature").click(image_generator, inputs=input_components, outputs="image")
    save_btn = gr.Button("Save Creature").click(save_creature, inputs=input_components, output="text")

# creature_modal.launch(debug=True)
    
if __name__ == "__main__":
    # modals = []
    
    # tab_names = ["Monster", "Trap", "Hazard"]
    # output = gr.ImageEditor()
    # modal = gr.TabbedInterface(modals)

    creature_modal.launch(debug=True)

    # for mounting to specific url
    # CUSTOM_PATH = "/gradio"
    # from server import app
    # gr.mount_gradio_app(app, creature_modal, path=CUSTOM_PATH)
    # Or embed in an iframe

