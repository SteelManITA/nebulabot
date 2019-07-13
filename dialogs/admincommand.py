import config
def init(bot, update):
	if update.message.text is not None:
		if update.message.text.startswith("@admin"):

			var_messaggio = update.message.text
			var_messaggio = update.message.text[7:]
			bot.send_message(-1001267698171, 
                 text="<b>NUOVA RICHIESTA DI SUPPORTO</b>\nChat: {idchat}\nAutore: {username}\nLink: {linkurl}{idchat}/{link}\n<code>Messaggio:{}</code>"
					 .format(var_messaggio, username="@"+update.message.from_user.username, link=update.message.message_id, 
					 idchat=update.message.chat.title, linkurl="https://t.me/"),
                 parse_mode='HTML')
			bot.send_message(config.channel_id, 
                 text="<b>NUOVA RICHIESTA DI SUPPORTO</b>\nChat: {idchat}\nAutore: {username}\nLink: {linkurl}{idchat}/{link}\n<code>Messaggio:{}</code>"
					 .format(var_messaggio, username="@"+update.message.from_user.username, link=update.message.message_id, 
					 idchat=update.message.chat.title, linkurl="https://t.me/"),
                 parse_mode='HTML')
