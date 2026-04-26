from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def back_to_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='🔎 Что я умею распознавать?', callback_data='recognition_list')],
            [InlineKeyboardButton(text='🔙 Назад в меню', callback_data='back_to_main')],
        ]
    )

def photo_again() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='📍 Показать ближайшие пункты', callback_data='container_map')],
            [InlineKeyboardButton(text='📸 Прислать другое фото', callback_data='photo_detection')],
            [InlineKeyboardButton(text='🔙 Назад в меню', callback_data='back_to_main')],
        ]
    )

def back() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='🔙 Назад в меню', callback_data='photo_detection')],
        ]
    )