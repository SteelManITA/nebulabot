import config
from utils import decorator
@decorator.restricted
@decorator.cancellacomandi
def init(bot, update):
	pass
	if update.message.text is not None:
		if update.message.text.startswith("/annuncio"):
			var_messaggio = update.message.text
			var_messaggio = var_messaggio.replace("/annuncio", "")
		for a in config.annuncio_group:
			bot.send_message(a, text="{}".format(var_messaggio), parse_mode='HTML')