from fastapi import APIRouter


router = APIRouter(
    prefix='/api/v1'  # это то с чего будет начинаться каждый наш путь
)


@router.get('/hello')
def user_hello():

    return {
        "hello": "world"
    }
