from collections import defaultdict
from datetime import datetime

from models.dish import DishModel
from models.ingredient import IngredientModel, KbhuModel
from models.menu import MenuModel, WeekMenuModel

# Неделя 1 Пятница

# Dish 1
ingredients1 = [
    IngredientModel(name="Куриное филе", amount=1.7, unit="кг"),
    IngredientModel(name="Болгарский перец", amount=0.8, unit="кг"),
    IngredientModel(name="Морковь", amount=0.6, unit="кг"),
    IngredientModel(name="Лук", amount=0.4, unit="кг"),
    IngredientModel(name="Соевый соус", amount=0.1, unit="л"),
    IngredientModel(name="Уксус рисовый", amount=0.12, unit="л"),
    IngredientModel(name="Сахар", amount=0.15, unit="кг"),
    IngredientModel(name="Томатный сок", amount=0.25, unit="л"),
    IngredientModel(name="Растительное масло", amount=0.05, unit="л"),
    IngredientModel(name="Крахмал", amount=2, unit="ст.л"),
    IngredientModel(name="Рис", amount=1.2, unit="кг"),
]

recipe1 = """Нарежьте куриное филе кубиками, обжарьте до золотистой корочки.
Нарежьте овощи, обжарьте с курицей.
В отдельной миске смешайте соевый соус, уксус, сахар, томатный сок и крахмал.
Залейте соус в сковороду, тушите 10 минут.
Отварите рис.
Подавайте с 1 куриным стейком (взрослому), 0.5 — ребёнку."""

kbhju1 = KbhuModel(calories=350, protein=25, fat=10, carbs=40)

dish1 = DishModel(
    id=1,
    name="Кисло-сладкая курица с рисом",
    ingredients=ingredients1,
    recipe=recipe1,
    kbhju_per_portion=kbhju1,
    portions=12
)

# Dish 2
ingredients2 = [
    IngredientModel(name="Картофель", amount=2.5, unit="кг"),
    IngredientModel(name="Молоко", amount=0.6, unit="л"),
    IngredientModel(name="Масло сливочное", amount=0.1, unit="кг"),
    IngredientModel(name="Куриный фарш", amount=1.3, unit="кг"),
    IngredientModel(name="Лук", amount=0.3, unit="кг"),
    IngredientModel(name="Томатная паста", amount=0.2, unit="кг"),
    IngredientModel(name="Вода", amount=0.4, unit="л"),
    IngredientModel(name="Соль", amount=0, unit="по вкусу"),
    IngredientModel(name="Перец", amount=0, unit="по вкусу"),
]

recipe2 = """Сварите картофель, сделайте пюре с молоком и сливочным маслом.
Фарш + мелко нарезанный лук + соль = сформируйте тефтели.
Обжарьте тефтели, добавьте томатную пасту и воду. Тушите 15–20 мин.
Подавайте с пюре и 1 куриным стейком."""

kbhju2 = KbhuModel(calories=300, protein=20, fat=12, carbs=30)

dish2 = DishModel(
    id=2,
    name="Картофельное пюре с тефтелями",
    ingredients=ingredients2,
    recipe=recipe2,
    kbhju_per_portion=kbhju2,
    portions=12
)

# Dish steak
ingredients_steak = [
    IngredientModel(name="Куриное филе", amount=1.35, unit="кг"),
    IngredientModel(name="Соль", amount=0, unit="по вкусу"),
    IngredientModel(name="Чесночный порошок", amount=0, unit="по вкусу"),
    IngredientModel(name="Паприка", amount=0, unit="по вкусу"),
    IngredientModel(name="Перец", amount=0, unit="по вкусу"),
]

recipe_steak = """Нарежьте филе на стейки (по 150 г).
Замаринуйте в специях (без масла).
Обжарьте на гриле / в духовке 200°C 20 минут или на сковороде гриль.
Храните в контейнерах. Подавайте к каждому приёму пищи."""

kbhju_steak = KbhuModel(calories=165, protein=31, fat=3.6, carbs=0)

dish_steak = DishModel(
    id=9,
    name="Куриные стейки",
    ingredients=ingredients_steak,
    recipe=recipe_steak,
    kbhju_per_portion=kbhju_steak,
    portions=9
)

