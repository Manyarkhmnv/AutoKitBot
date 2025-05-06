import asyncio
import os

from aiogram import Bot, Dispatcher, types, F
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from dotenv import load_dotenv

load_dotenv()


API_TOKEN = os.getenv("API_TOKEN")

templates = {
    "1. Скачиваем истории/тиктоки": ("Бот за пару секунд извлечёт фото, видео, сторис и тексты.", "https://t.me/SaveAsBot"),
    "2. Почтовый ящик": ("Читает твою gmail почту в Telegram, отправляет важные письма.", "https://t.me/GmailBot"),
    "3. Мини-лендинг": ("Раздел с шаблонами лендингов на Notion, которые можно настроить под свои услуги или продукты. Просто меняешь текст и готово!", "https://sotion.so/notion-templates"),
    "4. Список дел": ("Бот присылает тебе утренний список задач каждый день.", "https://t.me/SkeddyBot"),
    "5. Напоминания": ("Бот напоминает о дедлайнах, платежах и встречах.", "https://t.me/SkeddyBot"),
    "6. CRM-таблица": ("Бесплатный шаблон CRM для Google Sheets, позволяющий визуализировать процесс продаж и анализировать стратегию.", "https://salesflare.com/templates/free-google-sheets-crm?"),
    "7. Меню-бот": ("Telegram-бот с кнопками: обо мне, услуги, заявка и т.д.", "https://n8n.io/workflows/3055-telegram-bot-with-menu-driven-commands/"),
}

def get_main_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=title, callback_data=title)]
        for title in templates.keys()
    ])
    return keyboard


async def start_handler(message: types.Message):
    await message.answer(
        "Привет! Вот лучшие шаблоны автоматизации, которые может внедрить в свою жизнь даже школьник. \n \nНикакого кода, готовые инструкции и быстрое начало работы. \n \nНажми на интересующий шаблон и получи ссылку.",


        reply_markup=get_main_keyboard()
    )

async def callback_handler(callback: types.CallbackQuery):
    title = callback.data
    if title in templates:
        desc, link = templates[title]
        text = f"<b>{title}</b>\n{desc}\n\n<a href='{link}'>Открыть</a>"
        await callback.message.answer(text, parse_mode=ParseMode.HTML)
    await callback.answer()

async def main():
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()

    dp.message.register(start_handler, CommandStart())
    dp.callback_query.register(callback_handler, F.data.in_(templates.keys()))

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
