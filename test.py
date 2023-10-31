import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from env import BOT_API_KEY, OPENAI_API_KEY

token = BOT_API_KEY
openai.api_key = OPENAI_API_KEY

bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler()
async def send(message : types.Message):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[],
    temperature=0.5,
    max_tokens=256
)

    await message.answer(response['choices'][0]['text'])

executor.start_polling(dp, skip_updates=True)