import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

import repository
from reminder_bot import ReminderBot


async def main():
    bot: Bot = Bot(token=repository.get_bot_token(), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dispatcher: Dispatcher = Dispatcher()
    await ReminderBot(bot, dispatcher).start()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()
