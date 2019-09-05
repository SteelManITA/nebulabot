from utils import decorator
import config
@decorator.restricted
@decorator.cancellacomandi
def init(update, context):
    bot = context.bot
    bot.send_message(chat_id=config.admingroup_id,
                     text="<b>INFORMAZIONI UTENTE</b>\n\nUSERNAME: {username}\nID: <code>{id}</code>\nGRUPPO: {chat_title}"
                     .format(username="@" + update.message.reply_to_message.from_user.username,
                             id=update.message.reply_to_message.from_user.id, chat_title=update.message.chat.title)
                     , parse_mode='HTML')
