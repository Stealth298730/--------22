from aiogram.utils.keyboard import ReplyKeyboardBuilder


def build_global_menu_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Список тварин")
    builder.button(text="Додати нову тварину")
    builder.button(text="Показати список вилікуваних тварин")
    builder.adjust(1)
    return builder.as_markup()