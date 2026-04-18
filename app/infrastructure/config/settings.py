import os

class Settings:
    application_name = os.getenv("APP_NAME", 'Car Insurance API')

    rate_per_year = float(os.getenv("RATE_PER_YEAR", 0.005))
    rate_per_value_step = float(os.getenv("RATE_PER_VALUE_STEP", 0.005))
    value_step = float(os.getenv("VALUE_STEP", 10000))
    coverage_percentage = float(os.getenv("COVERAGE_PERCENTAGE", 1.0))