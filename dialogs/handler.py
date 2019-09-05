import random
import config
import wikipedia
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from . import definisci
from . import battuta
from . import admincommand
from . import customhandler
from . import customhandler2
from utils import util

#RISPOSTE DI NEBULA

#pompino
def pompino(update, context):
	bot = context.bot
	if update.message.text is not None:
		if str(update.message.text).lower().startswith("nebula fammi un pompino"):
			bot.send_message(update.message.chat_id, text="{username} fattelo da solo! non sei di certo alla mia altezza quindi smamma❗️".format(username=update.message.from_user.first_name), parse_mode='HTML')
#bocchino
def bocchino(update, context):
	bot = context.bot
	if update.message.text is not None:
		if str(update.message.text).lower().startswith("nebula fammi un bocchino"):
			bot.send_message(update.message.chat_id, text="{username} fattelo da solo! non sei di certo alla mia altezza quindi smamma❗️".format(username=update.message.from_user.first_name), parse_mode='HTML')
#panino
def panino(update, context):
	bot = context.bot
	if update.message.text is not None:
		if str(update.message.text).lower().startswith("nebula fammi un panino"):
			bot.send_message(update.message.chat_id, text="{username} fattelo da solo❗️".format(username=update.message.from_user.first_name), parse_mode='HTML')
#panino
def panino2(update, context):
	bot = context.bot
	if update.message.text is not None:
		if str(update.message.text).lower().startswith("sudo nebula fammi un panino"):
			bot.send_message(update.message.chat_id, text="{username} te lo faccio subito mio signore!".format(username=update.message.from_user.first_name), parse_mode='HTML')
#PRESENTAZIONE NEBULA
def presentazione(update, context):
	bot = context.bot
	if update.message.text is not None:
		if str(update.message.text).lower().startswith("nebula chi sei?"):
			bot.send_message(update.message.chat_id, text='Sono Nebula la mascotte di questo gruppo e tanti altri!')

def presentazione2(update, context):
	bot = context.bot
	if update.message.text is not None:
		if str(update.message.text).lower().startswith("chi sei nebula?"):
			bot.send_message(update.message.chat_id, text='Sono Nebula la mascotte di questo gruppo e tanti altri!')
			

#kaffe
def kaffe(update, context):
	bot = context.bot
	if update.message.text is not None:
		if str(update.message.text).lower().startswith("buongiornissimo"):
			bot.send_message(update.message.chat_id, text="Kaffeeee?!", parse_mode='HTML')

#kali
def kali(update, context):
	bot = context.bot
	if update.message.text is not None:
		if str(update.message.text).lower().startswith("kali linux"):
			bot.send_message(update.message.chat_id, text="Complimenti {username} sei ufficialmente un'analfabeta funzionale!".format(username=update.message.from_user.first_name), parse_mode='HTML')

def ciao(update, context):
	bot = context.bot
	if update.message.text is not None:
		if str(update.message.text).lower().startswith("ciao nebula"):
			bot.send_message(update.message.chat_id, "Ciao {username}".format(username=update.message.from_user.first_name))

def buonasera(update, context):
	bot = context.bot
	if update.message.text is not None:
		if str(update.message.text).lower().startswith("buonasera"):
			bot.send_message(update.message.chat_id, "buonasera {username}".format(username=update.message.from_user.first_name))
#Buongiorno
def buongiorno(update, context):
	bot = context.bot
	if update.message.text is not None:
		if str(update.message.text).lower().startswith("buongiorno"):
			#bot.sendSticker(update.message.chat_id, 'https://furryden.it/immagini/stickerbot/zampagiorno.webp')
			bot.send_message(update.message.chat_id, "Buongiorno {username}".format(username=update.message.from_user.first_name))
#Buonanotte
def buonanotte(update, context):
	bot = context.bot
	if update.message.text is not None:
		if str(update.message.text).lower().startswith("buonanotte"):
			#bot.sendSticker(update.message.chat_id, 'https://furryden.it/immagini/stickerbot/zampanight.webp')
			bot.send_message(update.message.chat_id, "Buonanotte {username}".format(username=update.message.from_user.first_name))
#avada kedavra
def kedavra(update, context):
	if update.message.text is not None:
		if str(update.message.text).lower().startswith("avada kedavra"):
			update.message.reply_text("{username} Avada Affanculo".format(username=update.message.from_user.first_name))
#send nudes
def sendnudes(update, context):
	bot = context.bot
	if update.message.text is not None:
		if str(update.message.text).lower().startswith("nebula send nudes"):
			bot.send_photo(update.message.chat_id, 'https://furryden.it/immagini/sendnudes2.png')
#come stai
def comestai(update, context):
	bot = context.bot
	if update.message.text is not None:
		if str(update.message.text).lower().startswith("come stai nebula?"):
			bot.send_message(update.message.chat_id, "Sto bene {username}".format(username=update.message.from_user.first_name))



		
#DICHIARAZIONE FUNZIONI
def init(update, context):
	buongiorno(update, context)
	buonanotte(update, context)
	ciao(update, context)
	kedavra(update, context)
	sendnudes(update, context)
	comestai(update, context)
	buonasera(update, context)
	pompino(update, context)
	bocchino(update, context)
	panino(update, context)
	panino2(update, context)
	kaffe(update, context)
	presentazione(update, context)
	presentazione2(update, context)
	battuta.init(update, context)
	kali(update, context)
	util.debug(update)
	definisci.init(update, context)
	admincommand.init(update, context)
	customhandler.init(update, context)
	customhandler2.init(update, context)
	


