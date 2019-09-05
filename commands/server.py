#!/usr/bin/python
import psutil
from utils import decorator

@decorator.ownerbot
@decorator.cancellacomandi
def init(update, context):
    bot = context.bot
    bot.send_message(update.message.chat_id,text="<b>SERVER STATUS</b>\n<b>CPU:</b> <code>{cpu}%</code>\n<b>RAM:</b> <code>{ram}%</code>\n=========\nantares.hersel.it"
        .format(cpu=psutil.cpu_percent(),ram=psutil.virtual_memory()[2]),
        parse_mode='HTML')