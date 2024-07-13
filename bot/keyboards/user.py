import json

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def generate_main_menu(is_admin=False):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🔎 Камеры", callback_data='cams'),
               InlineKeyboardButton("👤 Профиль", callback_data='profile'))
    markup.add(InlineKeyboardButton("🎬 Кино", callback_data='kino'),
               InlineKeyboardButton("⭐ Избранное", callback_data='favorites'))
    markup.add(InlineKeyboardButton("❔ Инфо", callback_data='info'))

    if is_admin:
        admin_button = InlineKeyboardButton("🛠️ Админ панель", callback_data='admin')
        markup.add(admin_button)

    return markup

def generate_keyboard_info():
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton("Разработчик", url="https://github.com/reques6e"))

    return markup

back_button = InlineKeyboardButton("⁉️ Главное меню", callback_data='back_to_start')
keyboard = InlineKeyboardMarkup().add(back_button)