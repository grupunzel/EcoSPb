from aiogram import Router, types, F
from aiogram.filters import CommandStart
from main_handler.main_keyboard import main_keyboard

router = Router()

@router.message(CommandStart())
async def send_welcome(message: types.Message):
    await message.answer("""♻️ Привет! Я ЭкоСПб — помощник по раздельному сбору отходов в Санкт-Петербурге.

Что я умею:
🌱 Узнать, как утилизировать предмет
📍 Показать пункты приёма
📸 Определить отходы по фото
📩 Отправить жалобу на переполненный контейнер

Выберите действие:""", reply_markup=main_keyboard())

@router.callback_query(F.data == "back_to_main")
async def back_to_main(callback: types.CallbackQuery):
    await callback.message.edit_text("""♻️ Привет! Я ЭкоСПб — помощник по раздельному сбору отходов в Санкт-Петербурге.

Что я умею:
🌱 Узнать, как утилизировать предмет (по названию)
📍 Показать пункты приёма
📸 Определить отходы по фото
📩 Отправить жалобу на переполненный контейнер

Выберите действие:""", reply_markup=main_keyboard())
        
