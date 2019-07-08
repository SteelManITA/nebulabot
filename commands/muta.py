import config
from utils import decorator

@decorator.restricted
@decorator.cancellacomandi
def init(bot, update):
    pass
    bot.restrict_chat_member(update.message.chat_id,update.message.reply_to_message.from_user.id,
    can_send_messages=False,
    can_send_media_messages=False,
    can_send_other_messages=False,
    can_add_web_page_previews=False
    )
    bot.send_message(config.channel_id,
		text="UTENTE MUTATO\nUSERNAME: {username}\nID: {id}\nGRUPPO: {chat_title}"
			.format(username="@"+update.message.reply_to_message.from_user.username,id=update.message.reply_to_message.from_user.id,chat_title=update.message.chat.title)
			, parse_mode='HTML')