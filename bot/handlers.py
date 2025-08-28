from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from .keyboards import main_menu_keyboard, choose_dish_keyboard, dish_keyboard
from data import get_today_menu, week_menu, get_dish_shopping_list

router = Router()

@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Добро пожаловать в бот для планирования питания!", reply_markup=main_menu_keyboard())

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from .keyboards import choose_dish_keyboard, dish_keyboard, main_menu_keyboard
from data import get_dish_shopping_list, get_today_menu, week_menu

router = Router()

@router.message(Command("start"))
async def start_handler(message: Message) -> None:
    await message.answer("Добро пожаловать в бот для планирования питания!", reply_markup=main_menu_keyboard())

@router.callback_query(F.data == "today_menu")
async def today_menu_handler(callback: CallbackQuery) -> None:
    menu = get_today_menu()
    text = f"Меню на сегодня ({menu.day}, неделя {menu.week}):\n"
    for dish in menu.dishes:
        text += f"- {dish.name}\n"
    await callback.message.edit_text(text, reply_markup=main_menu_keyboard())

@router.callback_query(F.data == "today_kbhju")
async def today_kbhju_handler(callback: CallbackQuery) -> None:
    menu = get_today_menu()
    text = f"КБЖУ на сегодня ({menu.day}, неделя {menu.week}):\n"
    for dish in menu.dishes:
        k = dish.kbhju_per_portion
        text += f"{dish.name}: {k.calories} ккал, {k.protein} г белка, {k.fat} г жира, {k.carbs} г углеводов\n"
    await callback.message.edit_text(text, reply_markup=main_menu_keyboard())

@router.callback_query(F.data == "choose_dish")
async def choose_dish_handler(callback: CallbackQuery) -> None:
    await callback.message.edit_text("Выберите блюдо:", reply_markup=choose_dish_keyboard())

@router.callback_query(F.data == "choose_kbhju")
async def choose_kbhju_handler(callback: CallbackQuery) -> None:
    await callback.message.edit_text("Выберите блюдо для просмотра КБЖУ:", reply_markup=choose_dish_keyboard())

@router.callback_query(F.data.startswith("dish_"))
async def dish_handler(callback: CallbackQuery) -> None:
    dish_id = int(callback.data.split("_")[1])
    dish = None
    for menu in week_menu.menus:
        for d in menu.dishes:
            if d.id == dish_id:
                dish = d
                break
    if dish:
        text = f"{dish.name}\n\nРецепт:\n{dish.recipe}"
        await callback.message.edit_text(text, reply_markup=dish_keyboard(dish_id))

@router.callback_query(F.data.startswith("kbhju_"))
async def kbhju_handler(callback: CallbackQuery) -> None:
    dish_id = int(callback.data.split("_")[1])
    dish = None
    for menu in week_menu.menus:
        for d in menu.dishes:
            if d.id == dish_id:
                dish = d
                break
    if dish:
        k = dish.kbhju_per_portion
        text = (f"КБЖУ для {dish.name} (на порцию):\n"
                f"{k.calories} ккал\n"
                f"{k.protein} г белка\n"
                f"{k.fat} г жира\n"
                f"{k.carbs} г углеводов")
        await callback.message.edit_text(text, reply_markup=dish_keyboard(dish_id))

@router.callback_query(F.data.startswith("shop_"))
async def shop_handler(callback: CallbackQuery) -> None:
    dish_id = int(callback.data.split("_")[1])
    dish = None
    for menu in week_menu.menus:
        for d in menu.dishes:
            if d.id == dish_id:
                dish = d
                break
    if dish:
        text = get_dish_shopping_list(dish)
        await callback.message.edit_text(text, reply_markup=dish_keyboard(dish_id))

@router.callback_query(F.data == "back_to_week")
async def back_to_week_handler(callback: CallbackQuery) -> None:
    await callback.message.edit_text("Главное меню:", reply_markup=main_menu_keyboard())

