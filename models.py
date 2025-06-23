from pydantic import BaseModel
from typing import Optional, List

class GameRequest(BaseModel):
    session_id: int
    scene_id:int
    clicked_object: Optional[str]=None  #None if first time

class GameResponse(BaseModel):
    message: str
    status:str #correct,wrong,repeat,start
