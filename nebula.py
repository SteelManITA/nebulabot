#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from dialogs import admincommand
import config, commands, dialogs, utils

# Questo abilita i log
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
def error(update, context):
    logger.warning('Update "%s" genera errore: "%s"', update, context.error)

# Questa è la funzione che inizializza il bot
def main():
    updater = Updater(config.bot_token, use_context=True)
    dp = updater.dispatcher

    # Qui "creo" i comandi e assegno una funzione
    dp.add_handler(CommandHandler("start", commands.start.init))
    dp.add_handler(CommandHandler("regole", commands.regole.init))
    dp.add_handler(CommandHandler("ban", commands.ban.init))
    dp.add_handler(CommandHandler("aiuto", commands.aiuto.init))
    dp.add_handler(CommandHandler("source", commands.source.init))
    dp.add_handler(CommandHandler("io", commands.io.init))
    dp.add_handler(CommandHandler("distro", commands.distro.init))
    dp.add_handler(CommandHandler("muta", commands.muta.init))
    dp.add_handler(CommandHandler("smuta", commands.smuta.init))
    dp.add_handler(CommandHandler("fissa", commands.fissa.init))
    dp.add_handler(CommandHandler("setfissa", commands.setfissa.init))
    dp.add_handler(CommandHandler("say", commands.say.init))
    dp.add_handler(CommandHandler("annuncio", commands.annuncio.init))
    dp.add_handler(CommandHandler("richiedi", commands.richiedifunzione.init))
    dp.add_handler(CommandHandler("exit", commands.leave.init))
    dp.add_handler(CommandHandler("title", commands.chattitle.init))
    dp.add_handler(CommandHandler("description", commands.chatdescription.init))
    dp.add_handler(CommandHandler("setbattuta", commands.insertbattuta.init))
    dp.add_handler(CommandHandler("setrisposta", commands.insertcustomhandler.init))
    dp.add_handler(CommandHandler("server", commands.server.init))
    dp.add_handler(CommandHandler("comunicazione", commands.comunicazione.init))
    dp.add_handler(CommandHandler("kicka", commands.kick.init))
    dp.add_handler(CommandHandler("info", commands.get.init))
    dp.add_handler(CommandHandler("community", commands.community.init))
    dp.add_handler(CallbackQueryHandler(admincommand.risolto))

    
    # Qui richiamo le funzioni senza comando, =>handler
    dp.add_handler(MessageHandler(None, dialogs.handler.init))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
