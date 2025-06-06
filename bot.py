from pyrogram import Client, __version__
from info import API_ID, API_HASH, BOT_TOKEN, temp


class Bot(Client):

    def __init__(self):
        super().__init__(
            name="FileToLinkBot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=30,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )

    async def start(self):
        await super().start()
        temp.BOT = self
        print(f"Bot started. Pyrogram v{__version__}")

    async def stop(self, *args):
        await super().stop()
        print("Bot stopped. Bye.")
    
app = Bot()
app.run()
