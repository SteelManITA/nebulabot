from telegram import InlineKeyboardButton, InlineKeyboardMarkup
#BENVENUTO DI NEBULA
def init(bot, update):
	for new in update.message.new_chat_members:
		keyboard = [[InlineKeyboardButton("HTML/CSS/FRONTEND", url='http://t.me/html_css_ita'),
             InlineKeyboardButton("PHP_ITA",   url='http://t.me/php_italia'),
			 InlineKeyboardButton("PROGRAMMAZIONE",   url='http://t.me/programmazione_ita'), 
             InlineKeyboardButton("OFF TOPIC", url='http://t.me/offtopic_ita')]]

		reply_markup = InlineKeyboardMarkup(keyboard)
		update.message.reply_text('Benvenuto {username} in {chat_title}!\nRicordati di leggere il regolamento /regole\nBuona permanenza!\nPer richiedere supporto digita: @admin tuomessaggio'
			.format(username=update.message.from_user.first_name, chat_title = update.message.chat.title), reply_markup=reply_markup)