from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram import executor

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def extract_ref_id(text):
    return text.split()[1] if len(text.split()) > 1 else None

async def user_registration(message: Message):
    #Получение реферального идентификатора
    ref_id = await extract_ref_id(message.text)
    if ref_id:
        """
        Если в /start присутствовала реферальная ссылка
        Пример: 'https://t.me/bot_link?start=555'

        """
        await message.answer(text=f"Успешно!\nРеферальный идентификатор: '{ref_id}'")
    else:
        #Если в /start не было реферальной ссылки
        await message.answer(text=f"Реферальный идентификатор отсутствует.")
    

def register_handlers(dp):
    dp.register_message_handler(user_registration, commands=['start'], state="*")


if __name__ == '__main__':
    register_handlers(dp)
    executor.start_polling(dp, skip_updates=True)