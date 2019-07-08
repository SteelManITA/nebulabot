import wikipedia
#ZAMPA DEFINISCI RISCRITTO
def init(bot, update):
	if update.message.text is not None:
		if str(update.message.text).lower().startswith("nebula definisci"):
			var_messaggio = update.message.text
			var_messaggio = update.message.text[17:]
			print("{} searced a definition from Wikipedia".format(update.message.from_user.username))
			wikipedia.set_lang("it")
			try:
				definition = wikipedia.summary(var_messaggio, sentences=3)
				bot.send_message(update.message.chat_id, text=definition)
			except:
				bot.send_message(update.message.chat_id, text="Mi spiace {}, non ho trovato nulla riguardo '{}'".format(update.message.from_user.username, var_messaggio))