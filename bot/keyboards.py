from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data import week_menu

# Главное меню
def main_menu_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text="Что приготовить сегодня", callback_data="today_menu")],
        [InlineKeyboardButton(text="Калорийность блюда сегодня", callback_data="today_kbhju")],
        [InlineKeyboardButton(text="Что приготовить на выбор", callback_data="choose_dish")],
        [InlineKeyboardButton(text="Калорийность выбранного блюда", callback_data="choose_kbhju")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

# Клавиатура для выбора блюда
def choose_dish_keyboard() -> InlineKeyboardMarkup:
    buttons = []
    for menu in week_menu.menus:
        for dish in menu.dishes:
            buttons.append([InlineKeyboardButton(text=dish.name, callback_data=f"dish_{dish.id}")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)

# Клавиатура для блюда
def dish_keyboard(dish_id: int) -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text="Вернуться в меню недели", callback_data="back_to_week")],
        [InlineKeyboardButton(text="Калорийность блюда", callback_data=f"kbhju_{dish_id}")],
        [InlineKeyboardButton(text="Список продуктов для покупки", callback_data=f"shop_{dish_id}")],
        [InlineKeyboardButton(text="Посмотреть следующее блюдо недели", callback_data=f"next_dish_{dish_id}")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
