from utils import decorator
@decorator.cancellacomandi
def init(bot, update):
    var_lettura = open("/root/pythonserver/nebulabot/help.txt", "r").read()
    bot.send_message(update.message.chat_id, text=var_lettura, parse_mode='HTML')