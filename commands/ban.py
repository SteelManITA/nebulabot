from utils import decorator
@decorator.restricted
@decorator.cancellacomandi
def init(update, context):
    bot = context.bot
    bot.send_video(update.message.chat_id, 
    video='http://4.bp.blogspot.com/-HUn5hfk8OzQ/UM_Pi-bGphI/AAAAAAAAEVY/JO-DljB1L2I/s1600/explosi%25C3%25B3n+gif.gif', 
    caption='<b>QUESTA NON E\' UN\'ESERCITAZIONE</b>\n\nRecarsi immediatamente al bunker antiatomico, ripeto <b>NON E\' UN\'ESERCITAZIONE</b>', parse_mode='HTML')
    print("{} ha eseguito un ban".format(update.message.from_user.username))