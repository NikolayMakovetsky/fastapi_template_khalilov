from dataclasses import dataclass
from fastapi import FastAPI


__all__ = ['Routes']  # метод, кот.вернет нам наш класс при импорте в другом месте (избегаем тавтологии)
# создаем именно dataclass т.к. он будет принимать и хранить в атрибутах определенные пути,
# которые мы будем затем регистрировать


@dataclass(frozen=True)  # frozen class неизменяемый
class Routes:
    routes: tuple

    def register_routes(self, app: FastAPI):
        """Функция регистрирующая роутер в наше приложение"""

        for router in self.routes:
            app.include_router(router)
