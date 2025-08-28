from pydantic import BaseModel

class IngredientModel(BaseModel):
    name: str
    amount: float
    unit: str
    # Placeholder for KBHU per 100g
    calories_per_100g: float = 0.0
    protein_per_100g: float = 0.0
    fat_per_100g: float = 0.0
    carbs_per_100g: float = 0.0

class KbhuModel(BaseModel):
    calories: float
    protein: float
    fat: float
    carbs: float
