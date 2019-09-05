import config
import MySQLdb
import unicodedata
from utils import decorator

@decorator.restricted
@decorator.cancellacomandi
def init(update, context):
    if update.message.reply_to_message is not None:
        if str(update.message.text).lower().startswith("/setrisposta"):
            var_domanda = str(update.message.reply_to_message.text).lower()
            var_risposta = str(update.message.text[12:]).lower()
            
            db=MySQLdb.connect(
                config.database['server'],
                config.database['user'],
                config.database['password'],
                config.database['name']
            )
   
            db.autocommit(True)
            db.set_character_set('utf8mb4')
            cur=db.cursor()

            query = 'INSERT INTO risposte (domanda_text, risposta_text) VALUES (%s, %s)'
            cur.execute(query, (var_domanda, var_risposta))

            cur.close()
            db.close()