from aiogram import F, Router  # Импортируем необходимые классы и модули из aiogram
from aiogram.types import Message, CallbackQuery  # Импортируем классы Message и CallbackQuery
from aiogram.filters import CommandStart, Command  # Импортируем фильтры команд
from aiogram.fsm.state import State, StatesGroup  # Импортируем классы для работы с состояниями
from aiogram.fsm.context import FSMContext  # Импортируем контекст состояния

import keyboards as kb  # Импортируем модуль keyboards под псевдонимом kb

router = Router()  # Создаем объект маршрутизатора


class Register(StatesGroup):
    # Определяем группу состояний для регистрации
    name = State()  # Состояние для ввода имени
    age = State()  # Состояние для ввода возраста
    number = State()  # Состояние для ввода номера телефона


@router.message(CommandStart())
async def cmd_start(message: Message):
    # Обработчик команды /start
    await message.answer('Привет!', reply_markup=kb.main)  # Отправляем приветственное сообщение с клавиатурой main
    await message.reply('Как дела?')  # Отправляем сообщение "Как дела?"


@router.message(Command('help'))
async def cmd_help(message: Message):
    # Обработчик команды /help
    await message.answer('Вы нажали на кнопку помощи')  # Отправляем сообщение с текстом помощи


@router.message(F.text == 'Каталог')
async def catalog(message: Message):
    # Обработчик текстового сообщения с текстом "Каталог"
    await message.answer('Выберите категорию товара', reply_markup=kb.catalog)  # Отправляем сообщение с клавиатурой catalog


@router.callback_query(F.data == 'T-shirt')
async def t_shirt(callback: CallbackQuery):
    # Обработчик нажатия на кнопку с callback_data 't-shirt'
    await callback.answer('Вы выбрали категорию', show_alert=True)  # Отправляем ответ на callback с алертом
    await callback.message.answer('Вы выбрали категорию футболок.')  # Отправляем сообщение о выборе категории


@router.message(Command('register'))
async def register(message: Message, state: FSMContext):
    # Обработчик команды /register
    await state.set_state(Register.name)  # Устанавливаем состояние на 'name'
    await message.answer('Введите ваше имя')  # Просим пользователя ввести имя


@router.message(Register.name)
async def register_name(message: Message, state: FSMContext):
    # Обработчик состояния Register.name
    await state.update_data(name=message.text)  # Сохраняем введенное имя в состояние
    await state.set_state(Register.age)  # Устанавливаем состояние на 'age'
    await message.answer('Введите ваш возраст')  # Просим пользователя ввести возраст


@router.message(Register.age)
async def register_age(message: Message, state: FSMContext):
    # Обработчик состояния Register.age
    await state.update_data(age=message.text)  # Сохраняем введенный возраст в состояние
    await state.set_state(Register.number)  # Устанавливаем состояние на 'number'
    await message.answer('Отправьте ваш номер телефона', reply_markup=kb.get_number)  # Просим пользователя отправить номер телефона и показываем соответствующую клавиатуру


@router.message(Register.number, F.contact)
async def register_number(message: Message, state: FSMContext):
    # Обработчик состояния Register.number при получении контакта
    await state.update_data(number=message.contact.phone_number)  # Сохраняем номер телефона в состояние
    data = await state.get_data()  # Получаем все сохраненные данные
    await message.answer(f'Ваше имя: {data["name"]}\nВаш возраст: {data["age"]}\nНомер: {data["number"]}')  # Отправляем сообщение с введенными данными
    await state.clear()  # Очищаем состояние
