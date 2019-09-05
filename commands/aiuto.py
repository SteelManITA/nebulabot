from utils import decorator
@decorator.cancellacomandi
def init(update, context):
    bot = context.bot
    var_lettura = open("/home/admin/pythonserver/nebulabot/text/help.txt", "r").read()
    bot.send_message(update.message.chat_id, text=var_lettura, parse_mode='HTML')