from telegram.ext import Updater, CommandHandler

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

def main():
    mybot = Updater("743204620:AAG2A-xUyuORIpoK5sYldvw_DPL4NoJ_Vow", request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))

    dp.add_handler(CommandHandler("hello", nice))
    
    mybot.start_polling()
    mybot.idle()

def greet_user(bot, update):
    text = 'Привет!'
    print(text)
    update.message.reply_text(text)

def nice(bot, update):
    text = 'Кококо'
    print(text)
    update.message.reply_text(text)

main()
