from pydantic import Field
from pydantic_settings import BaseSettings


class PremiumCalculatorSettings(BaseSettings):
    rate_per_year: float = Field(default=0.005, gt=0)
    rate_per_value_step: float = Field(default=0.005, gt=0)
    value_step: float = Field(default=10000, gt=0)
    coverage_percentage: float = Field(default=1.0, gt=0, le=1)

    class Cofnig:
        env_file = ".env"
