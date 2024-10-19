import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Replace with your actual bot token and channel ID
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
MOVIE_CHANNEL_ID = '@your_movie_channel'  # Use the username of your movie channel
ADMIN_USER_IDS = [123456789]  # Replace with the actual user IDs of admins

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def is_admin(user_id):
    return user_id in ADMIN_USER_IDS

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Welcome! Send a movie name or type "search <movie_name>" to find a movie.')

async def search_movie(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    movie_name = ' '.join(context.args)
    if not movie_name:
        await update.message.reply_text('Please specify a movie name. Use "search <movie_name>".')
        return

    # Simulated search functionality (you would implement this)
    await context.bot.send_message(chat_id=MOVIE_CHANNEL_ID, text=f"Searching for: {movie_name}")
    
    # Forwarding a placeholder file
    file_id = 'YOUR_FILE_ID'  # Replace with actual file ID or logic to get the file
    await context.bot.forward_message(chat_id=update.message.chat_id, from_chat_id=MOVIE_CHANNEL_ID, message_id=file_id)

async def admin_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if is_admin(update.message.from_user.id):
        await update.message.reply_text("Admin command executed!")
    else:
        await update.message.reply_text("You do not have permission to execute this command.")

async def main() -> None:
    application = ApplicationBuilder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("search", search_movie))
    application.add_handler(CommandHandler("admin", admin_command))

    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
