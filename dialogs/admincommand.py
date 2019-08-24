import config
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def init(bot, update):
	if update.message.text is not None:
		if update.message.text.startswith("@admin"):
			keyboard = [[InlineKeyboardButton("Risolto✅", callback_data='1')]]
			reply_markup = InlineKeyboardMarkup(keyboard)

			var_messaggio = update.message.text
			var_messaggio = update.message.text[7:]
			bot.send_message(config.admingroup_id, 
                 text="<b>NUOVA RICHIESTA DI SUPPORTO</b>\nChat: {idchat}\nAutore: {username}\nLink: {linkurl}{idchat}/{link}\n<code>Messaggio:{}</code>"
					 .format(var_messaggio, username="@"+update.message.from_user.username, 
					 link=update.message.message_id, 
					 idchat=update.message.chat.title, 
					 linkurl="https://t.me/"),
                 parse_mode='HTML', 
				 reply_markup=reply_markup)
			bot.send_message(config.channel_id, 
                 text="<b>NUOVA RICHIESTA DI SUPPORTO</b>\nChat: {idchat}\nAutore: {username}\nLink: {linkurl}{idchat}/{link}\n<code>Messaggio:{}</code>"
					 .format(var_messaggio, 
					 username="@"+update.message.from_user.username, 
					 link=update.message.message_id, 
					 idchat=update.message.chat.title, 
					 linkurl="https://t.me/"),
                 parse_mode='HTML')

def risolto(bot, update):
	query = update.callback_query
	var_messaggio = query.message.text
	var_messaggio = query.message.text[6:]
	query.edit_message_text(text="{}\n<b>Risolto da: @{username}</b>"
	.format(var_messaggio,
	username=str(update.effective_user.username)),
	parse_mode='HTML')

