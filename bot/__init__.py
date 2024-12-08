from pyrogram import Client
from logging import getLogger
from logging.config import dictConfig
from .config import Telegram, LOGGER_CONFIG_JSON

dictConfig(LOGGER_CONFIG_JSON)

version = 0.3
logger = getLogger('bot')

TelegramBot = Client(
    name="bot",
    api_id=Telegram.28136820,
    api_hash=Telegram.20eb6e8833f0d5c89e2e7a784b2693bc,
    bot_token=Telegram.7712627407:AAEM9glTY6AwP1gzNT2y_m_BIPEro5WfI8M,
    plugins={'root': 'bot/plugins'}
)
