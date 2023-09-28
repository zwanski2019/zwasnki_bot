# zwasnki_bot
Telegram Bot Description:  This Telegram bot, developed using the python-telegram-bot library, initiates a conversation with the user and provides a custom keyboard interface with the following options:  IMEI Services Check Your Account Balance Visit Server for More Upon starting a chat with the bot and sending the /start command, the bot 

from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext

# Define states for the conversation
SELECTING_ACTION = 1

# Start function
def start(update, context):
    user = update.effective_user
    update.message.reply_text(
        f"Hi {user.mention_markdown_v2()}!\n"
        "Please select an action:",
        reply_markup=ReplyKeyboardMarkup([["IMEI Services", "Check Your Account Balance", "Visit Server for More"]], one_time_keyboard=True),
    )

    return SELECTING_ACTION

# Function to handle user input
def handle_user_input(update, context):
    user_input = update.message.text
    if user_input == "IMEI Services":
        # Handle IMEI Services here
        update.message.reply_text("You selected IMEI Services.")
    elif user_input == "Check Your Account Balance":
        # Handle Check Account Balance here
        update.message.reply_text("You selected Check Your Account Balance.")
    elif user_input == "Visit Server for More":
        # Handle Visit Server for More here
        update.message.reply_text("You selected Visit Server for More.")
    else:
        update.message.reply_text("Please select a valid option.")

    return SELECTING_ACTION

# Main function to run the bot
def main():
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token obtained from BotFather
    updater = Updater(token="6352725032:AAFP_sdPCF5_eQcLYmIlQcMAz_IFrHmCCzA", use_context=True)

    dp = updater.dispatcher

    # Define conversation handler
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            SELECTING_ACTION: [MessageHandler(Filters.text & ~Filters.command, handle_user_input)],
        },
        fallbacks=[],
    )

    dp.add_handler(conv_handler)

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