menu_friday1 = MenuModel(week=1, day="Пятница", dishes=[dish1, dish2, dish_steak])

# Dish 3
ingredients3 = [
    IngredientModel(name="Макароны", amount=0.9, unit="кг"),
    IngredientModel(name="Куриное филе", amount=1.05, unit="кг"),
    IngredientModel(name="Морковь", amount=0.3, unit="кг"),
    IngredientModel(name="Лук", amount=0.3, unit="кг"),
    IngredientModel(name="Сливки 10%", amount=0.4, unit="л"),
    IngredientModel(name="Томатная паста", amount=0.2, unit="кг"),
    IngredientModel(name="Масло", amount=0.05, unit="л"),
]

recipe3 = """Нарежьте курицу и овощи, обжарьте.
Добавьте сливки и томатную пасту, тушите 10–15 минут.
Отварите макароны, соедините.
Подавайте с куриным стейком."""

kbhju3 = KbhuModel(calories=320, protein=22, fat=11, carbs=35)

dish3 = DishModel(
    id=3,
    name="Макароны с курицей в сливочно-томатном соусе",
    ingredients=ingredients3,
    recipe=recipe3,
    kbhju_per_portion=kbhju3,
    portions=12
)

# Dish 4
ingredients4 = [
    IngredientModel(name="Картофель", amount=1.8, unit="кг"),
    IngredientModel(name="Куриное филе", amount=0.85, unit="кг"),
    IngredientModel(name="Лук", amount=0.3, unit="кг"),
    IngredientModel(name="Морковь", amount=0.3, unit="кг"),
    IngredientModel(name="Болгарский перец", amount=0.3, unit="кг"),
    IngredientModel(name="Масло", amount=0.05, unit="л"),
    IngredientModel(name="Зелень", amount=0, unit="по вкусу"),
    IngredientModel(name="Соль", amount=0, unit="по вкусу"),
]

recipe4 = """Обжарьте лук, морковь, перец.
Добавьте курицу и картофель, немного воды.
Тушите ~40 минут.
Подавайте с куриным стейком."""

kbhju4 = KbhuModel(calories=280, protein=18, fat=8, carbs=32)

dish4 = DishModel(
    id=4,
    name="Картофельное рагу с курицей",
    ingredients=ingredients4,
    recipe=recipe4,
    kbhju_per_portion=kbhju4,
    portions=12
)

menu_monday1 = MenuModel(week=1, day="Понедельник", dishes=[dish3, dish4, dish_steak])

# Неделя 2

# Dish 5
ingredients5 = [
    IngredientModel(name="Куриное филе", amount=1.7, unit="кг"),
    IngredientModel(name="Брокколи", amount=1, unit="кг"),
    IngredientModel(name="Лук", amount=0.4, unit="кг"),
    IngredientModel(name="Соус терияки", amount=0.3, unit="л"),
    IngredientModel(name="Рис", amount=1.2, unit="кг"),
]

recipe5 = """Нарежьте курицу и обжарьте с луком.
Добавьте брокколи, влейте соус, тушите 10 минут.
Отварите рис.
Подавайте с 1 стейком."""

kbhju5 = KbhuModel(calories=340, protein=26, fat=9, carbs=38)

dish5 = DishModel(
    id=5,
    name="Курица терияки с рисом и брокколи",
    ingredients=ingredients5,
    recipe=recipe5,
    kbhju_per_portion=kbhju5,
    portions=12
)

# Dish 6
ingredients6 = [
    IngredientModel(name="Картофель", amount=2.5, unit="кг"),
    IngredientModel(name="Молоко", amount=0.6, unit="л"),
    IngredientModel(name="Масло", amount=0.1, unit="кг"),
    IngredientModel(name="Фарш куриный", amount=1.3, unit="кг"),
    IngredientModel(name="Лук", amount=0.3, unit="кг"),
    IngredientModel(name="Яйцо", amount=2, unit="шт"),
    IngredientModel(name="Панировка", amount=0.1, unit="кг"),
]

recipe6 = """Сварите картофель, сделайте пюре.
Фарш + яйцо + лук, сформируйте котлеты, обваляйте в панировке.
Обжарьте или запеките.
Подавайте с пюре и стейком."""

kbhju6 = KbhuModel(calories=310, protein=21, fat=13, carbs=28)

