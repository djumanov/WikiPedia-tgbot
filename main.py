from telegram.bot import Bot

TOKEN = "5598770871:AAFm0H64aLx5kI0n1CNFNwNJTT5kXmLa7bw"

bot = Bot(token=TOKEN)

print(bot.get_me())