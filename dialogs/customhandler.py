#!/usr/bin/env python
# -*- coding: utf-8 -*-
import config
import MySQLdb
 
def init(bot, update):
	if update.message.text is not None:
		
			db=MySQLdb.connect(config.database['server'],config.database['user'],config.database['password'],config.database['name'])
   
			db.autocommit(True)
			cur=db.cursor()
 
   
			cur.execute("SELECT risposta_text FROM risposte WHERE domanda_text = '{domanda}'".format(domanda = update.message.text))
			row=cur.fetchone()
			while row is not None:
				bot.send_message(update.message.chat_id, text=row[0],parse_mode='HTML')
				row = cur.fetchone()
   
				cur.close()
				db.close()