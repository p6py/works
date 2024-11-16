from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
import asyncio

BOT1_TOKEN = "TOKEN" # откуда принимать сообщения
BOT2_TOKEN = "TOKEN" # куда пересылать сообщения

bot1 = Bot(token=BOT1_TOKEN)
bot2 = Bot(token=BOT2_TOKEN)

dp = Dispatcher()

@dp.message()
async def handle_message(message: Message):
    try:
        if message.text:
            await bot2.send_message(chat_id=message.chat.id, text=message.text)

        elif message.photo:
            photo = message.photo[-1]  # Берем фото в максимальном разрешении
            await bot2.send_photo(chat_id=message.chat.id, photo=photo.file_id, caption=message.caption)

        elif message.video:
            await bot2.send_video(chat_id=message.chat.id, video=message.video.file_id, caption=message.caption)

        elif message.document:
            await bot2.send_document(chat_id=message.chat.id, document=message.document.file_id, caption=message.caption)

        elif message.audio:
            await bot2.send_audio(chat_id=message.chat.id, audio=message.audio.file_id, caption=message.caption)

        elif message.voice:
            await bot2.send_voice(chat_id=message.chat.id, voice=message.voice.file_id, caption=message.caption)

        elif message.sticker:
            await bot2.send_sticker(chat_id=message.chat.id, sticker=message.sticker.file_id)

        else:
            await bot2.send_message(chat_id=message.chat.id, text="Сообщение не поддерживается для пересылки.")
    except Exception as e:
        print(f"Ошибка при пересылке сообщения: {e}")


async def main():

    await bot1.delete_webhook(drop_pending_updates=True)
    await bot2.delete_webhook(drop_pending_updates=True)

    await dp.start_polling(bot1)

if __name__ == "__main__":
    asyncio.run(main())
