from pydantic import BaseModel

from .ingredient import IngredientModel, KbhuModel

class DishModel(BaseModel):
    id: int
    name: str
    ingredients: list[IngredientModel]
    recipe: str
    kbhju_per_portion: KbhuModel
    portions: int
