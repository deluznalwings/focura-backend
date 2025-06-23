def create_intro_prompt(description: str, session_objects: list[str]) -> list[dict]:
    system_msg = {
        "role": "system",
        "content": (
            "You are a super summarizer which takes a complete description of a scene and a list of objects and then provides the summary of the scene covering only the objects mentioned in the list of objects"
            "Use easy words and give helpful clues about 5 target objects"
            "Do not mention any other objects that are not in the target list."
            "The story should make it easier for the player to guess and remember what to look for."
            "Your answer must be in this format ONLY: {\"intro_text\": \"...\"}. Do not include markdown or explanation.Respond ONLY with valid minified JSON (single line, double quotes, no trailing commas). Keep it concise and suitable for a first game level."
        )
    }

    user_msg = {
        "role": "user",
        "content": (
            f"The room looks like this: {description}\n\n"
            f"THE 5 HIDDEN OBJECTS ARE: {', '.join(session_objects)}\n\n"
            f"Please write a short, simple intro spanning 60-70 words dropping information about the 5 HIDDEN OBJECTS taking help of the DESCRIPTION that gives clues about these items in simple language."
            "Use easy words and give helpful clues about 5 target objects"
            "Your entire response MUST be a single, valid JSON object and nothing else. "
            "Do not add any text, explanation, or markdown code fences before or after the JSON object. "
            "Your answer must be in this format ONLY: {\"intro_text\": \"...\"}"
    
            
        )
    }

    return [system_msg, user_msg]


def create_interaction_prompt(description: str, clicked_object: str, session_objects: list[str], found_objects: list[str], history: list[str], status: str) -> list[str]:
    system_msg = {
        "role": "system",
        "content": (
            "You are a story-driven interaction engine for a hidden-object game. Based on the user's actions, you continue the story in an immersive, imaginative tone. If the user clicks the right object, respond with affirmation and progress the narrative and optionally share a fun fact or bit of lore about the object. If they click something already found, gently remind them. If they click a wrong object, encourage exploration and gently let them know and provide a hint related to one of the remaining target objects. Utilize the spatial information of objects provided in the description. For a wrong click, if one of the remaining session object lies besides this wrong click, drop a subtle hint about it. Respond ONLY with a valid JSON object in this format and nothing else:{\"message\": \"..\"}"
            "Do not include markdown or explanation.Respond ONLY with valid minified JSON (single line, double quotes, no trailing commas)."
            "Your entire response MUST be a single, valid JSON object and nothing else."
            "Do not add any text, explanation, or markdown code fences before or after the JSON object."
        )
    }
    user_msg = {
        "role": "user",
        "content": (
            f"The description of the scene is: {description}\n"
            f"The player just clicked on: {clicked_object}\n"
            f"This object was a: {status.upper()} click.\n"
            f"Objects found so far: {', '.join(found_objects) if found_objects else 'None'}\n"
            f"Previous clicks (in order): {', '.join(history)}\n\n"
            "Respond with a narrative continuation. Keep it brief (2–3 lines)."
            "Respond ONLY with a valid JSON object in this format and nothing else:{\"message\": \"..\"}"
            "Your entire response MUST be a single, valid JSON object and nothing else. "
            "Do not add any text, explanation, or markdown code fences before or after the JSON object. "
            "Do not include markdown or explanation.Respond ONLY with valid minified JSON (single line, double quotes, no trailing commas)."
        )
        
    }
    return [system_msg, user_msg]
