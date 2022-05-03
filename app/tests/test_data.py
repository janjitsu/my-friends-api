from app.core.friends import Friends

data = {
    "Ana": ["Carlos"],
    "Carlos": ["Ana", "Julia", "Peter"],
    "Julia": ["Carlos"],
    "Peter": ["Carlos"]
}

async def get_test_data():
    friends = Friends(data)
    yield friends


