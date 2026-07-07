from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


from src.questions import QUESTIONS
from src.keyboards import keyboard_main, inline, quiz_povtor

router = Router()

class Quiz(StatesGroup):
    waiting_answer = State()
    
    
@router.message(Command('game'))
async def cmd_game(message: Message):
    await message.answer("Выберите один пункт", reply_markup=inline)
  
    
# старт викторины
@router.callback_query(F.data == 'quiz_start')
async def quiz_start(callback: CallbackQuery, state: FSMContext):
        await callback.answer("Че там где там броузер?", show_alert=True)
        await state.update_data(index=0,score=0)
        await state.set_state(Quiz.waiting_answer)
        await callback.message.answer(f"Вопрос 1\n\n{QUESTIONS[0]['q']}"
)
        
@router.message(Quiz.waiting_answer)
async def quiz_answer(message: Message, state: FSMContext):
    data = await state.get_data()

    index = data["index"]
    score = data["score"]

    user_answer = message.text.strip().lower()
    correct_answer = QUESTIONS[index]["a"].strip().lower()

    if user_answer == correct_answer:
        score += 1
        await message.answer("Правильно!")
    else:
        await message.answer(
            f"Неправильно. Правильный ответ: {QUESTIONS[index]['a']}"
        )

    index += 1

    if index < len(QUESTIONS):
        await state.update_data(index=index, score=score)

        await message.answer(
            f"Вопрос {index + 1}\n\n{QUESTIONS[index]['q']}"
        )
    else:
        await message.answer(
            f"Викторина окончена!\n\n"
            f"Твой результат: {score} из {len(QUESTIONS)}",
            reply_markup=quiz_povtor
        )

        await state.clear()     
        

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer("Выберите:", reply_markup=inline)

@router.callback_query(F.data == "start_learning")
async def start_learning(callback: CallbackQuery):
    await callback.answer("Начинаем обучение!", show_alert=True)

@router.message(F.text == 'js')
async def js_info(message: Message):
    await message.answer("JS — язык программирования для веб-разработки.")

@router.message(F.text == 'python')
async def py_info(message: Message):
    await message.answer("Python — популярный язык общего назначения.")

@router.message(F.text == 'c#')
async def cs_info(message: Message):
    await message.answer("C# — объектно-ориентированный язык от Microsoft.")

@router.message(CommandStart())
async def cmd_start(message: Message):
        await message.answer(
                f'Привет {message.from_user.first_name}! Выбери язык программирования',
                reply_markup=keyboard_main
                )
        print(f'пользователь : {message.from_user.full_name} отправил {message.text} в {message.date}')
         

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


