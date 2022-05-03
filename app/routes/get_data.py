from app.core.friends import Friends

data = {
    "Ana": ["Carlos", "Vinicius", "Maria", "João"],
    "Carlos": ["Ana"],
    "Maria": ["Ana", "Vinicius"],
    "Vinicius": ["Maria", "Ana"],
    "João": ["Luiza", "Ana"],
    "Luiza": ["João"]
}

async def get_data():
    friends = Friends(data)
    yield friends
