from telegram import ParseMode
import os
import random
import config

def start_handler(update, context):
    greetings = ['Hey', 'Hola', 'Hey there', 'Heyaa', 'Hi', 'Hello']
    chat_id = update.effective_chat.id
    greeting = greetings[random.randint(0, len(greetings) - 1)]
    app_url = config.get()[1]

    with open(os.path.join(config.root, 'messages', 'start.txt'), 'r') as reader:
        start_message = greeting + reader.read().format(app_url, app_url, app_url + 'signup')

    context.bot.send_message(chat_id=chat_id, text=start_message, parse_mode=ParseMode.HTML)