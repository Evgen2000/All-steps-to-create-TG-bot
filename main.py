import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart,Command


bot = Bot(token="6429052985:AAFyrq1rR1-ewwPb3X80uB7sFP082dsnOXw")
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет!')
    await message.reply('Как дела?')


@dp.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Вам нужна помощь? Напишите - да')


@dp.message(F.text == 'да')
async def nice(message: Message):
    await message.answer('Ща разберемся, я вас слушаю')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
