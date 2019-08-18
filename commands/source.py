from utils import decorator
@decorator.cancellacomandi
def init(bot, update):
    bot.send_message(update.message.chat_id, text="<b>     NebulaBot</b>\n"
                                          "====================\n\n"
                                          "<b>Linguaggio:</b> <em>Python</em>\n\n"
                                          "<b>Versione</b>:<em> v.6.0 - Falco</em>\n\n"
                                          "<b>Developer</b>:<em>Hersel Giannella</em>\n\n"
                                            "<b>Sorgente</b>:<a href=\"https://github.com/hersel91/nebulabot\"> GitHub</a>\n\n"
                                          "<b>Sito Web</b>:  <a href=\"https://hersel.it\">hersel.it</a> ", parse_mode = 'HTML')