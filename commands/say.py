from utils import decorator
@decorator.restricted
@decorator.cancellacomandi
def init(update, context):
	bot = context.bot
	if update.message.text is not None:
		if str(update.message.text).lower().startswith("/say"):
			var_messaggio = update.message.text
			var_messaggio = update.message.text[4:]
			bot.send_message(update.message.chat_id, text='{}'.format(var_messaggio), parse_mode='HTML')