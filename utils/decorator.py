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

#CANCELLA COMANDI
def cancellacomandi(func):
    @wraps(func)
    def wrapped(bot, update):
        if update.message.text is not None:
          if update.message.text.startswith("/"):
            bot.delete_message(update.message.chat_id, update.message.message_id)
        return func(bot, update)
    return wrapped
#OWNERBOT
OWNER_LIST= [123456789]

def ownerbot(func):
    @wraps(func)
    def wrapped(bot, update):
        user_id = update.effective_user.id
        if user_id not in OWNER_LIST:
            print("Unauthorized access denied for {}.".format(user_id))
            return
        return func(bot, update)
    return wrapped
#COMANDI PRIVATI
def private(fn):
  def wrapper(*args,**kwargs):
    
    message = args[1].message
    if message.chat.type == 'private':
      return fn(*args,**kwargs)
    else:
      return False
  return wrapper
