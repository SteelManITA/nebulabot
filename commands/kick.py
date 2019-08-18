from utils import decorator
import config
@decorator.restricted
@decorator.cancellacomandi
def init(bot, update):
   
    bot.kick_chat_member(update.message.chat_id, update.message.reply_to_message.from_user.id)
    bot.unban_chat_member(update.message.chat_id, update.message.reply_to_message.from_user.id)
    bot.send_message(update.message.chat_id, text="Utente <code>{}</code> kickato con successo!"
    .format(update.message.reply_to_message.from_user.id), parse_mode='HTML')
    bot.send_message(chat_id=config.admingroup_id,
                     text="<b>UTENTE KICKATO</b>\n\nUSERNAME: {username}\nID: <code>{id}</code>\nGRUPPO: {chat_title}"
                     .format(username="@" + update.message.reply_to_message.from_user.username,
                             id=update.message.reply_to_message.from_user.id, 
                             chat_title=update.message.chat.title)
                     , parse_mode='HTML')