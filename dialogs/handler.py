import random
import config
import wikipedia
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from . import definisci
from . import welcome
from . import battuta
from . import admincommand

#RISPOSTE DI NEBULA

#pompino
def pompino(bot, update):
	if update.message.text is not None:
		if str(update.message.text).lower().startswith("nebula fammi un pompino"):
			bot.send_message(update.message.chat_id, text="{username} fattelo da solo! non sei di certo alla mia altezza quindi smamma❗️".format(username=update.message.from_user.first_name), parse_mode='HTML')
#bocchino
def bocchino(bot, update):
	if update.message.text is not None:
		if str(update.message.text).lower().startswith("nebula fammi un bocchino"):
			bot.send_message(update.message.chat_id, text="{username} fattelo da solo! non sei di certo alla mia altezza quindi smamma❗️".format(username=update.message.from_user.first_name), parse_mode='HTML')
#panino
def panino(bot, update):
	if update.message.text is not None:
		if str(update.message.text).lower().startswith("nebula fammi un panino"):
			bot.send_message(update.message.chat_id, text="{username} fattelo da solo❗️".format(username=update.message.from_user.first_name), parse_mode='HTML')
#PRESENTAZIONE NEBULA
def presentazione(bot, update):
	if update.message.text is not None:
		if str(update.message.text).lower().startswith("nebula chi sei?"):
			bot.send_message(update.message.chat_id, text='Sono Nebula la mascotte di questo gruppo e tanti altri!')

def presentazione2(bot, update):
	if update.message.text is not None:
		if str(update.message.text).lower().startswith("chi sei nebula?"):
			bot.send_message(update.message.chat_id, text='Sono Nebula la mascotte di questo gruppo e tanti altri!')
			

#kaffe
def kaffe(bot, update):
	if update.message.text is not None:
		if str(update.message.text).lower().startswith("buongiornissimo"):
			bot.send_message(update.message.chat_id, text="Kaffeeee?!", parse_mode='HTML')

#kali
def kali(bot, update):
	if update.message.text is not None:
		if str(update.message.text).lower().startswith("kali linux"):
			bot.send_message(update.message.chat_id, text="Complimenti {username} sei ufficialmente un'analfabeta funzionale!".format(username=update.message.from_user.first_name), parse_mode='HTML')

def dammizampa(bot, update):
	if update.message.text is not None:
		if str(update.message.text).lower().startswith("ciao nebula"):
			bot.send_message(update.message.chat_id, "CIAO {username}".format(username=update.message.from_user.first_name))
def buonasera(bot, update):
	if update.message.text is not None:
		if str(update.message.text).lower().startswith("buonasera"):
			bot.send_message(update.message.chat_id, "buonasera {username}".format(username=update.message.from_user.first_name))
#Buongiorno
def buongiorno(bot, update):
	if update.message.text is not None:
		if str(update.message.text).lower().startswith("buongiorno"):
			#bot.sendSticker(update.message.chat_id, 'https://furryden.it/immagini/stickerbot/zampagiorno.webp')
			bot.send_message(update.message.chat_id, "Buongiorno {username}".format(username=update.message.from_user.first_name))
#Buonanotte
def buonanotte(bot, update):
	if update.message.text is not None:
		if str(update.message.text).lower().startswith("buonanotte"):
			#bot.sendSticker(update.message.chat_id, 'https://furryden.it/immagini/stickerbot/zampanight.webp')
			bot.send_message(update.message.chat_id, "Buonanotte {username}".format(username=update.message.from_user.first_name))
#avada kedavra
def kedavra(bot, update):
	if update.message.text is not None:
		if str(update.message.text).lower().startswith("avada kedavra"):
			update.message.reply_text("{username} Avada Affanculo".format(username=update.message.from_user.first_name))
#send nudes
def sendnudes(bot, update):
	if update.message.text is not None:
		if str(update.message.text).lower().startswith("nebula send nudes"):
			bot.send_photo(update.message.chat_id, 'https://furryden.it/immagini/sendnudes2.png')
#come stai
def comestai(bot, update):
	if update.message.text is not None:
		if str(update.message.text).lower().startswith("come stai nebula?"):
			bot.send_message(update.message.chat_id, "Sto bene {username}".format(username=update.message.from_user.first_name))



		
#DICHIARAZIONE FUNZIONI
def init(bot, update):
	welcome.init(bot, update)
	buongiorno(bot, update)
	buonanotte(bot, update)
	dammizampa(bot, update)
	kedavra(bot, update)
	sendnudes(bot, update)
	comestai(bot, update)
	buonasera(bot, update)
	pompino(bot, update)
	bocchino(bot, update)
	panino(bot, update)
	kaffe(bot, update)
	presentazione(bot, update)
	presentazione2(bot, update)
	battuta.init(bot, update)
	kali(bot, update)
	definisci.init(bot, update)
	admincommand.init(bot, update)
	


