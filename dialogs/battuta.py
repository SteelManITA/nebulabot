import config
import MySQLdb
 
def init(bot, update):
	if update.message.text is not None:
		if str(update.message.text).lower().startswith("nebula fai una battuta"):
			db=MySQLdb.connect(config.database['server'],config.database['user'],config.database['password'],config.database['name'])
   
			db.autocommit(True)
			cur=db.cursor()
 
   
			cur.execute("SELECT * FROM battute ORDER BY RAND() LIMIT 1")
			row=cur.fetchone()
			while row is not None:
				bot.send_message(update.message.chat_id, text=row[1])
				row = cur.fetchone()
   
				cur.close()
				db.close()

