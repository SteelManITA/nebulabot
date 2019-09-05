#!/usr/bin/env python
# -*- coding: utf-8 -*-
import config
import telegram
import MySQLdb
from random import random
from time import sleep 

def init(update, context):
	bot = context.bot
	if update.message is not None and update.message.text is not None:
		if str(update.message.text).lower().startswith("nebula"):
			var_risposta = str(update.message.text).lower()
			
			bot.sendChatAction(chat_id=update.message.chat_id , 
			action = telegram.ChatAction.TYPING)
			
			sleep(random() * 1 + 1.)
			
			db=MySQLdb.connect(
                config.database['server'],
                config.database['user'],
                config.database['password'],
                config.database['name']
            )
			db.autocommit(True)
			db.set_character_set('utf8mb4')
			cur=db.cursor()
  		
			query = 'SELECT risposta_text FROM risposte WHERE domanda_text = %s'
			cur.execute(query, [var_risposta])
			row = cur.fetchone()
			
			while row is not None:
				update.message.reply_text(text=row[0], parse_mode='HTML')
				row = cur.fetchone()
				cur.close()
				db.close()
