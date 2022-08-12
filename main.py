from telegram import User, ForceReply
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram.update import Update


TOKEN = "5598770871:AAFm0H64aLx5kI0n1CNFNwNJTT5kXmLa7bw"


updater: User = Updater(token=TOKEN)


def start(update: Update, context: CallbackContext):
    update.message.reply_text(f"Assalomu alaykum, {update.message.from_user.first_name}!\n\nWiki Pedia Botga Hush kelibsiz!!!\nWiki Pediadan qidirish uchun:\n\t'/search something'\nbuyrug'idan foydalaning...")


def search(update: Update, context: CallbackContext):
    print(update.message.text)



dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('search', search))


updater.start_polling()
updater.idle()
