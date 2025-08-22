import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

BOT_TOKEN = os.getenv("BOT_TOKEN")  # lo pondremos en Render

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Hola! Estoy vivo 24/7 🤖")

async def eco(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # responde con el mismo texto que le mandes
    await update.message.reply_text(update.message.text)

def main():
    if not BOT_TOKEN:
        raise RuntimeError("Falta la variable de entorno BOT_TOKEN")

    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, eco))
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
