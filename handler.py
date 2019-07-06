import random
import config
import wikipedia
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

#DEFINIZIONE COMANDI ADMIN
from functools import wraps

LIST_OF_ADMINS = [123456789]

def restricted(func):
    @wraps(func)
    def wrapped(bot, update):
        user_id = update.effective_user.id
        if user_id not in LIST_OF_ADMINS:
            print("Unauthorized access denied for {}.".format(user_id))
            return
        return func(bot, update)
    return wrapped

# FUNZIONI
def cancellacomandi(bot, update):
	if update.message.text is not None:
		if update.message.text.startswith("/"):
			bot.deleteMessage(chat_id=update.message.chat.id, message_id=update.message.message_id)


def admin(bot, update):
	if update.message.text is not None:
		if update.message.text.startswith("@admin"):

			var_messaggio = update.message.text
			var_messaggio = update.message.text[7:]
			bot.send_message(-1001267698171, 
                 text="<b>NUOVA RICHIESTA DI SUPPORTO</b>\nChat: {idchat}\nAutore: {username}\nLink: {linkurl}{idchat}/{link}\n<code>Messaggio:{}</code>"
					 .format(var_messaggio, username="@"+update.message.from_user.username, link=update.message.message_id, 
					 idchat=update.message.chat.title, linkurl="https://t.me/"),
                 parse_mode='HTML')
			bot.send_message(config.channel_id, 
                 text="<b>NUOVA RICHIESTA DI SUPPORTO</b>\nChat: {idchat}\nAutore: {username}\nLink: {linkurl}{idchat}/{link}\n<code>Messaggio:{}</code>"
					 .format(var_messaggio, username="@"+update.message.from_user.username, link=update.message.message_id, 
					 idchat=update.message.chat.title, linkurl="https://t.me/"),
                 parse_mode='HTML')

@restricted
def annuncio(bot, update):
	pass
	if update.message.text is not None:
		if update.message.text.startswith("/annuncio"):
			var_messaggio = update.message.text
			var_messaggio = var_messaggio.replace("/annuncio", "")
		for a in config.annuncio_group:
			bot.send_message(a, text="{}".format(var_messaggio), parse_mode='HTML')

def richiedi(bot, update):
	if update.message.text is not None:
		if update.message.text.startswith("/richiedi"):
			var_messaggio = update.message.text
			var_messaggio = update.message.text[9:]
			bot.send_message(605363037, 
                 text="<b>NUOVA FUNZIONE RICHIESTA</b>\nAutore: {username}\n<code>Messaggio:{}</code>"
					 .format(var_messaggio, username="@"+update.message.from_user.username,),
                 parse_mode='HTML')
@restricted
def say(bot, update):
	pass
	if update.message.text is not None:
		if update.message.text.startswith("/say"):
			var_messaggio = update.message.text
			var_messaggio = var_messaggio.replace("/say", "")
			bot.send_message(update.message.chat_id, text='{}'.format(var_messaggio), parse_mode='HTML')
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
#ZAMPA IMITAZIONE
def imitazione(bot, update):
	if update.message.text is not None:
		if str(update.message.text).lower().startswith("nebula fai un'imitazione"):
			imita_dir = [
        		'https://furryden.it/datastore/audio/ululato.mp3',
        		'https://furryden.it/datastore/audio/miagolio.mp3',
        		'https://furryden.it/datastore/audio/elefante.mp3',
        		'https://furryden.it/datastore/audio/leone.mp3',
        		'https://furryden.it/datastore/audio/scimmia.mp3',
        		'https://furryden.it/datastore/audio/gufo.mp3',
        		'https://furryden.it/datastore/audio/gallo.mp3',
			]
			bot.send_audio(update.message.chat_id, audio=random.choice(imita_dir))

#ZAMPA BATTUTE
def battuta(bot, update):
	if update.message.text is not None:
		if str(update.message.text).lower().startswith("nebula fai una battuta"):
			battuta_dir = [
        		'Come si dice uno scontro tra due carrelli?..... scontrino!',
        		'Il commercialista è triste perchè è partita iva!',
        		'Cosa faceva uno sputo su una scala? Saliva',
        		'A quale velocità va il cammello dei re magi? A tutta mirra',
        		'Si chiamano forbici, non sono fatte per le biciclette',
        		'Ieri ho fatto un incubo. Io un inquadrato',
        		'Se vuoi entrare in una vagina o suoni il campanello oppure pussy',
				'Dire ciao, buongiorno, arrivederci fa bene è salutare',
				'Una bomba scoppia in un cimitero. Tutti morti',
				'Ragazzo scoppia di salute. 8 morti e 4 feriti',
				'Sapete dove è il camerun? Tra il salottum ed il bagnum',
				'Se la museruola si mette sul muso, dove si mette la cazzuola?',
			]
			bot.send_message(update.message.chat_id, text=random.choice(battuta_dir))


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
			bot.send_photo(update.message.chat_id, 'https://furryden.it/immagini/sendnudes.png')
#come stai
def comestai(bot, update):
	if update.message.text is not None:
		if str(update.message.text).lower().startswith("come stai nebula?"):
			bot.send_message(update.message.chat_id, "Sto bene {username}".format(username=update.message.from_user.first_name))
#NEBULA DEFINISCI RISCRITTO
def zampadefinisci(bot, update):
	if update.message.text is not None:
		if str(update.message.text).lower().startswith("nebula definisci"):
			var_messaggio = update.message.text
			var_messaggio = update.message.text[17:]
			print("{} searced a definition from Wikipedia".format(update.message.from_user.username))
			wikipedia.set_lang("it")
			try:
				definition = wikipedia.summary(var_messaggio, sentences=3)
				bot.send_message(update.message.chat_id, text=definition)
			except:
				bot.send_message(update.message.chat_id, text="Mi spiace {}, non ho trovato nulla riguardo '{}'".format(update.message.from_user.username, var_messaggio))
			

#BENVENUTO DI NEBULA
def welcome(bot, update):
	for new in update.message.new_chat_members:
		keyboard = [[InlineKeyboardButton("HTML/CSS/FRONTEND", url='http://t.me/html_css_ita'),
             InlineKeyboardButton("PHP_ITA",   url='http://t.me/php_italia'),
			 InlineKeyboardButton("PROGRAMMAZIONE",   url='http://t.me/programmazione_ita'), 
             InlineKeyboardButton("OFF TOPIC", url='http://t.me/offtopic_ita')]]

		reply_markup = InlineKeyboardMarkup(keyboard)
		update.message.reply_text('Benvenuto {username} in {chat_title}!\nRicordati di leggere il regolamento /regole\nBuona permanenza!\nPer richiedere supporto digita: @admin tuomessaggio'
			.format(username=update.message.from_user.first_name, chat_title = update.message.chat.title), reply_markup=reply_markup)

		
#DICHIARAZIONE FUNZIONI
def init(bot, update):
	admin(bot, update)
	welcome(bot, update)
	buongiorno(bot, update)
	buonanotte(bot, update)
	say(bot, update)
	#cancellacomandi(bot, update)
	dammizampa(bot, update)
	kedavra(bot, update)
	sendnudes(bot, update)
	richiedi(bot, update)
	comestai(bot, update)
	zampadefinisci(bot, update)
	buonasera(bot, update)
	annuncio(bot, update)
	pompino(bot, update)
	bocchino(bot, update)
	panino(bot, update)
	kaffe(bot, update)
	presentazione(bot, update)
	presentazione2(bot, update)
	imitazione(bot, update)
	battuta(bot, update)
	kali(bot, update)
	


