from utils import decorator

@decorator.cancellacomandi
def init(update, context):
    bot = context.bot
    bot.send_message(update.message.chat_id, text='https://telegra.ph/REGOLAMENTO-DEL-GRUPPO-06-26', parse_mode='HTML')