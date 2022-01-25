from pydantic import BaseSettings


class Settings(BaseSettings):
    class Config:
        env_prefix = "TODO_APP_"
        env_file = ".env"

    app_title: str = "Todo"

    redis_host: str = "localhost"
    redis_port: int = 6379
    redis_password: str = ""
