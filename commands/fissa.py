import config
import MySQLdb
from utils import decorator
from utils import controller
import config

@decorator.restricted
@controller.can_pin
@decorator.cancellacomandi
def init(update, context):
	bot = context.bot
	if update.message.text is not None:
		if update.message.text.lower().startswith("/fissa"):
			var_messaggio = update.message.text[6:]
			message_text="<b>Annuncio</b>\n\n{}" . format(var_messaggio)
			
			db=MySQLdb.connect(config.database['server'],config.database['user'],config.database['password'],config.database['name'])
			db.autocommit(True)
			cur=db.cursor()
   
			cur.execute("SELECT content FROM fissati_default ORDER BY created_at DESC LIMIT 1")

			row=cur.fetchone()
			if row is not None:
				message_text = message_text . "\n\n" . format(row[0])
				
			bot.send_message(update.message.chat_id, text=message_text, parse_mode='HTML')
			bot.pin_chat_message(update.message.chat_id, update.message.message_id+1)

			cur.close()
			db.close()