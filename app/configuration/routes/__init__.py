from app.configuration.routes.routes import Routes
from app.internal.routes import user

__routes__ = Routes(routers=(user.router, )) # все, механизм регистрации тут готов