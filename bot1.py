import logging
import requests
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Встановити токен вашого бота
BOT_TOKEN = "7150704262:AAGU1B-5evIIilBPc9CHb8Iq6XXjbhHQlEY"

# Створення об'єкта бота та диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Функція для логування до Fluentd
def log_to_fluentd(tag, message):
    url = "http://localhost:8080"
    headers = {"Content-Type": "application/json"}
    data = {
        "@log_name": tag,
        "message": message
    }
    try:
        requests.post(url, headers=headers, json=data)
    except Exception as e:
        print(f"Error sending log to Fluentd: {e}")

# Команда /start
@dp.message(Command("start"))
async def start(event: types.Message):
    user = event.from_user
    msg = f"User {user.id} ({user.username}) started the bot"
    log_to_fluentd("telegram_bot", msg)
    await event.answer("Привіт! Я бот з логуванням.")

# Команда /ping
@dp.message(Command("ping"))
async def ping(event: types.Message):
    msg = f"Ping from user {event.from_user.id}"
    log_to_fluentd("telegram_bot", msg)
    await event.answer("pong!")

# Запуск бота
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
