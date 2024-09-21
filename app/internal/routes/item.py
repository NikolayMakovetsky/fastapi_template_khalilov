from fastapi import APIRouter


router = APIRouter(
    prefix='/api/item'
)


@router.get('/')
def get_items():

    return [
        {"id": 1, "ItemName": "item1"},
        {"id": 2, "ItemName": "item2"},
        {"id": 3, "ItemName": "item3"}
    ]