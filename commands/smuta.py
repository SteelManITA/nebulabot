import config
from utils import decorator
#FUNZIONE SMUTA
@decorator.restricted
@decorator.cancellacomandi
def init(update, context):
    bot = context.bot
    bot.restrict_chat_member(update.message.chat_id,update.message.reply_to_message.from_user.id,
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_other_messages=True,
    can_add_web_page_previews=True
    )
    bot.send_message(config.channel_id,
		text="UTENTE SMUTATO\nUSERNAME: {username}\nID: {id}\nGRUPPO: {chat_title}"
			.format(username="@"+update.message.reply_to_message.from_user.username,id=update.message.reply_to_message.from_user.id,chat_title=update.message.chat.title)
			, parse_mode='HTML')  