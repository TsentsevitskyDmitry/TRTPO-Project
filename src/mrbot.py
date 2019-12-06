import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters 
import telegram
from datetime import datetime
from dprocessor import DialogProcessor
from TextNotofocationProcessor import NotificationsORM
import threading
from log import Log

dprocessor = DialogProcessor();
notifications = NotificationsORM();
sender = None;

def start(token):
    # Enable logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(token, use_context=True)
    global sender
    sender = telegram.Bot(token=token)
    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start_callback))
    dp.add_handler(CommandHandler("help", help_callback))
    dp.add_handler(CommandHandler("show", show_callback))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text | Filters.video | Filters.photo | Filters.document, reply_text_callback))
    dp.add_handler(MessageHandler(Filters.photo | Filters.document, reply_document_callback))

    # log all errors
    dp.add_error_handler(error_callback)
    # Start the Bot
    updater.start_polling()

    Log("Bot Started!");
    set_checker()
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


def reply_text_callback(update, context):
    """Answer user message."""
    if update.message == None: 
        return
    reply = dprocessor.process_text(update.message.text, update.effective_chat.id);
    update.message.reply_text(reply)

def reply_document_callback(update, context):
    """Answer user message."""
    update.message.reply_text("Sorry, not implemented")

def show_callback(update, context):
    update.message.reply_text(notifications.show_all(update.effective_chat.id))

def start_callback(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!\nSend me a short messages with things you want to remember!\nUsge: Напомни *когда* *что*')

def help_callback(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Usge: Напомни *когда* *что*')

def error_callback(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def check():
    remindings = notifications.get_all(datetime.now())
    for remind in remindings:
        sender.send_message(chat_id=remind.chat_id, text="ВНИМАНИЕ!!! - " + remind.payload)
        Log("Send notification to %i"%(remind.chat_id));
        remind.delete_instance()

def set_checker():
  threading.Timer(10.0, set_checker).start()
  check()