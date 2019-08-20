import config
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from utils import util
from utils import decorator

@decorator.cancellacomandi
def init(bot, update):
    button_list = [
    InlineKeyboardButton("HTML/CSS", url='https://t.me/html_css_ita'),
    InlineKeyboardButton("JAVASCRIPT", url='https://t.me/javascript_ita'),
    InlineKeyboardButton("PROGRAMMAZIONE", url='https://t.me/programmazione_ita'),
    InlineKeyboardButton("PHP", url='https://t.me/php_italia'),
    InlineKeyboardButton("JAVA", url='https://t.me/java_italia'),
    InlineKeyboardButton("OFFTOPIC", url='https://t.me/offtopic_ita')
    ]
    reply_markup = InlineKeyboardMarkup(util.build_menu(button_list, n_cols=2))
    bot.send_message(update.message.chat_id, text="Le Nostre Community Telegram", reply_markup=reply_markup)