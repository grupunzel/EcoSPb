import os
from dotenv import load_dotenv
from config.logger import logger

try:
    load_dotenv()
except Exception as e:
    logger.error(f'.env load failed {e}')

class Settings:
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    GIGA_CREDENTIALS = os.getenv("GIGA_CREDENTIALS")
    FFMPEG_PATH = os.getenv("FFMPEG_PATH", "/opt/homebrew/bin/ffmpeg")
    FFPROBE_PATH = os.getenv("FFPROBE_PATH", "/opt/homebrew/bin/ffprobe")

    def __init__(self):
        os.environ["PATH"] += os.pathsep + os.getenv("EXTRA_PATH", "/opt/homebrew/bin")

settings = Settings()