dish6 = DishModel(
    id=6,
    name="Пюре с куриными котлетами",
    ingredients=ingredients6,
    recipe=recipe6,
    kbhju_per_portion=kbhju6,
    portions=12
)

menu_friday2 = MenuModel(week=2, day="Пятница", dishes=[dish5, dish6, dish_steak])

# Dish 7
ingredients7 = [
    IngredientModel(name="Макароны", amount=0.9, unit="кг"),
    IngredientModel(name="Куриное филе", amount=1.05, unit="кг"),
    IngredientModel(name="Сыр", amount=0.3, unit="кг"),
    IngredientModel(name="Морковь", amount=0.3, unit="кг"),
    IngredientModel(name="Лук", amount=0.3, unit="кг"),
    IngredientModel(name="Масло", amount=0.05, unit="л"),
]

recipe7 = """Обжарьте курицу с овощами.
Добавьте натёртый сыр.
Отварите макароны, смешайте.
Подавайте со стейком."""

kbhju7 = KbhuModel(calories=330, protein=23, fat=12, carbs=34)

dish7 = DishModel(
    id=7,
    name="Макароны с курицей и сыром",
    ingredients=ingredients7,
    recipe=recipe7,
    kbhju_per_portion=kbhju7,
    portions=12
)

# Dish 8
ingredients8 = [
    IngredientModel(name="Картофель", amount=1.8, unit="кг"),
    IngredientModel(name="Куриное филе", amount=0.85, unit="кг"),
    IngredientModel(name="Кабачок", amount=0.4, unit="кг"),
    IngredientModel(name="Болгарский перец", amount=0.3, unit="кг"),
    IngredientModel(name="Морковь", amount=0.3, unit="кг"),
    IngredientModel(name="Лук", amount=0.3, unit="кг"),
]

recipe8 = """Нарежьте и обжарьте овощи.
Добавьте курицу, немного воды.
Тушите до готовности (~40 мин)."""

kbhju8 = KbhuModel(calories=270, protein=19, fat=7, carbs=31)

dish8 = DishModel(
    id=8,
    name="Овощное рагу с курицей",
    ingredients=ingredients8,
    recipe=recipe8,
    kbhju_per_portion=kbhju8,
    portions=12
)

menu_monday2 = MenuModel(week=2, day="Понедельник", dishes=[dish7, dish8, dish_steak])

week_menu = WeekMenuModel(menus=[menu_friday1, menu_monday1, menu_friday2, menu_monday2])

# Функция для получения сегодняшнего меню
def get_today_menu() -> MenuModel:
    today = datetime.now().strftime("%A")  # English day
    # Map to Russian
    day_map = {
        "Friday": "Пятница",
        "Monday": "Понедельник",
    }
    day = day_map.get(today, "Пятница")  # Default to Friday
    week = 1 if datetime.now().isocalendar()[1] % 2 == 1 else 2
    for menu in week_menu.menus:
        if menu.day == day and menu.week == week:
            return menu
    return menu_friday1  # Default

# Функция для агрегации ингредиентов
def aggregate_ingredients(dishes: list[DishModel]) -> dict[str, dict]:
    aggregated = defaultdict(lambda: {"amount": 0, "unit": ""})
    for dish in dishes:
        for ing in dish.ingredients:
            if ing.amount > 0:  # Skip spices
                aggregated[ing.name]["amount"] += ing.amount
                aggregated[ing.name]["unit"] = ing.unit
    return dict(aggregated)

# Функция для покупки на неделю
def get_week_shopping_list(week: int) -> str:
    menus = [m for m in week_menu.menus if m.week == week]
    all_dishes = []
    for menu in menus:
        all_dishes.extend(menu.dishes)
    agg = aggregate_ingredients(all_dishes)
    shopping_list = "Список покупок на неделю:\n"
    for name, data in agg.items():
        shopping_list += f"- {name}: {data['amount']} {data['unit']}\n"
    return shopping_list

# Функция для покупки на блюдо
def get_dish_shopping_list(dish: DishModel) -> str:
    shopping_list = f"Список покупок для {dish.name}:\n"
    for ing in dish.ingredients:
        if ing.amount > 0:
            shopping_list += f"- {ing.name}: {ing.amount} {ing.unit}\n"
    return shopping_list
