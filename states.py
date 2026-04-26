from aiogram.fsm.state import State, StatesGroup

class EcoStates(StatesGroup):
    waiting_for_item = State()
    waiting_for_address = State()
    waiting_for_photo = State()
    waiting_for_complaint = State()
    waiting_for_photo_detection = State()