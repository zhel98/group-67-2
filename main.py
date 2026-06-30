import asyncio

from aiogram.types import Message
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command

BOT_TOKEN = "8939204700:AAHaksTu8Wm31BMz0RPvYM7qjkxz9jdRryo"

bot = Bot(token = BOT_TOKEN)
dp = Dispatcher() #обработчик входящих сообщений

@dp.message(CommandStart())
async def cmd_start(message: Message):
        await message.answer(
                f'Привет {message.from_user.first_name}! Я твой ботяра')
        print(f'пользователь : {message.from_user.full_name} отправил {message.text} в {message.date}')


@dp.message(Command('help'))
async def cmd_help(message: Message):
         await message.answer(
                 '/start - привет\n'
                 '/help - список команд'
                 
         )

async def main():
        await dp.start_polling(bot) #отправляет запросы на тг-сервер
        
if __name__ == "__main__":
        asyncio.run(main())