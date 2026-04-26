from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def util_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='📍 Показать ближайшие пункты', callback_data='container_map')],
            [InlineKeyboardButton(text='💡 Задать еще вопрос', callback_data='utilization_question')],
            [InlineKeyboardButton(text='🔙 Назад в меню', callback_data='back_to_main')],
        ]
    )

def back_to_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='🔙 Назад в меню', callback_data='back_to_main')],
        ]
    )