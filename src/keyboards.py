from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

keyboard_main= ReplyKeyboardMarkup(keyboard=(
    [KeyboardButton(text='JS')],
    [KeyboardButton(text='Python'), KeyboardButton(text="c#")] 
), resize_keyboard=True, input_field_placeholder="Выберите один пункт")

inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Документация JS", url="https://developer.mozilla.org/")],
        [InlineKeyboardButton(text="Документация Python", url="https://www.python.org/")],
        [InlineKeyboardButton(text="Документация C#", url="https://learn.microsoft.com/ru-ru/dotnet/csharp/")],
        [InlineKeyboardButton(text="Начать обучение", callback_data="start_learning")],
        [InlineKeyboardButton(text="Начать викторину",callback_data="quiz_start")],
    ])