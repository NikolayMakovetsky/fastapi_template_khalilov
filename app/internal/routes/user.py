from fastapi import APIRouter


router = APIRouter(
    prefix='/api/user'
)


@router.get('/')
def get_users():

    return [
        {"id": 1, "Username": "user1"},
        {"id": 2, "Username": "user2"},
        {"id": 3, "Username": "user3"}
    ]


@router.get('/hello')
def user_hello():

    return {
        "hello": "world"
    }
