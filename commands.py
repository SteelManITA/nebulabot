from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import random
import os
import config
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

def start(bot, update):
    update.message.reply_text('Ciao sono Nebula! bot di questo gruppo\nsono stata creata da @Hersy\nSorgente: https://github.com/hersel91/Zampa2')


def distro(bot, update):
    distro_dir = [
        'https://distrowatch.com/table.php?distribution=opensuse',
        'https://distrowatch.com/table.php?distribution=elementary',
        'https://distrowatch.com/table.php?distribution=manjaro',
        'https://distrowatch.com/table.php?distribution=debian',
        'https://distrowatch.com/table.php?distribution=ubuntu',
        'https://distrowatch.com/table.php?distribution=arch',
        'https://distrowatch.com/table.php?distribution=solus',
        'https://distrowatch.com/table.php?distribution=fedora',
        'https://distrowatch.com/table.php?distribution=deepin',
        'https://distrowatch.com/table.php?distribution=mint',
        'https://distrowatch.com/table.php?distribution=popos',
        'https://distrowatch.com/table.php?distribution=centos',
        'https://distrowatch.com/table.php?distribution=kdeneon',
        'https://distrowatch.com/table.php?distribution=zorin',
        'https://distrowatch.com/table.php?distribution=antix',
        'https://distrowatch.com/table.php?distribution=porteus',
        'https://distrowatch.com/table.php?distribution=lubuntu',
        'https://distrowatch.com/table.php?distribution=lite',
        'https://distrowatch.com/table.php?distribution=xubuntu',
        'https://distrowatch.com/table.php?distribution=kubuntu',
        'https://distrowatch.com/table.php?distribution=freebsd',
        'https://distrowatch.com/table.php?distribution=tails',       
            ]
    bot.send_message(update.message.chat_id, text=random.choice(distro_dir))  

def regole(bot, update):
    bot.send_message(update.message.chat_id, text='https://telegra.ph/REGOLAMENTO-DEL-GRUPPO-06-26', parse_mode='HTML')

def io(bot, update):
    bot.send_message(update.message.from_user.id, text="NOME UTENTE: {nomeutente}\nUSERNAME: {username}\nID: {id}"
        .format(nomeutente=update.message.from_user.first_name, username="@"+update.message.from_user.username, id=update.message.from_user.id), 
        parse_mode='HTML')
    

@restricted
def ban(bot, update):
    pass
    bot.send_video(update.message.chat_id, 
    video='http://4.bp.blogspot.com/-HUn5hfk8OzQ/UM_Pi-bGphI/AAAAAAAAEVY/JO-DljB1L2I/s1600/explosi%25C3%25B3n+gif.gif', 
    caption='<b>QUESTA NON E\' UN\'ESERCITAZIONE</b>\n\nRecarsi immediatamente al bunker antiatomico, ripeto <b>NON E\' UN\'ESERCITAZIONE</b>', parse_mode='HTML')

def aiuto(bot, update):
    var_lettura = open("/root/pythonserver/nebulabot/help.txt", "r").read()
    bot.send_message(update.message.chat_id, text=var_lettura, parse_mode='HTML')

def source(bot, update):
    bot.send_message(update.message.chat_id, text="<b>     NebulaBot</b>\n"
                                          "====================\n\n"
                                          "<b>Linguaggio:</b> <em>Python</em>\n\n"
                                          "<b>Versione</b>:<em> v.2.7 - Balena</em>\n\n"
                                          "<b>Developer</b>:<em>Hersel Giannella</em>\n\n"
                                            "<b>Sorgente</b>:<a href=\"https://github.com/hersel91/nebulabot\"> GitHub</a>\n\n"
                                          "<b>Sito Web</b>:  <a href=\"https://hersel.it\">hersel.it</a> ", parse_mode = 'HTML')
#FUNZIONE MUTA
@restricted
def muta(bot, update):
    pass
    bot.restrict_chat_member(update.message.chat_id,update.message.reply_to_message.from_user.id,
    can_send_messages=False,
    can_send_media_messages=False,
    can_send_other_messages=False,
    can_add_web_page_previews=False
    )
    bot.send_message(config.channel_id,
		text="UTENTE MUTATO\nUSERNAME: {username}\nID: {id}\nGRUPPO: {chat_title}"
			.format(username="@"+update.message.reply_to_message.from_user.username,id=update.message.reply_to_message.from_user.id,chat_title=update.message.chat.title)
			, parse_mode='HTML')
@restricted
def smuta(bot, update):
    pass
    bot.restrict_chat_member(update.message.chat_id,update.message.reply_to_message.from_user.id,
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_other_messages=True,
    can_add_web_page_previews=True
    )
    bot.send_message(config.channel_id,
		text="UTENTE SMUTATO\nUSERNAME: {username}\nID: {id}\nGRUPPO: {chat_title}"
			.format(username="@"+update.message.reply_to_message.from_user.username,id=update.message.reply_to_message.from_user.id,chat_title=update.message.chat.title)
			, parse_mode='HTML')  

