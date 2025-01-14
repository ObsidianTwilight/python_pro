from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
TOKEN: Final = '7802931820:AAGhqYm-6AC1kzyIK37CbOZdXHNyBgtScIY'
BOT_USERNAME: Final = '@HelloSunshine56bot'

# Commands
print('running commands')
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! I am looking forward to have a conversation betweeen us!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Yay! Finally, I am here to help! But do not ask complex questions.')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command!')

# Responces

def handle_responces(text: str) -> str:
    if 'hello' or 'Hello' in text:
        return 'Hey there!' 

    elif 'how are you?' or 'How are you?' in text:
        return 'I am good!'

    elif 'can you talk?' in text:
        return 'No.'
    
    elif 'What a pathetic bot' in text:
        return 'Hey! Watch your mouth!'
    
    return 'Type something that I can understand...'

# If added to group
print('running untill message handler')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Running under message handler")
    message_type: str = update.message.chat.type # It inform us whether it is a group chat or private chat
    text: str = update.message.text # Process incoming message

    # Message incoming to bot
    # print statement for debugging             whether it is in private chat or group
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"') # {text} -> What kinda text they're sending

    # For bot must not reply unless it being tagged

    if message_type == 'group':
        if BOT_USERNAME in text: # If someone trying to talk to bot in group chat
            new_text: str = text.replace(BOT_USERNAME, '').strip() # we do not wnat to process bot's username as part of the message
            #                    Replace bot's username with an empty string
            responce: str = handle_responces(new_text)
        else:
            return # bot should not responce unless it explicitly calling its username
    else:
        responce: str = handle_responces(text)

    print('Bot:',responce)  # For debugging
    await update.message.reply_text(responce)

    # For logging errors
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')
    print("Runnung untill if __nmae__ == '__main__'")
    # By putting it altogether
    
if __name__ == '__main__':
    print('starting bot...') # Make sure to program is running
    app = Application.builder().token(TOKEN).build()

        # Commands handler
    app.add_handler(CommandHandler('start', start_command)) # start_command is called without parenthesis
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

        # Messages handler
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

        # Error handler
    app.add_error_handler(error)
        # Polls the bot
        # Check for the updates constantly if there's new user's message -> It will do this through polling
    print('polling...')# make sure all of the above statements ran
    app.run_polling(poll_interval = 3) # How often bot should check for new messages with interval in seconds



