from aiogram import Bot, Dispatcher
from config.settings import settings
from config.logger import logger
import main_handler.commands as commands
from utilization_handler import utilization_handler
from container_handler import container_map_handler
from complaint_handler import complaint_handler
from photo_detection_handler import photo_detection_handler
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio

async def main():
    bot = Bot(token=settings.TELEGRAM_TOKEN)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    dp.include_router(commands.router)
    dp.include_router(utilization_handler.router)
    dp.include_router(container_map_handler.router)
    dp.include_router(complaint_handler.router)
    dp.include_router(photo_detection_handler.router)
    try:
        logger.info('Bot started')
        await dp.start_polling(bot)
    except Exception as e:
        logger.critical(f'Bot crashed: {e}')
    finally:
        await bot.session.close()
    

if __name__ == '__main__':
    asyncio.run(main())