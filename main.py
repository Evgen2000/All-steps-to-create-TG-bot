import asyncio  # Модуль для работы с асинхронным программированием
from aiogram import Bot, Dispatcher, F  # Импорт классов Bot, Dispatcher и F из библиотеки aiogram
from handlers import router  # Импорт маршрутизатора из модуля handlers

async def main():
    # Создаем объект бота с указанием токена
    bot = Bot(token="6429052985:AAFyrq1rR1-ewwPb3X80uB7sFP082dsnOXw")
    
    # Создаем диспетчер для обработки событий
    dp = Dispatcher()
    
    # Включаем маршрутизатор, который содержит обработчики событий
    dp.include_router(router)
    
    # Запускаем процесс polling для получения обновлений от Telegram
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        # Запускаем основную асинхронную функцию
        asyncio.run(main())
    except KeyboardInterrupt:
        # Если выполнение прерывается (например, нажатием Ctrl+C), выводим сообщение
        print('Бот выключен')
