from pydantic_settings import BaseSettings, SettingsConfigDict
import redis

class Env(BaseSettings):
    REDIS_URL: str

    model_config = SettingsConfigDict(
        env_file='.env',
        case_sensitive=False,
        extra='ignore'
    )

env = Env()

r = redis.Redis.from_url(env.REDIS_URL)