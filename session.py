from typing import Dict, List
import random
scene_overview="A sunlit, cozy bedroom bursts with life and color. Large windows framed by soft blue curtains let in abundant natural light, illuminating a bed covered in pastel bedding and surrounded by lush green plants. The wooden floor is adorned with a vibrant patterned rug, and the walls and shelves are filled with books, framed artwork, and eclectic decorations. The room feels warm, inviting, and creative, with a harmonious mix of nature, art, and comfort"
scene_objects={
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
}
session_store:Dict[str, Dict]={}

def initialize_session(session_id:int, num_objects:int, scene_id:int):  
    selected_objects=random.sample(list(scene_objects.keys()),num_objects)
    description=scene_overview + "\n\nHere are all objects in the room:\n\n"
    for name, desc in scene_objects.items():
        description += f"- {name}: {desc}\n"
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