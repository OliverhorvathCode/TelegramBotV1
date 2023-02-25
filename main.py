from telegram.ext import *
import keys

print('Starting up bot....')

def start_command(update, context):
    update.message.reply_text('Hello There! I am Oliver\'s first bot!')

def help_command(update, context):
    update.message.reply_text('Type something and I will respond!')

def custom_command(update, context):
    update.message.reply_text('This is a custom command!')

def handle_response(text: str) -> str:
    if 'hello' in text:
      return 'Hey What\'s up?'

    if 'how are you' in text:
        return 'I am swell'


    return 'I don\'t know'


def handle_message(update, context):
    message_type = update.message.chat.type
    text = str(update.message.text).lower()
    response = ''
    print(f'User ({update.message.chat.id}) says: "{text} in: {message_type}"')
    if message_type == 'group':
        if '@Test_07bot' in text:
            new_text = text.replace('@Test_07bot', '').strip()
            response = handle_response(new_text)
    else:
        response = handle_response(text)

    update.message.reply_text(response)


def error(update, context):
    print(f'Update {update} caused error: {context.error}')

if __name__ == '__main__':
    updater = Updater(keys.token, use_context=True)
    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('custom', custom_command))

    # Messages
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    #Error Messages
    dp.add_error_handler(error)

    #Running the bot (Finally!)
    updater.start_polling(1.0)
    updater.idle()