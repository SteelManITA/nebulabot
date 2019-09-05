from utils import decorator
import config
@decorator.restricted
@decorator.cancellacomandi
def init(update, context):
	bot = update.context
	if update.message.text is not None:
		if update.message.text.lower().startswith("/comunicazione"):
			var_messaggio = update.message.text[14:]
			bot.send_message(config.admingroup_id, text="<b>Comunicazione</b>\n\n{}\n@Hersy @TheLonelyAdventurer @jfet97 @thecmo @SteelManITA @iAmGio @Folgore796"
                .format(var_messaggio), parse_mode='HTML')
			bot.pin_chat_message(update.message.chat_id, update.message.message_id+1)