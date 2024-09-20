from fastapi import FastAPI
from app.configuration.routes import __routes__


class Server:

    __app: FastAPI

    def __init__(self, app: FastAPI):
        self.__app = app
        self.__register_routes(app)

    def get_app(self) -> FastAPI:
        return self.__app

    # статический метод не относится ни к атрибутам экземпляра, ни к атрибутам самого класса
    @staticmethod
    def __register_events(app):
        """Приватный статический метод регистрации событий"""
        ...

    @staticmethod
    def __register_routes(app):
        """Приватный статический метод регистрации путей"""
        __routes__.register_rotes(app)
