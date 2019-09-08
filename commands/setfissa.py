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
		if update.message.text.lower().startswith("/setfissa"):
			var_messaggio = update.message.text[9:]
            db=MySQLdb.connect(config.database['server'],config.database['user'],config.database['password'],config.database['name'])
			db.autocommit(True)

            cur=db.cursor()
            cur.execute('INSERT INTO fissati_default (content) VALUES ("'+var_messaggio+'")')
            cur.close()

            db.close()

			bot.send_message(update.message.chat_id, text="<b>La fine del messaggio fissato è stata cambiata:</b>\n\n" . format(var_messaggio), parse_mode='HTML')