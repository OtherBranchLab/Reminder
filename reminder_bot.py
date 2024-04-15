from aiogram import Bot, Dispatcher


class ReminderBot:
    def __init__(self, bot: Bot, dispatcher: Dispatcher):
        self.bot: Bot = bot
        self.dispatcher: Dispatcher = dispatcher
        self.users: dict[int, dict[str, Catalog | int]] = {}

    async def start(self):
        self.register_command()
        self.register_message_handler()
        self.register_callback_query_handler()
        print("Bot started")
        await self.dispatcher.start_polling(self.bot)
        return None

    def register_command(self):
        pass

    def register_message_handler(self):
        pass

    def register_callback_query_handler(self):
        pass
