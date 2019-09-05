from utils import decorator
from utils import controller
import config

@decorator.restricted
@controller.can_pin
@decorator.cancellacomandi
def init(update, context):
	bot = context.bot
	if update.message.text is not None:
		if update.message.text.lower().startswith("/fissa"):
			var_messaggio = update.message.text[6:]
			bot.send_message(update.message.chat_id, text="<b>Annuncio</b>\n\n{}".format(var_messaggio), parse_mode='HTML')
			bot.pin_chat_message(update.message.chat_id, update.message.message_id+1)