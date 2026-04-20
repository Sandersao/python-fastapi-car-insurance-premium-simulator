from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    application_name = Field(default="Car Insurance API")
    application_description: str = Field(default="Car Insurance Premium Simulator API")

    class Cofnig:
        env_file = ".env"
