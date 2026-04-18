import random


class GISService:
    def get_risk_adjustment(self, location: str) -> float:
        return random.uniform(-0.02, 0.02)
