from pydantic import BaseModel

from .dish import DishModel


class MenuModel(BaseModel):
    week: int
    day: str
    dishes: list[DishModel]


class WeekMenuModel(BaseModel):
    menus: list[MenuModel]
