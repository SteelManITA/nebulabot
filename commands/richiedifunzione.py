from utils import decorator
@decorator.cancellacomandi
def init(bot, update):
	if update.message.text is not None:
		if update.message.text.startswith("/richiedi"):
			var_messaggio = update.message.text
			var_messaggio = update.message.text[9:]
			bot.send_message(605363037, 
                 text="<b>NUOVA FUNZIONE RICHIESTA</b>\nAutore: {username}\n<code>Messaggio:{}</code>"
					 .format(var_messaggio, username="@"+update.message.from_user.username,),
                 parse_mode='HTML')