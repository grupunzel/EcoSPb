from aiogram import Router, types, F
from main_handler.main_keyboard import main_keyboard
from aiogram.fsm.context import FSMContext
from states import EcoStates
from ai_handler.utilization.utilization_agent import get_ai_answer
from utilization_handler.utilization_keyboard import util_keyboard, back_to_menu
import asyncio

router = Router()

SPINNER_FRAMES = ["🤔", "💭", "🔄", "⚙️", "✨"]

@router.callback_query(F.data == "utilization_question")
async def utilization(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(EcoStates.waiting_for_item)
    await callback.message.edit_text("""📝 Напишите название предмета (например: батарейка, лампочка, пластиковая бутылка) или задайте вопрос про утилизацию. 🧐" \
    
Я подскажу, как правильно переработать.♻️""", reply_markup=back_to_menu())
    await callback.answer()


@router.message(EcoStates.waiting_for_item, F.text)
async def handle_item(message: types.Message, state: FSMContext):
    processing_message = None
    try:
        user_text = message.text.strip()
        processing_message = await message.answer("🤔 Думаю над ответом...")
        
        animation_task = asyncio.create_task(
            run_animation(message.bot, message.chat.id, processing_message.message_id)
        )

        bot_answer = await get_ai_answer(user_text)

        animation_task.cancel()
        try:
            await message.bot.delete_message(chat_id=message.chat.id, message_id=processing_message.message_id)
        except Exception:
            pass

        await message.answer(bot_answer, parse_mode="Markdown", reply_markup=util_keyboard())
        await state.clear()

    except Exception as e:
        if processing_message:
            try:
                await message.bot.delete_message(chat_id=message.chat.id, message_id=processing_message.message_id)
            except Exception:
                pass
        
        await message.answer("❌ Что-то пошло не так. Попробуйте ещё раз позже.\n\n Вы можете выбрать другое действие в меню:", reply_markup=main_keyboard())
        await state.clear()

async def run_animation(bot, chat_id: int, message_id: int):
    frame_index = 0
    try:
        while True:
            frame = SPINNER_FRAMES[frame_index % len(SPINNER_FRAMES)]
            try:
                await bot.edit_message_text(
                    chat_id=chat_id,
                    message_id=message_id,
                    text=f"{frame} Думаю над ответом..."
                )
            except Exception:
                pass
            frame_index += 1
            await asyncio.sleep(0.4)
    except asyncio.CancelledError:
        pass