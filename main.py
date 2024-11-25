import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import PollAnswer

# Initialize bot and dispatcher
API_TOKEN = ""
bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())


# Command to send a quiz
@dp.message(Command("quiz"))
async def send_quiz(message: types.Message):
    await bot.send_poll(
        chat_id=message.chat.id,
        question="What is the capital of France?",
        options=["Berlin", "Madrid", "Paris", "Rome"],
        type="quiz",
        correct_option_id=2,  # Correct answer is "Paris"
        explanation="Paris is the capital of France.",
        is_anonymous=False
    )


# Handling quiz answers
@dp.poll_answer()
async def handle_quiz_answer(poll_answer: PollAnswer):
    user_id = poll_answer.user.id
    selected_option = poll_answer.option_ids[0]

    correct_option_id = 2  # Match this with the correct_option_id in the quiz poll
    if selected_option == correct_option_id:
        await bot.send_message(chat_id=user_id, text="🎉 Correct! Well done.")
    else:
        await bot.send_message(chat_id=user_id, text="❌ That's incorrect. Try again!")


# Run the bot
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
