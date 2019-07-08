from utils import decorator
import random
@decorator.cancellacomandi
def init(bot, update):
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