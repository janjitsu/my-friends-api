from pydantic import BaseModel

class AddFriendRequest(BaseModel):
    name: str
    friends: list
