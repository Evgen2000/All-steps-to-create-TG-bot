import asyncio
from aiogram import Bot, Dispatcher, F

from handlers import router


async def main():
    bot = Bot(token="6429052985:AAFyrq1rR1-ewwPb3X80uB7sFP082dsnOXw")
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
