import telepot

token = '5020600955:AAHQj5zfM6Vgrfbk1CiSed5TNcLoDfXYiFc'
chat_id = -743030458

bot = telepot.Bot(token)

def send_message(text):
    bot.sendMessage(chat_id, text, parse_mode='Markdown')
