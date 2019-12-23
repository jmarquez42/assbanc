from telegram.ext import Updater, CommandHandler
import requests
import subprocess

def get_ip():
    return subprocess.check_output('hostname').decode('utf-8')

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def bop(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text="Hola Vanessa")
    #bot.send_photo(chat_id=chat_id, photo=url)


def ip(bot, update):
    txt_ip = get_ip()
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=txt_ip)


def main():
    updater = Updater('')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop', bop))
    dp.add_handler(CommandHandler('ip', ip))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()