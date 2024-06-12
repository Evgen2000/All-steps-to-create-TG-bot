from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)  # Импортируем необходимые классы из aiogram.types

# Создаем объект ReplyKeyboardMarkup для основного меню
main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Каталог')],  # Кнопка "Каталог"
        [KeyboardButton(text='Корзина')],  # Кнопка "Корзина"
        [KeyboardButton(text='Контакты'), KeyboardButton(text='О нас')]  # Кнопка "О нас"
    ],
    resize_keyboard=True,  # Уменьшаем размер клавиатуры для более удобного отображения
    input_field_placeholder='Выберите пункт меню'  # Текст подсказки в поле ввода
)

# Создаем объект InlineKeyboardMarkup для меню каталога
catalog = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Футболки', callback_data='T-shirt')],  # Кнопка "Футболки" с callback_data 'T-shirt'
        [InlineKeyboardButton(text='Кроссовки', callback_data='Sneakers')],  # Кнопка "Кроссовки" с callback_data 'Sneakers'
        [InlineKeyboardButton(text='Штаны', callback_data='Trousers')],  # Кнопка "Штаны" с callback_data 'Trousers'
        [InlineKeyboardButton(text='Носки', callback_data='Socks')]  # Кнопка "Носки" с callback_data 'Socks'
    ]
)

# Создаем объект ReplyKeyboardMarkup для запроса номера телефона
get_number = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Отправить номер', request_contact=True)]  # Кнопка для отправки номера телефона
    ],
    resize_keyboard=True  # Уменьшаем размер клавиатуры для более удобного отображения
)
