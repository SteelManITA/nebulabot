from utils import decorator
 
@decorator.restricted
def init(bot, update):
    bot.pin_chat_message(update.message.chat_id, update.message.reply_to_message.message_id)
    bot.delete_message(update.message.chat_id, update.message.message_id)