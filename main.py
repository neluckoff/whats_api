from whatsapp.user import User
from whatsapp.client import Bot
import re
import phonenumbers
import pywhatkit

if __name__ == '__main__':
    bot = Bot()
    bot.message_send('+79266715863', 'test msg')
    # user = User(bot)
    # pywhatkit.sendwhatmsg_to_group_instantly()

    # bot.message_send()
