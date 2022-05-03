from fastapi import APIRouter, HTTPException, Depends
from app.routes.requests import AddFriendRequest
from app.routes.get_data import get_data

router = APIRouter(dependencies=[Depends(get_data)])

@router.get("/friends")
async def get_friends(friends = Depends(get_data)):
    return friends.all()

@router.post("/friends", status_code=201)
async def add_friend(request: AddFriendRequest, friends = Depends(get_data)):
    try:
        friends.add(request.name, request.friends)
        return {"message": "Success"}
    except Exception as e:
        raise HTTPException(status_code=400, detail={"message": str(e)})

@router.get("/friends/{name}")
async def get_friends_of(name: str, friends = Depends(get_data)):
    try:
        return friends.of(name)
    except Exception as e:
        raise HTTPException(status_code=400, detail={"message": str(e)})

@router.get("/friends/{name}/related")
async def get_related_of(name: str, friends = Depends(get_data)):
    try:
        return friends.related(name)
    except Exception as e:
        raise HTTPException(status_code=400, detail={"message": str(e)})

