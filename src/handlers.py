from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


from src.questions import QUESTIONS
from src.keyboards import keyboard_main, inline

router = Router()

class Quiz(StatesGroup):
    waiting_answer = State()
    
    
@router.message(Command('game'))
async def cmd_game(message: Message):
    await message.answer("Выберите один пункт", reply_markup=inline)
    
@router.message(F.text == 'JS')
async def JS(message: Message):
        await message.answer(
                f'{message.from_user.first_name} JS - язык программирования для веб'
        )

@router.message(F.text == 'Python')
async def Python(message: Message):
        await message.answer(
                f'{message.from_user.first_name} Python - язык программирования'
        )
        
@router.message(F.text == 'с#')
async def с(message: Message):
        await message.answer(
                f'{message.from_user.first_name} с# - язык программирования'
        )
    
# старт викторины
@router.callback_query(F.data == 'quiz_start')
async def quiz_start(callback: CallbackQuery, state: FSMContext):
        await callback.answer("Че там где там броузер?", show_alert=True)
        await state.update_data(index=0,score=0)
        await state.set_state(Quiz.waiting_answer)
        await callback.message.answer(f"Вопрос 1\n\n{QUESTIONS[0]['q']}"
)


@router.message(CommandStart())
async def cmd_start(message: Message):
        await message.answer(
                f'Привет {message.from_user.first_name}! Выбери язык программирования',
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
 
        
# @router.message()
# async def echo(message: Message):
#         await message.answer(
#                 f'Ты написал: {message.text}'
#         )


