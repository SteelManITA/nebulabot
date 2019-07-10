from utils import decorator

@decorator.restricted
@decorator.cancellacomandi
def init(bot, update):
    if update.message.text is not None:
        if update.message.text.startswith("/title"):
            var_messaggio = update.message.text
            var_messaggio = var_messaggio.replace("/title", "")
            bot.setChatTitle(update.message.chat_id, title="{}".format(var_messaggio), parse_mode='HTML')