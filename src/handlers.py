from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

from src.keyboards import keyboard_main, inline

router = Router()

@router.callback_query(F.data == 'quiz start')
async def quiz_strart(callback: CallbackQuery):
        await callback.answer("Че там где там броузер?", show_alert=True)
        await callback.message.answer("Начинаем еблю!")


@router.message(CommandStart())
async def cmd_start(message: Message):
        await message.answer(
                f'Привет {message.from_user.first_name}! Я твой ботяра',
                reply_markup=keyboard_main
                )
        print(f'пользователь : {message.from_user.full_name} отправил {message.text} в {message.date}')


@router.message(Command('help'))
async def cmd_help(message: Message):
         await message.answer(
                 '/start - привет\n'
                 '/help - список команд\n'
                 '/about - описание бота\n'
                 'пока - прощание\n'
                 'echo - сообщение юзера дублируется',
                 reply_markup=inline
         )
         

@router.message(Command('about'))
async def cmd_about(message: Message):
        await message.answer(
                f'Привет {message.from_user.first_name}! Я исполняю все что ты пишешь на бэкэнде'
        )


@router.message(F.text.lower() == 'пока')
async def bye(message: Message):
        await message.answer(
                f'{message.from_user.first_name} Пока браузи'
        )


@router.message(F.text == 'Корзина')
async def get_group(message: Message):
        await message.answer(
                f'{message.from_user.first_name} Привет вот твоя корзина'
        )
 
        
@router.message()
async def echo(message: Message):
        await message.answer(
                f'Ты написал: {message.text}'
        )


