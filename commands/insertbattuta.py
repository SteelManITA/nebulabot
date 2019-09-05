import config
import MySQLdb
from utils import decorator
 
@decorator.restricted
@decorator.cancellacomandi
def init(update, context):
    if update.message.text is not None:
        if str(update.message.text).lower().startswith("/setbattuta"):
            var_messaggio = update.message.text
            var_messaggio = update.message.text[11:]
            db=MySQLdb.connect(config.database['server'],config.database['user'],config.database['password'],config.database['name'])
   
            db.autocommit(True)
            cur=db.cursor()
            
 
   
            cur.execute('INSERT INTO battute (battuta_text) VALUES ("'+var_messaggio+'")')
            
        
   
            cur.close()
            db.close()