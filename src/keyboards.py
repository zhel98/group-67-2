from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

keyboard_main= ReplyKeyboardMarkup(keyboard=(
    [KeyboardButton(text='Корзина')],
    [KeyboardButton(text='Профиль'), KeyboardButton(text="Каталог")] 
), resize_keyboard=True, input_field_placeholder="Выберите один пункт")

inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Наш сайт",url="https://farmamir.kg")],
        [InlineKeyboardButton(text="Начать викторину",callback_data="quiz_start")],
        ])