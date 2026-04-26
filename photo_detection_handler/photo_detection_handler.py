from aiogram import Router, types, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states import EcoStates
import asyncio
from photo_detection_handler.photo_detection_keyboard import back_to_menu, photo_again, back
from utilization_handler.utilization_handler import run_animation
from ai_handler.photo_detection.photo_agent import photo_detection

router = Router()

@router.callback_query(F.data == "photo_detection")
async def back_to_main(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(EcoStates.waiting_for_photo_detection)
    await callback.message.edit_text("""📸 Отправьте мне фото предмета, а я скажу, как его правильно утилизировать! 🙋‍♂️
                                     
👉🏻👈🏻 Пока я умею хорошо распозновать только некоторые предметы. Чтобы узнать какие, нажмите на кнопку ниже 👇🏻""", reply_markup=back_to_menu())
    await callback.answer()

@router.message(EcoStates.waiting_for_photo_detection, F.photo)
async def process_photo(message: Message, state: FSMContext):
    processing_message = await message.answer("🤔 Думаю над ответом...")
        
    animation_task = asyncio.create_task(
        run_animation(message.bot, message.chat.id, processing_message.message_id)
    )

    photo = message.photo[-1]
    file = await message.bot.get_file(photo.file_id)
    file_bytes = await message.bot.download_file(file.file_path)
    try:
        bot_answer = await photo_detection(file_bytes.getvalue())
        animation_task.cancel()
        try:
            await message.bot.delete_message(chat_id=message.chat.id, message_id=processing_message.message_id)
        except Exception:
            pass

        await message.answer(bot_answer, parse_mode="Markdown", reply_markup=photo_again())
        await state.clear()
    
    except Exception as e:
        await message.answer("Ошибка чтения фото.", parse_mode="Markdown", reply_markup=photo_again())
        await state.clear()

@router.callback_query(F.data == "recognition_list")
async def back_to_main(callback: types.CallbackQuery):
    await callback.message.edit_text("""☝️🤓 Я хорошо умею распознавать следующие предметы:\n
Банан 🍌       Сендвич 🥪      Пицца 🍕 
Пончик 🍩      Торт 🍰         Картон 📦
Вилка 🍴       Миска 🥣        Пластик 🛍️
Телевизор 📺   Клавиатура ⌨️   Микроволновка ♨️
Рюкзак 🎒      Галстук 👔      Чемодан 🧳
Стул 🪑        Диван 🛋️        Растение 🪴
Часы ⏰        Фен 💨          Яблоко 🍎
""", reply_markup=back())
    await callback.answer()