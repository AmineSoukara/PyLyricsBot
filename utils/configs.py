import os
import time


class Var(object):

    # Get a bot token from botfather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

    # Get from my.telegram.org
    API_ID = int(os.environ.get("API_ID", 12345))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "")

    # ID of users that can't use the bot commands
    BANNED_USERS = set(
        int(x) for x in os.environ.get(
            "BANNED_USERS", "").split())

    # To record start time of bot
    BOT_START_TIME = time.time()

    # Genius Api From Here : https://genius.com/api-clients
    API = os.environ.get("GENIUS_API", None)

    # buttons
    PAGENUM = int(os.environ.get("PAGENUM", 20))


class Tr(object):

    START_TEXT = """
👋 Hi ! {} Welcome To @PyLyricsBot !

PyLyrics Is An [Open-Source](https://github.com/AmineSoukara/PyLyricsBot/fork) Bot That Can Help You Get Song Lyrics
"""

    ABOUT_TEXT = """🤖 **My Name:** [Py Lyrics](t.me/PyLyricsBot)

📝 **Language:** [Python 3](https://www.python.org)

📚 **Framework:** [Pyrogram](https://github.com/pyrogram/pyrogram)

📡 **Hosted On:** [Heroku](heroku.com)

👨‍💻 **Developer:** [Amine Soukara](t.me/AmineSoukara)

💡 **Source Code:** [Github](https://github.com/AmineSoukara/PyLyricsBot/fork)

👥 **Support Group:** [Damien Help](https://t.me/DamienHelp)

📢 **Updates Channel:** [Damien Soukara](https://t.me/DamienSoukara)


❤ [Donate](https://www.paypal.me/AmineSoukara) (PayPal)
"""

    HELP_TEXT = """💡 Just Send Me The Name Of The Song.  That's it

❤ [Donate](https://www.paypal.me/AmineSoukara) (PayPal)
"""

    ERR_TEXT = "⚠️ Genius API Not Found"

    ERRTOKEN_TEXT = "😶 The Access Token Provided Is Expired, Revoked, Malformed Or Invalid For Other Reasons.",

    NORES = "💬 No Results"

    SEARCHING = "🔍 Searching For :"

    WAIT = "💬 Please Wait !!"

    ARTIST = "🗣 Artist :"

    SONG = "🎵 Song :"
