import random
import string
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = "8906474519:AAGLdemExK3LMp6wPNPFHRM9blSTBFjlVxU"

# Жуткая фраза (без "kill myself")
PHRASE = "i want to kill myself"

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Случайные английские символы (длина 5–10)
    rand_part = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(5, 10)))
    # Добавляем символы 𐕣⸸𖤐 (можно добавить и другие)
    symbols = random.sample(["𐕣", "⸸", "𖤐"], k=random.randint(1, 3))
    rand_part += ''.join(symbols)
    
    # Повторяем фразу случайное число раз (от 5 до 20)
    repeat_count = random.randint(5, 20)
    repeated = (PHRASE + " ") * repeat_count
    
    # Ответ
    await update.message.reply_text(f"{rand_part}\n\n{repeated.strip()}")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))
    app.run_polling()

if __name__ == "__main__":
    main()
