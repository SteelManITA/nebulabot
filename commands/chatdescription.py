from utils import decorator

@decorator.restricted
@decorator.cancellacomandi
def init(bot, update):
    if update.message.text is not None:
        if update.message.text.startswith("/description"):
            var_messaggio = update.message.text
            var_messaggio = var_messaggio.replace("/description", "")
            bot.setChatDescription(update.message.chat_id, description="{}".format(var_messaggio), parse_mode='HTML')