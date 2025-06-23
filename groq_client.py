import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
def stream_completion(messages: list, model="llama3-8b-8192"):
    try: 
        completion = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=False,
        response_format={"type": "json_object"},
        stop=None,
    )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"An error occurred while calling the Groq API: {e}")
        return '{"message": "Sorry, I had trouble connecting to my thoughts. Please try again."}'    
        
    