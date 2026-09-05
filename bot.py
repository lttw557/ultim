import os
import random
import string
import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes, CommandHandler

# ===== НАСТРОЙКИ =====
TOKEN = "8906474519:AAGLdemExK3LMp6wPNPFHRM9blSTBFjlVxU"  # замените на токен от @BotFather
WEBHOOK_URL = "https://ultim-production.up.railway.app/telegram"  # ваш Railway-адрес
# =====================

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

SYMBOLS = ["𐕣", "⸸", "𖤐"]
PHRASE = "i want to kill myself"   # можно заменить на любую другую

async def handle_business_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обрабатывает сообщения в режиме секретаря."""
    if not update.business_message:
        return
    msg = update.business_message
    conn_id = msg.business_connection_id

    # Хаотичный набор
    rand_part = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(8, 15)))
    for _ in range(random.randint(2, 4)):
        pos = random.randint(0, len(rand_part))
        rand_part = rand_part[:pos] + random.choice(SYMBOLS) + rand_part[pos:]

    # Повторяющаяся фраза
    repeat = random.randint(10, 25)
    repeated = (PHRASE + " ") * repeat
    repeated = repeated.strip()

    # Отправляем два сообщения от имени владельца аккаунта
    await context.bot.send_message(
        chat_id=msg.chat.id,
        text=rand_part,
        business_connection_id=conn_id
    )
    await context.bot.send_message(
        chat_id=msg.chat.id,
        text=repeated,
        business_connection_id=conn_id
    )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Бот-секретарь активирован.")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.UpdateType.BUSINESS_MESSAGE, handle_business_message))
    app.add_handler(CommandHandler("start", start))

    port = int(os.environ.get("PORT", 8443))
    logger.info(f"Запуск webhook на порту {port}, URL: {WEBHOOK_URL}")
    app.run_webhook(
        listen="0.0.0.0",
        port=port,
        webhook_url=WEBHOOK_URL,
        allowed_updates=Update.ALL_TYPES
    )

if __name__ == "__main__":
    main()
