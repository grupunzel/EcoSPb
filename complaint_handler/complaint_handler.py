from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from states import EcoStates
from complaint_handler.complaint_keyboard import back_to_menu, skip_photo_keyboard, back
from datetime import datetime

router = Router()

@router.callback_query(F.data == "send_complaint")
async def back_to_main(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(EcoStates.waiting_for_address)
    await callback.message.edit_text("📝 Для отправки жалобы, пожалуйста, укажите адрес пункта сбора отходов:👇🏻", reply_markup=back_to_menu())
    await callback.answer()

@router.message(EcoStates.waiting_for_address, F.text)
async def complaint_handler(message: types.Message, state: FSMContext):
    container_address = message.text.strip()
    await state.update_data(complaint_address=container_address)
    await state.set_state(EcoStates.waiting_for_complaint)
    await message.answer("📢 Теперь отправьте мне Вашу жалобу и я передам её в администрацию района.", reply_markup=back())

@router.message(EcoStates.waiting_for_complaint, F.text)
async def photo_handler(message: types.Message, state: FSMContext):
    container_complaint = message.text.strip()
    await state.update_data(complaint_text=container_complaint)
    await state.set_state(EcoStates.waiting_for_photo)
    await message.answer("📸 Отправьте фото, подтверждающее Вашу жалобу.", reply_markup=skip_photo_keyboard())

@router.message(EcoStates.waiting_for_photo, F.photo)
async def write_down_complaint(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    address = user_data.get("complaint_address", "Адрес не указан")
    complaint = user_data.get("complaint_text", "Нет жалоб")
    user_id = message.from_user.id
    username = message.from_user.username or ""
    full_name = message.from_user.full_name or ""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    photo = message.photo[-1]
    file_id = photo.file_id

    with open("complaints.txt", "a", encoding="utf-8") as f:
        f.write(f"""Пользователь #{user_id}: {full_name} (@{username})
Время заявки: {timestamp}
Адрес пункта: {address}
Жалоба: {complaint}
Фото: {file_id}
\n{'*'*50}""")
    
    await message.answer("""🙌🏻 Спасибо! Ваша жалоба принята. 
                         
Благодарим Вас за заботу и вклад в экологию Санкт-Петербурга 🙏""", reply_markup=back_to_menu())
    await state.clear()

@router.callback_query(F.data == "skip_photo")
async def write_down_complaint_without_photo(callback: types.CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    address = user_data.get("complaint_address", "Адрес не указан")
    complaint = user_data.get("complaint_text", "Нет жалоб")
    user_id = callback.from_user.id
    username = callback.from_user.username or ""
    full_name = callback.from_user.full_name or ""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("complaints.txt", "a", encoding="utf-8") as f:
        f.write(f"""Пользователь #{user_id}: {full_name} (@{username})
Время заявки: {timestamp}
Адрес пункта: {address}
Жалоба: {complaint}
\n{'*'*50}""")
    
    await callback.message.answer("""🙌🏻 Спасибо! Ваша жалоба принята. 
                         
Благодарим Вас за заботу и вклад в экологию Санкт-Петербурга 🙏""", reply_markup=back_to_menu())
    await state.clear()

@router.callback_query(F.data == "show_complaint")
async def show_user_complaint(callback: types.CallbackQuery):
    text = "*" * 50 + '\n'
    user_id = callback.from_user.id
    try:
        with open("complaints.txt", "r", encoding="utf-8") as f:
            content = f.read()

            raw_complaints = content.split('*'*50)
            for raw in raw_complaints:
                raw = raw.strip()
                if not raw:
                    continue

                if f"Пользователь #{user_id}:" not in raw:
                    continue
                else:
                    lines = raw.split("\n")
                    for line in lines:
                        text += line + '\n'
                    text += "*" * 50

            await callback.message.edit_text(f"📝 Ваши жалобы:\n\n{text}", reply_markup=back_to_menu())
            await callback.answer()
    
    except Exception as e:
        await callback.message.edit_text("🙌🏻 У Вас пока нет жалоб.", reply_markup=back())
        await callback.answer()