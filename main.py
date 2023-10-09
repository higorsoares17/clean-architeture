from fastapi import FastAPI
from configs.environment import get_environment_variables
from routers.v1.health import HealthRouter
from routers.v1.user import UserRouter

env = get_environment_variables()
app = FastAPI(
    title=env.APP_NAME,
    version=env.API_VERSION
)

app.include_router(HealthRouter)
app.include_router(UserRouter)

