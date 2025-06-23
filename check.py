import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

try:
    response = client.chat.completions.create(
        model="deepseek-r1-distill-llama-70b",
        messages=[{"role": "user", "content": "You are a game assistant helping players find hidden objects in a room. "
            "Your job is to write a short 3-4 line introduction describing the scene simply. "
            "Use easy words and give helpful clues about 5 target objects, but do NOT name them directly. "
            "Do not mention any other objects that are not in the target list. "
            "The story should make it easier for the player to guess and remember what to look for."
            "Your answer must be in this format ONLY: {\"intro_text\": \"...\"}. Do not include markdown or explanation.Respond ONLY with valid minified JSON (single line, double quotes, no trailing commas). Keep it concise and suitable for a first game level."
            "scene_overview A sunlit, cozy bedroom bursts with life and color. Large windows framed by soft blue curtains let in abundant natural light, illuminating a bed covered in pastel bedding and surrounded by lush green plants. The wooden floor is adorned with a vibrant patterned rug, and the walls and shelves are filled with books, framed artwork, and eclectic decorations. The room feels warm, inviting, and creative, with a harmonious mix of nature, art, and comfort"
            ""
            "guitar"
"An acoustic guitar with a natural wood finish rests upright against the side of the bed, its strings catching the sunlight streaming through the window. Positioned near the center of the room, it stands out as a creative centerpiece."
"radio"
"A retro-style radio sits on the floor at the bottom left corner, next to the bed. Its dark casing and dials add a nostalgic touch, blending into the cozy, eclectic atmosphere."
"red book"
"A small red book with a white spine is tucked on a shelf to the right of the window, partially hidden among other books. Its bold color makes it pop out in the otherwise earthy-toned bookshelf."
"rug"
"A vibrant, patterned rug lies on the wooden floor at the foot of the bed. The rug features a playful, abstract face and geometric designs, adding warmth and personality to the room."
"cactus"
"A tiny cactus in a green pot sits on the shelf to the left of the bed, near the window. Its spiky form is distinct among the leafy plants, offering a subtle detail for careful observers."
"hanging plant bookshelf"
"A lush green plant dangles from a pot on the top right corner of the bookshelf, its vines cascading down and mingling with the books. It brings a sense of life and nature into the reading nook."
"flowerpot bookshelf"
"A small plant in a brown pot is nestled among the books on the right bookshelf, its leaves reaching out between the spines. This plant is easy to overlook amid the crowded shelf."
"orange artwork"
"A framed piece of art with a bold orange motif hangs on the left wall above the bedside shelf. Its warm colors and abstract shapes draw the eye upward."
"flowerpot floor"
"A leafy green plant in a black pot sits on the floor to the right of the rug, near the orange cushion. Its placement by the bed and rug makes it a subtle but grounding element."
"framed artwork"
"A rectangular framed artwork with green and blue hues is mounted on the left wall, just above the bedside shelf. Its cool tones contrast with the warmer decor around it."
"windowsill plant"
"A large, bushy plant in a terracotta pot dominates the windowsill, its leaves catching the sunlight. This plant is central in the image, bridging the indoors and the lush greenery outside."
"orange cushion"
"A bright orange cushion with a star pattern rests on the bed, near the right edge. Its vivid color makes it one of the most eye-catching objects in the room."
            
"the selected objects are flowerpot floor, windowsill plant, radio"}],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        response_format={"type": "json_object"},
        stream=False,
    )
    print("✅ API key is valid.")
    print("Response:", response.choices[0].message.content)
except Exception as e:
    print("❌ API key is invalid or something went wrong:")
    print(e)