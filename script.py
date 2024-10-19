import logging
from telegram import Update, InputFile
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Replace with your actual bot token and channel ID
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
MOVIE_CHANNEL_ID = '@your_movie_channel'  # Use the username of your movie channel

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome! Send a movie name or type "search <movie_name>" to find a movie.')

def search_movie(update: Update, context: CallbackContext) -> None:
    movie_name = ' '.join(context.args)
    if not movie_name:
        update.message.reply_text('Please specify a movie name. Use "search <movie_name>".')
        return

    # Here you would implement the logic to search the channel for the movie.
    # This is a placeholder implementation.
    context.bot.send_message(chat_id=MOVIE_CHANNEL_ID, text=f"Searching for: {movie_name}")

    # Simulating a file forwarding based on search
    # In a real implementation, you'd fetch the file based on your search logic.
    # For demonstration, we're just using a placeholder file ID.
    file_id = 'YOUR_FILE_ID'  # Replace with actual file ID or logic to get the file
    context.bot.forward_message(chat_id=update.message.chat_id, from_chat_id=MOVIE_CHANNEL_ID, message_id=file_id)

def main() -> None:
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("search", search_movie))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
