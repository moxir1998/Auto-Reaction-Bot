from os import environ as env

class Telegram:
    API_ID = int(env.get("28136820", ""))
    API_HASH = env.get("20eb6e8833f0d5c89e2e7a784b2693bc", "")
    BOT_TOKEN = env.get("7712627407:AAEM9glTY6AwP1gzNT2y_m_BIPEro5WfI8M", "")
    BOT_USERNAME = env.get("Oasis_Like_1_bot", "")
    EMOJIS = [
        "👍", "👎", "❤", "🔥", 
        "🥰", "👏", "😁", "🤔",
        "🤯", "😱", "🤬", "😢",
        "🥶", "🤩", "🤮", "💩",
        "🙏", "👌", "🤣", "🤡",
        "🥱", "🥴", "😍", "🤓",
        "❤‍🔥", "🌚", "😐", "💯",
        "🤣", "⚡", "🍌", "🏆",
        "💔", "🤨", "😐", "😡",
        "👅", "🆒", "🖕", "😈",
        "😴", "😭", "👻", "⚡",
        "👨‍💻", "👀", "🎃", "🙄",
        "😇", "😨", "🤝", "🤐",
        "🤗", "🫡", "🎅", "🥸",
        "🤫", "😶‍🌫", "🤪", "😏",
        "😘", "👾", "🤷‍♂", "😎"
    ]

LOGGER_CONFIG_JSON = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'event-log.txt',
            'formatter': 'default'
        },
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'bot': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'pyrogram': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        }
    }
}
