from app.configuration.routes.routes import Routes
from app.internal.routes import user
from app.internal.routes import item


__routes__ = Routes(routers=(
    user.router,
    item.router
))
