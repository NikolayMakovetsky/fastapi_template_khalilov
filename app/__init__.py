from fastapi import FastAPI




def create_app(_=None) -> FastAPI:
    # _=None пишем, т.к. в некоторых версиях FastAPI uvicorn передает ему какой-то неопределенный аргумент,
    # который затем нигде не исп-ся, но из-за того, что мы его не принимаем, можно столкнуться с ошибкой
    app = FastAPI()
