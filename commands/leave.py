from utils import decorator

@decorator.ownerbot
def init(update, context):
    bot = context.bot
    bot.leaveChat(update.message.chat_id)