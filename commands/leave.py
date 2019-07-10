from utils import decorator

@decorator.ownerbot
def init(bot, update):
    bot.leaveChat(update.message.chat_id)