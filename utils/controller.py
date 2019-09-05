from functools import wraps


#CONTROLLER MESSAGGI FISSATI
def can_pin(func):
    @wraps(func)
    def pin_rights(update, context):
        bot = context.bot
        if update.effective_chat.get_member(bot.id).can_pin_messages:
            return func(update, context)
        else:
            update.effective_message.reply_text(
                "Non posso pinnare i messaggi! " "Assicurati di avermi fatto admin."
            )

    return pin_rights