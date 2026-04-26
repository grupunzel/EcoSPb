from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def back_to_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='🔎 Посмотреть свои жалобы', callback_data='show_complaint')],
            [InlineKeyboardButton(text='🔙 Назад в меню', callback_data='back_to_main')],
        ]
    )

def back() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='🔙 Назад в меню', callback_data='back_to_main')],
        ]
    )

def skip_photo_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='⏩ Пропустить', callback_data='skip_photo')],
        ]
    )