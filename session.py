from typing import Dict, List
import random
scenes={
101:{"scene_overview":"A sunlit, cozy bedroom bursts with life and color. Large windows framed by soft blue curtains let in abundant natural light, illuminating a bed covered in pastel bedding and surrounded by lush green plants. The wooden floor is adorned with a vibrant patterned rug, and the walls and shelves are filled with books, framed artwork, and eclectic decorations. The room feels warm, inviting, and creative, with a harmonious mix of nature, art, and comfort",
"scene_objects":{
"acoustic guitar":
"An acoustic guitar with a natural wood finish rests upright against the side of the bed, its strings catching the sunlight streaming through the window. Positioned near the center of the room, it stands out as a creative centerpiece.",
"vintage radio":
"A retro-style radio sits on the floor at the bottom left corner, next to the bed. Its dark casing and dials add a nostalgic touch, blending into the cozy, eclectic atmosphere.",
"red book":
"A small red book with a white spine is tucked on a shelf to the right of the window, partially hidden among other books. Its bold color makes it pop out in the otherwise earthy-toned bookshelf.",
"rug":
"A vibrant, patterned rug lies on the wooden floor at the foot of the bed. The rug features a playful, abstract face and geometric designs, adding warmth and personality to the room.",
"cactus plant":
"A tiny cactus in a green pot sits on the shelf to the left of the bed, near the window. Its spiky form is distinct among the leafy plants, offering a subtle detail for careful observers.",
"plants ceiling":
"Longest vine trails from a pot hanging from a rope at the upper-left corner, where the curtain meets the wooden wall. Tendrils spill downward, overlapping the teal drape and skimming the edge of the orange artwork.",
"plants bookshelf":
"A small plant in a brown pot is nestled among the books on the right bookshelf, its leaves reaching out between the spines. This plant is easy to overlook amid the crowded shelf.",
"orange artwork":
"A framed piece of art with a bold orange motif hangs on the left wall above the bedside shelf. Its warm colors and abstract shapes draw the eye upward.",
"plants floor":
"A leafy green plant in a black pot sits on the floor to the right of the rug, near the orange cushion. Its placement by the bed and rug makes it a subtle but grounding element.",
"framed artwork":
"A rectangular framed artwork with green and blue hues is mounted on the left wall, just above the bedside shelf. Its cool tones contrast with the warmer decor around it.",
"windowsill plants":
"A large, bushy plant in a terracotta pot dominates the windowsill, its leaves catching the sunlight. This plant is central in the image, bridging the indoors and the lush greenery outside.",
"orange cushion bed":
"A bright orange cushion with a star pattern rests on the bed, near the right edge. Its vivid color makes it one of the most eye-catching objects in the room."
}},
102:{"scene_overview":"Morning light floods a rustic, sky-blue kitchen. Weather-worn cabinets wrap the L-shaped counters that frame a wide, open window, revealing a lush tropical hillside beneath a bright, cloud-dotted sky. Sunbeams pour through the window, striping the wooden plank floor and spotlighting produce, cookware, and greenery that give the room a lived-in, breezy charm. The right wall holds the cooking zone—stove, range hood, and hanging utensils—while the left side is dotted with open shelves, stacked crockery, and trailing plants. Splashes of sunny yellow—from towels to potholders—punctuate the predominantly blue palette, creating a warm, inviting workspace that feels both practical and idyllic.",
"scene_objects":{
"table":
"A short, round side table sits in the extreme lower-right corner of the room, just in front of the oven. Its pale wooden top supports a small metal pot",
"saucepan":
"Near the lower-left bend of the counter, a silver saucepan with a lid rests on the white, marble-flecked surface. It catches the sunlight coming through the window, making its handles and rim gleam against the blue cabinetry below.",
"oven":
"Built into the right run of cabinets, the black-framed oven occupies the lower-right quadrant of the scene. Its glass door reflects the light on the floor",
"pile of fruits":
"Centered on the counter directly under the window, a small heap of red fruits lies beside a cutting board, adding a burst of color where the sunlight is brightest.",
"chimney":
"A stainless range hood is mounted high on the right wall, jutting out above the stove. Its metallic surface is tilted slightly downward and framed by hanging ladles and red pans.",
"plastic bucket":
"A cream-colored plastic bucket (doubling as a waste bin) nestles at the base of the cabinets, a little right of center, where the blue paint is most weathered.",
"towels":
"Two mustard-yellow dish towels hang from cabinet handles along the lower-left base units, swaying slightly and echoing the other yellow accents in the kitchen.",
"plates":
"On the narrow wall shelf just left of the window, a neat stack of off-white plates leans against the blue wall, partially shaded by a potted plant above.",
"stove":
"Set into the right countertop, the four-burner stovetop holds a pair of shiny saucepots. Its black grates and knobs align with the oven directly beneath.",
"yellow potholders":
"Two bright yellow, diamond-shaped potholders dangle side-by-side on hooks to the immediate right of the window frame, positioned at eye level above the counter items.",
"blue cabinet":
"The weather-beaten, sky-blue base cabinets span the entire lower half of the image—from beneath the left counter, across the sink area, and along the right wall—showing chipped paint, sturdy black hinges, and deep relief panels that define the kitchen’s rustic character."
}},
103:{"scene_overview":"Sun-washed turquoise cabinets line a narrow galley kitchen that opens directly onto a balcony drenched in greenery and a distant, rolling horizon. Golden daylight streams through the open double doors, striping the terracotta floor tiles and spotlighting baskets of produce, hanging copper pans, and trailing plants that lend the room a breezy, lived-in charm. Shelves crowded with crockery, a ceiling fan under a timber roof, and well-used utensils complete a space that feels equal parts rustic and idyllic, perfectly poised between indoors and the lush world outside",
"scene_objects":{
"stool": "Two slender wooden bar stools stand side-by-side just inside the doorway on the right, their pale legs planted in the sunlit path between the blue cabinets and the open door.",
"ceiling fan": "A compact three-blade ceiling fan with light beige blades hangs from the center of the wooden plank ceiling, its pull-cord dangling toward the room’s midpoint.",
"pineapple": "A whole pineapple sits on the left counter beneath the hanging mugs, its spiky crown poking toward the tiled backsplash just left of the sink area.",
"red kettle": "The glossy red kettle rests near the front edge of the left counter, its curved spout angled toward the centre of the kitchen and catching a glint of sunlight.",
"towel": "A soft yellow dish towel drapes from the handle of the bottom-left cabinet door, fluttering almost to the floor beside the cupboard frame.",
"red flowering plant": "A pot bursting with vivid scarlet blooms is perched on the far-right countertop,creating a bright focal accent amid the turquoise cabinetry.",
"plant floor": "A tall leafy houseplant in a clay pot rises from the extreme lower-left corner of the scene, its fronds arching toward the counter and partially lit by the doorway glow.",
"teacups": "Multiple white teacups rest in a neat row directly above the left counter on a wooden shelf ",
"cutlery holder": "A silver cylinder packed with knives and wooden spoons stands between the sink and the pineapple on the left countertop, its tools fanning outward for easy reach.",
"hanging copper pots": "Two round copper pans gleam on the right wall in a vertical line just beyond the doorway frame, reflecting stray beams of light at eye level.",
"colander": "A large perforated metal colander hangs high on the left wall, almost level with the top of the window frame, its bowl angled outward and catching the daylight."
}}
}
session_store:Dict[str, Dict]={}

def initialize_session(session_id:int, num_objects:int, scene_id:int):
    scene = scenes[scene_id] 
    all_objects = scene["scene_objects"] 
    overview = scene["scene_overview"]  
    selected_objects=random.sample(list(all_objects),min(num_objects, len(all_objects)))
    description=overview + "\n\nHere are all objects in the room:\n\n"
    for obj_name, obj_desc in all_objects.items():
        description += f"- {obj_name}: {obj_desc}\n"
    session_store[session_id]={
        "scene_id": scene_id,
        "description":description,
        "session_objects":selected_objects,
        "found_objects":[],
        "history":[],
    }
    return description, selected_objects

def update_session(session_id:int, clicked_object:str):
    session=session_store[session_id]
    session["history"].append(clicked_object)
    if clicked_object in session["found_objects"]:
        return "repeat"
    if clicked_object in session["session_objects"]:
        session["found_objects"].append(clicked_object)
        return "correct"
    return "wrong"