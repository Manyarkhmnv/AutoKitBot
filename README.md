# 🤖 Telegram Бот — шаблоны no-code автоматизаций

Этот проект — Telegram-бот, созданный с помощью Python и Aiogram, который показывает пользователю набор готовых инструментов и шаблонов для автоматизации повседневных задач. Код лаконичен, асинхронен и использует современные best practices.


# 🧰 Используемые технологии

- Python 3.10+ — основной язык, используется асинхронный подход (asyncio) для неблокирующего исполнения кода.
- Aiogram — современный асинхронный фреймворк для Telegram-ботов. Используется для: обработки команд (/start) и callback-кнопок, маршрутизации событий через Dispatcher, работы с ботом через Bot.
- InlineKeyboardMarkup — создание кнопочного интерфейса в Telegram, где каждая кнопка привязана к шаблону.
- HTML ParseMode — позволяет форматировать сообщения (жирный текст, ссылки) с помощью HTML-тегов.
- python-dotenv — безопасная загрузка переменных окружения (например, токена бота) из .env файла, без хардкода в коде.
- asyncio.run() — запуск асинхронного event loop, который обеспечивает работу всех async def функций.
