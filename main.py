from telegram import User
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram.update import Update


TOKEN = "5598770871:AAFm0H64aLx5kI0n1CNFNwNJTT5kXmLa7bw"


updater: User = Updater(token=TOKEN)


def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hi")


dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))


updater.start_polling()
updater.idle()
