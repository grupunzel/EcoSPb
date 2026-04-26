from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='♻️ Как утилизировать?', callback_data='utilization_question')],
            [InlineKeyboardButton(text='📌 Пункты сбора отходов', callback_data='container_map')],
            [InlineKeyboardButton(text='🖼️ Определить по фото', callback_data='photo_detection')],
            [InlineKeyboardButton(text='📢 Отправить жалобу', callback_data='send_complaint')],
        ]
    )