@router.callback_query(F.data.startswith("next_dish_"))
async def next_dish_handler(callback: CallbackQuery) -> None:
    dish_id = int(callback.data.split("_")[2])
    # Simple next: find next id
    next_id = dish_id + 1 if dish_id < 8 else 1
    dish = None
    for menu in week_menu.menus:
        for d in menu.dishes:
            if d.id == next_id:
                dish = d
                break
    if dish:
        text = f"{dish.name}\n\nРецепт:\n{dish.recipe}"
        await callback.message.edit_text(text, reply_markup=dish_keyboard(next_id))

@router.callback_query(F.data == "today_kbhju")
async def today_kbhju_handler(callback: CallbackQuery):
    menu = get_today_menu()
    text = f"КБЖУ на сегодня ({menu.day}, неделя {menu.week}):\n"
    for dish in menu.dishes:
        k = dish.kbhju_per_portion
        text += f"{dish.name}: {k.calories} ккал, {k.protein} г белка, {k.fat} г жира, {k.carbs} г углеводов\n"
    await callback.message.edit_text(text, reply_markup=main_menu_keyboard())

@router.callback_query(F.data == "choose_dish")
async def choose_dish_handler(callback: CallbackQuery):
    await callback.message.edit_text("Выберите блюдо:", reply_markup=choose_dish_keyboard())

@router.callback_query(F.data == "choose_kbhju")
async def choose_kbhju_handler(callback: CallbackQuery):
    await callback.message.edit_text("Выберите блюдо для просмотра КБЖУ:", reply_markup=choose_dish_keyboard())

@router.callback_query(F.data.startswith("dish_"))
async def dish_handler(callback: CallbackQuery):
    dish_id = int(callback.data.split("_")[1])
    dish = None
    for menu in week_menu.menus:
        for d in menu.dishes:
            if d.id == dish_id:
                dish = d
                break
    if dish:
        text = f"{dish.name}\n\nРецепт:\n{dish.recipe}"
        await callback.message.edit_text(text, reply_markup=dish_keyboard(dish_id))

@router.callback_query(F.data.startswith("kbhju_"))
async def kbhju_handler(callback: CallbackQuery):
    dish_id = int(callback.data.split("_")[1])
    dish = None
    for menu in week_menu.menus:
        for d in menu.dishes:
            if d.id == dish_id:
                dish = d
                break
    if dish:
        k = dish.kbhju_per_portion
        text = f"КБЖУ для {dish.name} (на порцию):\n{k.calories} ккал\n{k.protein} г белка\n{k.fat} г жира\n{k.carbs} г углеводов"
        await callback.message.edit_text(text, reply_markup=dish_keyboard(dish_id))

@router.callback_query(F.data.startswith("shop_"))
async def shop_handler(callback: CallbackQuery):
    dish_id = int(callback.data.split("_")[1])
    dish = None
    for menu in week_menu.menus:
        for d in menu.dishes:
            if d.id == dish_id:
                dish = d
                break
    if dish:
        text = get_dish_shopping_list(dish)
        await callback.message.edit_text(text, reply_markup=dish_keyboard(dish_id))

@router.callback_query(F.data == "back_to_week")
async def back_to_week_handler(callback: CallbackQuery):
    await callback.message.edit_text("Главное меню:", reply_markup=main_menu_keyboard())

@router.callback_query(F.data.startswith("next_dish_"))
async def next_dish_handler(callback: CallbackQuery):
    dish_id = int(callback.data.split("_")[2])
    # Simple next: find next id
    next_id = dish_id + 1 if dish_id < 8 else 1
    dish = None
    for menu in week_menu.menus:
        for d in menu.dishes:
            if d.id == next_id:
                dish = d
                break
    if dish:
        text = f"{dish.name}\n\nРецепт:\n{dish.recipe}"
        await callback.message.edit_text(text, reply_markup=dish_keyboard(next_id))
