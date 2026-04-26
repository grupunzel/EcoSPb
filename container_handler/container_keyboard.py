from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def choose_district() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='🏰 Петроградский', callback_data='petrogradsky_district'),
            InlineKeyboardButton(text='🏛️ Невский', callback_data='nevsky_district')],
            [InlineKeyboardButton(text='🏡 Красногвардейский', callback_data='krasnogvardeisky_district'),
            InlineKeyboardButton(text='🏭 Кировский', callback_data='kirovsky_district')],
            [InlineKeyboardButton(text='🌊 Приморский', callback_data='primorsky_district'),
            InlineKeyboardButton(text='🌳 Пушкинский', callback_data='pushkinsky_district')],
            [InlineKeyboardButton(text='🔙 Назад в меню', callback_data='back_to_main')]
        ]
    )

def back_to_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='🔙 Назад в меню', callback_data='container_map')],
        ]
    )