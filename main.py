from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import GameRequest, GameResponse
from session import initialize_session, update_session, session_store
from prompts import create_interaction_prompt, create_intro_prompt
from groq_client import stream_completion
import json

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post("/game", response_model=GameResponse)
def game_logic(request:GameRequest):
    session_id=request.session_id
    clicked_object=request.clicked_object
    if session_id not in session_store:
        scene_id=101
        description, session_objects= initialize_session(session_id, 5, scene_id)
        prompt = create_intro_prompt(description, session_objects)
        try: 
            response = stream_completion(prompt)
            response_json = json.loads(response)
            intro_text = response_json.get("intro_text", "[Missing intro text]")
        except json.JSONDecodeError:
            print(f"Error: Could not parse intro JSON from LLM for session {session_id}")
            intro_text = "Hello! Welcome to this cozy room. I have a few things for you to find. Let's begin!"   
        return GameResponse(
            message=intro_text,
            status="start",
        )

    status = update_session(session_id, clicked_object)
    session = session_store[session_id]
    prompt = create_interaction_prompt(
        description=session["description"],
        clicked_object=clicked_object,
        session_objects=session["session_objects"],
        found_objects=session["found_objects"],
        history=session["history"],
        status=status
    )
    try: 
        response_str = stream_completion(prompt)
        response_json = json.loads(response_str)
        interaction_msg = response_json.get("message", "Hmm, my thoughts are a bit tangled. What did you click again?")
    except json.JSONDecodeError:
        print(f"Error: Could not parse interaction JSON from LLM for session {session_id}")
        interaction_msg = f"You clicked the {clicked_object}. An interesting choice! Let's keep looking."
    return GameResponse(
        message=interaction_msg,
        status=status,
    )

@app.get("/")
def read_root():
    return {"message": "Focura backend is alive!"}   

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)